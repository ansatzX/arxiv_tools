from setuptools import setup

with open('requirements.txt', 'r') as f:
    req = f.read()
setup(
    name='Arxiv_Tools',
    python_requires='>3.8.0',
    version='0.1.0',
    author='Cunxi Gong',
    author_email='ansatzMe@outlook.com',
    description='Auto-fetch arxiv to md ',
    url='https://github.com/ansatzX/arxiv_tools',
    install_requires=req,
    packages=["ArXiv_Tools"],
    package_dir={'': 'src'},
)