import time
from ArXiv_Tools.report import filter_arxiv_to_md
from ArXiv_Tools.arxiv_index_fetch import query_args

# get time 
localtime = time.localtime()
year = localtime.tm_year
month = localtime.tm_mon
# Example: Generate quantum physics report for 2025-02
filter_arxiv_to_md(
    year=year,
    month=month,
    md_folder=r'/home/ansatz/data/obsidian/1/arxiv_datas/quant-ph',
    query_args=query_args  # Customize arXiv categories
)