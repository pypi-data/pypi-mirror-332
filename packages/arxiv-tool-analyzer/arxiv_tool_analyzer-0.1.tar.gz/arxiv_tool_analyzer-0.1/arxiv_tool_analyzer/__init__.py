# Import functions from the modules to make them available at the package level
from .arxiv_search import fetch_arxiv_data, save_to_excel
from .merge_files import merge_excel_files
from .search_terms import search_terms_in_abstracts

# Optional: Define what should be imported when using `from arxiv_tool import *`
__all__ = [
    'fetch_arxiv_data',
    'save_to_excel',
    'merge_excel_files',
    'search_terms_in_abstracts'
]