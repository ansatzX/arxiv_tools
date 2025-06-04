import os
from unicodedata import category
from .arxiv_index_fetch import query_arxiv_dict
from .zotero_query import zotero_query
from .codex import replace_characters, quant_ph
from . import arxiv_logger
import logging

logger = arxiv_logger

def _get_arxiv_doi(arxiv_id):
    arxiv_doi = arxiv_id.replace(':', '.')
    arxiv_doi = f'10.48550/{arxiv_doi}'
    return arxiv_doi

def _get_arxiv_url(arxiv_id):
    root_url = 'https://arxiv.org/abs'
    arg = arxiv_id.replace('arXiv:', '/')
    arxiv_url = f'{root_url}{arg}'
    return arxiv_url

def _gen_arxiv_markdown(arxiv_id, title, authors, abstract):
    arxiv_link_text = '[' + arxiv_id+ ']' + '(' + _get_arxiv_url(arxiv_id) + ')'
    title_text = title
    author_text = ''
    for author in authors:
        author_text += f'{author}, '
    abstract_text = abstract
    for key in replace_characters:
        abstract_text = abstract_text.replace(key, replace_characters[key])
    arxiv_markdown = f'''
### {arxiv_id}

Links:

- [ ] {arxiv_link_text} 

Title:  {title_text}

Authors:  {author_text}

Abstract: 
> [!quote]- Abstract
> {abstract_text}


'''
    return arxiv_markdown


def _gen_data(arxiv_dict, Zot_=None):
    collect_dict = {}
    not_collect_dict = {}
    # TO-DO
    # update_dict = {} 
    for _, (arxiv_id, (title, authors, abstract)) in enumerate(arxiv_dict.items()):
        arxiv_doi = _get_arxiv_doi(arxiv_id)
        try:
            query_res = Zot_.query_('DOI', arxiv_doi)
        except:
            query_res = []
        if query_res.__len__() :
            last_ok = query_res
            collect_dict[arxiv_id] =  _gen_arxiv_markdown(arxiv_id, title, authors, abstract)
        else:

            not_collect_dict[arxiv_id] =  _gen_arxiv_markdown(arxiv_id, title, authors, abstract)
    return collect_dict, not_collect_dict


def _gen_oneday_markdown(date_string, oneday_arxiv_dict, Zot_, old_data=None):

    collect_dict, not_collect_dict= _gen_data(oneday_arxiv_dict, Zot_)
    category = oneday_arxiv_dict['category']
    new_data = []
    date_markdown = f'# {date_string} preprint by arxiv_tools\n\n'
    date_markdown +=  f'''
---
tags:
  - #{category}-{date_string}
---


```dataview
TASK
from #{category}-{date_string}

WHERE completed

```

'''
    date_markdown += '## collected\n\n'
    for key in sorted([key for key in collect_dict]):
        value = collect_dict[key]
        date_markdown += value
        if old_data is not None:
            if key not in old_data:
                new_data.append(key)

    date_markdown += '## not collected\n\n'

    for key in sorted([key for key in not_collect_dict]):
        value = not_collect_dict[key]
        date_markdown += value
        if old_data is not None:
            if key not in old_data:
                new_data.append(key)
            
    if new_data.__len__(): 
        date_markdown += '## update \n\n'

        for key in sorted([key for key in new_data]):
            value = f'- [ ] [[#{key}]]\n'
            date_markdown += value
        
    return date_markdown

def parse_old_report(file_path):
    if os.path.exists(file_path):
        
        with open(
                file_path, 
                "r", encoding="utf-8"
            ) as f:
            lines = f.readlines()
        old_title_lines = []
        for line in lines:
            if line.startswith('### arXiv:'):
                arxiv_id_str = line[4:-1].strip()
                old_title_lines.append(arxiv_id_str)
            if line.startswith('- [x]'):
                arxiv_id_str = line[8:-2].strip()
                old_title_lines.append(arxiv_id_str)
            
        return old_title_lines
    else:
        return None
        
def filter_arxiv_to_md(year: int, month: int, md_folder: str, query_args: dict=quant_ph, categroy='quant-ph'):

    try:
        Zot_ = zotero_query() # default local use
        Zot_.get_everything()
    except:
        Zot_ = None
    root_dir = md_folder
    
    for i in range(31):
        day = i + 1
        date_from_date = f'{year}-{month:02}-{day:02}'
        date_to_date = f'{year}-{month:02}-{day+1:02}'
        # print(date_from_date, date_to_date)
        arxiv_dict = query_arxiv_dict(date_from_date, date_to_date, query_args)
        arxiv_dict['categroy'] = categroy
        if arxiv_dict.__len__():
            logger.info(f'{arxiv_dict.__len__()}')
            year_dir = os.path.join(root_dir, f'{year}')
            month_dir = os.path.join(year_dir, f'{month:02}')
            # date_dir = os.path.join(month_dir, f'{day:02}')
            os.makedirs(month_dir, exist_ok=True)
            date_string = f'{year}-{month:02}-{day:02}'
            logger.info(f'processing {date_from_date}, total num: {arxiv_dict.__len__()}')
            oneday_report_file = os.path.join(month_dir, f'{day:02}.md')
            parse_old = parse_old_report(oneday_report_file)
            # print(parse_old)
            markdown_str = _gen_oneday_markdown(date_string, arxiv_dict, Zot_, parse_old)
            # print(markdown_str)
            with open(
                oneday_report_file, 
                "w", encoding="utf-8"
            ) as f:
                f.write(markdown_str)