from setuptools import setup

setup(
    name='Arxiv_Tools',
    python_requires='>3.8.0',
    version='0.0.1',
    author='Cunxi Gong',
    author_email='ansatzMe@outlook.com',
    description='Auto-fetch  arxiv to md ',
    url='https://github.com/ansatzX/arxiv_tools',

    packages=["ArXiv_Tools"],
    package_dir={'': 'src'},
)