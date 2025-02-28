import os
from .arxiv_index_fetch import query_arxiv_dict, query_args
from .zotero_query import zotero_query
from .codex import replace_characters
import logging

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
    arxiv_id_text = '[' + arxiv_id+ ']' + '(' + _get_arxiv_url(arxiv_id) + ')'
    title_text = title
    author_text = ''
    for author in authors:
        author_text += f'{author}, '
    abstract_text = abstract
    for key in replace_characters:
        abstract_text = abstract_text.replace(key, replace_characters[key])
    arxiv_markdown = f'''
### {arxiv_id_text}

Title:  {title_text}

Authors:  {author_text}

Abstract: 
> [!quote]- Abstract
> {abstract_text}


'''
    return arxiv_markdown


def _gen_data(arxiv_dict, Zot_):
    collect_dict = {}
    not_collect_dict = {}
    # TO-DO
    # update_dict = {} 
    for _, (arxiv_id, (title, authors, abstract)) in enumerate(arxiv_dict.items()):
        arxiv_doi = _get_arxiv_doi(arxiv_id)

        query_res = Zot_.query_('DOI', arxiv_doi)
        if query_res.__len__() :
            last_ok = query_res
            collect_dict[arxiv_id] =  _gen_arxiv_markdown(arxiv_id, title, authors, abstract)
        else:

            not_collect_dict[arxiv_id] =  _gen_arxiv_markdown(arxiv_id, title, authors, abstract)
    return collect_dict, not_collect_dict


def _gen_oneday_markdown(date_string, oneday_arxiv_dict, Zot_):
    collect_dict, not_collect_dict = _gen_data(oneday_arxiv_dict, Zot_)

    # date_string = '2025-02-01'

    date_markdown =f'# {date_string} preprint by arxiv_tools\n\n'
    date_markdown += '## collected\n\n'
    for key in sorted([key for key in collect_dict]):
        value = collect_dict[key]
        date_markdown += value

    date_markdown += '## not collected\n\n'

    for key in sorted([key for key in not_collect_dict]):
        value = not_collect_dict[key]
        date_markdown += value

    return date_markdown

def filter_arxiv_to_md(year: int, month: int, md_folder: str, query_args: dict=query_args):

    Zot_ = zotero_query() # default local use
    Zot_.get_everything()
    root_dir = md_folder
    
    for i in range(31):
        day = i + 1
        date_from_date = f'{year}-{month:02}-{day:02}'
        date_to_date = f'{year}-{month:02}-{day+1:02}'
        # print(date_from_date, date_to_date)
        arxiv_dict = query_arxiv_dict(date_from_date, date_to_date, query_args)
        if arxiv_dict.__len__():
            year_dir = os.path.join(root_dir, f'{year}')
            month_dir = os.path.join(year_dir, f'{month:02}')
            # date_dir = os.path.join(month_dir, f'{day:02}')
            os.makedirs(month_dir, exist_ok=True)
            date_string = f'{year}-{month:02}-{day:02}'
            print(f'processing {date_from_date}')
            markdown_str = _gen_oneday_markdown(date_string, arxiv_dict, Zot_)
            with open(
                os.path.join(month_dir, f'{day:02}.md'), 
                "w", encoding="utf-8"
            ) as f:
                f.write(markdown_str)