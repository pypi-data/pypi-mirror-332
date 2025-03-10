from exa_py import Exa
from dotenv import load_dotenv
from typing import List
import os

load_dotenv()

class Search:
    """Search the web using the Exa API"""
    def __init__(self):
        self.exa = Exa(api_key=os.getenv('EXA_API_KEY'))
        self.moderation = False
        self.autoprompt = True
        self.type = "auto"

    def search(self, query: str, results=10, include_domains=None, exclude_domains=None, include_text=None, exclude_text=None):
        """Search the web and return results"""
        return self.exa.search(query, num_results=results, type=self.type, moderation=self.moderation, use_autoprompt=self.autoprompt, include_domains=include_domains, exclude_domains=exclude_domains, include_text=include_text, exclude_text=exclude_text).results

    def get(self, url: str):
        """Get the contents of a URL"""
        return self.exa.get_contents([url], summary=True, text=False, livecrawl="auto").results[0]
