from pyzotero import zotero

class zotero_query:

    def __init__(self, library_id='000000', library_type='user', local=True):
        zot = zotero.Zotero(library_id=library_id, library_type=library_type, local=local)
        self.zot = zot

    def get_everything(self):

        items = self.zot.everything(self.zot.items())
        self.items = items
        # return items
    
    def query_(self, query_key: str='DOI',doi_string: str = '10.48550/arXiv.2502.07673'):

        matching_items = [item for item in self.items if query_key in item['data'] and item['data'][query_key] == doi_string]

        return matching_items
    
    def slow_query_(self, query_key: str='DOI',doi_string: str = '10.48550/arXiv.2502.07673'):

        self.get_everything()
        matching_items = self.query_(query_key, doi_string)

        return matching_items

