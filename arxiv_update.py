import time
import os
import argparse
import logging
from ArXiv_Tools import arxiv_logger
from ArXiv_Tools.report import filter_arxiv_to_md
from ArXiv_Tools.codex import query_args

logger = arxiv_logger

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--time", default='1949.10', help="timeto query", type=str)
    parser.add_argument("--arxiv_folder", default='/home/ansatz/data/obsidian/1/arxiv_datas/', help="place to store arxiv datas", type=str)
    parser.add_argument("--categroy", default='quant-ph', help="category of arxivs also the folder", type=str)

    args = parser.parse_args() 
    arxiv_folder= args.arxiv_folder
    categroy = args.categroy
    time_ = args.time
    for time__ in time_.split(','):
        for cat_ in categroy.split(','):
            md_folder = os.path.join(arxiv_folder, cat_)
            try:
                _query_args = query_args[cat_]
            except:
                logger.info(f'cat_: {cat_} not supported, create issue to remind author')
                raise RuntimeError
            if time__ == '1949.10':
                localtime = time.localtime()
                year = int(localtime.tm_year)
                month = int(localtime.tm_mon)
            else:
                year = int(time__.split('.')[0])
                month = int(time__.split('.')[1])
            # Example: Generate quantum physics report for 2025-02
            logger.info(f'scirpt is runing to fecth {cat_} {time__}')
            # print('zxm')
            filter_arxiv_to_md(
                year=year,
                month=month,
                md_folder=md_folder,
                query_args=_query_args,  # Customize arXiv categories
                category=cat_
            )