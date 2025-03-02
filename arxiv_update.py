import time
import os
import argparse
from ArXiv_Tools.report import filter_arxiv_to_md
from ArXiv_Tools.arxiv_index_fetch import query_args

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--time ", default='1949.10', help="timeto query", type=str)
    parser.add_argument("--arxiv_folder", default='/home/ansatz/data/obsidian/1/arxiv_datas/', help="place to store arxiv datas", type=str)
    parser.add_argument("--categroy", default='quant-ph', help="category of arxivs also the folder", type=str)

    args = parser.parse_args() 
    arxiv_folder= args.arxiv_folder
    categroy = args.categroy
    time = args.time
    for time_ in time.split(','):
        for cat_ in categroy.split(','):
            md_folder = os.path.join(arxiv_folder, cat_)
            if cat_ == 'quant-ph':
                query_args = query_args

            if time == '1949.10':
                localtime = time.localtime()
                year = int(localtime.tm_year)
                month = int(localtime.tm_mon)
            else:
                year = time.split('.')[0]
                month = time.split('.')[1]
            # Example: Generate quantum physics report for 2025-02
            filter_arxiv_to_md(
                year=year,
                month=month,
                md_folder=md_folder,
                query_args=query_args  # Customize arXiv categories
            )