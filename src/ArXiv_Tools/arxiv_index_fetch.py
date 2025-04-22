import re
from urllib.parse import urlencode
import feedparser

from bs4 import BeautifulSoup

from .codex import quant_ph
sub = 'quant-ph'

search_url = 'https://arxiv.org/search/advanced?'

test_url = 'https://arxiv.org/search/advanced?advanced=&terms-0-term=&terms-0-operator=AND&terms-0-field=title&classification-physics=y&classification-physics_archives=quant-ph&classification-include_cross_list=include&date-filter_by=date_range&date-year=&date-from_date=2025-02-01&date-to_date=2025-02-02&date-date_type=submitted_date&abstracts=show&size=200&order=submitted_date'



def query_arxiv_dict(date_from_date='2025-02-01', date_to_date='2025-02-02', query_args=quant_ph):

    query_args['date-from_date'] = date_from_date
    query_args['date-to_date'] = date_to_date

    query_dict = {}

    url_args = re.sub(
            "%2B", "+", urlencode(query_args)
        )
    # print(url_args)

    url = search_url + url_args

    results = feedparser.parse(url)

    summary_text = results['feed']['summary']

    so = BeautifulSoup(summary_text, 'lxml')


    find_results = so.find_all(class_='arxiv-result')

    tmp_res = []
    for res in find_results:
        aso = BeautifulSoup(res.__str__(), 'lxml')

        list_title = aso.find(class_='list-title')
        arxiv_id_text = list_title.find('a').text
        arxiv_id = arxiv_id_text # with or without v version 

        title = aso.find(class_='title')
        title = title.text.strip()

        _authors = aso.find(class_='authors')
        authors = []
        for s in _authors.find_all('a'):
            authors.append(s.text)

        abstract = aso.find(class_='abstract-full')
        abstract = abstract.text.strip() # with less
        query_dict[arxiv_id] = [title, authors, abstract]
        # tmp_res.append([arxiv_id, title, authors, abstract])

    return query_dict
