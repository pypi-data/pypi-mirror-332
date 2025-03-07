from setuptools import setup, find_packages

setup(
    name='arxiv_tool_analyzer',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'arxiv',
        'pandas',
        'openpyxl',
    ],
    author='Nooshin Bahador',
    author_email='nooshin.bah@gmail.com',
    description='A tool to search and analyze arXiv papers',
    url='https://github.com/nbahador/arxiv_tool_analyzer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)