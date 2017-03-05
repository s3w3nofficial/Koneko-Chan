import wptools
from scripts.Respounder import *

class wiki():
    def wiki_search(self, query):
        self.query = query
        query = wptools.page(query).get_wikidata()
        try: 
            query = query.wikidata['description']
        except:
            Respounder().respound("Error query not found")

        Respounder().respound("I find thease informations about your request" + query)