# arXiv Tools - Intelligent Literature Workflow Manager

**Author:** Ansatz Gong  
**Version:** 0.1.0 | Last Updated: 2025-02-23

## Background & Motivation

### Problem Statement
arXiv daily submissions may update article tags post-publication. Traditional workflows face two challenges:
1. **Metadata Synchronization Gap**: Local reading history (via browser clicks) isn't synced with arXiv accounts
2. **Version Drift Detection**: No native mechanism to detect newly added/updated articles in historical submissions

### Solution Overview
This toolset bridges arXiv metadata with Zotero reference management and Obsidian knowledge workflows by:
```mermaid
graph LR
    A[arXiv Daily Query] --> B[Zotero Sync Check]
    B --> C{New/Updated?}
    C -->|Yes| D[Markdown Report]
    C -->|No| E[Version Archive]
    D --> F[Obsidian Processing]
```

## Installation & Setup

### Prerequisites
#### Zotero Configuration:

Enable API access: Settings > Advanced > Miscellaneous > Allow other applications on this computer to communicate with Zotero ......

#### Python Environment:

```bash 
pip install .
```

#### Obsidian Setup (Optional):
install and activate plugins : `MetaEdit` `Dataview`


## Core Features
Intelligent Metadata Pipeline


you may write a schedule job to update data everyday.

I recommand conda as python env mananger tool

you can write a bash script

```bash
#!/bin/bash 
source /home/ansatz/.bashrc

# quant_ph
#
#
export my_conda_bin=/home/ansatz/soft/miniconda3/bin/conda 

cd /home/ansatz/data/code/arxiv_reading

$my_conda_bin run -n arxiv python -u arxiv_update.py  --categroy chem-ph,quant-ph --arxiv_folder /home/ansatz/data/obsidian/1/arxiv_datas --time 2025.5
```
```crontab
30 7 * * * bash /home/ansatz/data/code/arxiv_reading/run.sh
```

or you can use python directly, if default python can work.
 
```crontab
30 7 * * * python arxiv_update.py --categroy hep-ex --time 2024.2 --arxiv_folder /home/ansatz/data/obsidian/1/arxiv_datas
```
It means that this command will be executed at 7:30 everyday/
## TO-DO

1. update function and remind 

2. add AI reading and sorting function




