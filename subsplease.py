#VERSION: 1.0
# AUTHORS: PlutoMonkey

from html.parser import HTMLParser
from helpers import download_file, retrieve_url
from novaprinter import prettyPrinter
# some other imports if necessary
import json
from urllib.parse import urlparse
from urllib.parse import parse_qs

class subsplease(object):
    url = 'https://subsplease.org/'
    name = 'SubsPlease'
    supported_categories = {'all': ''}

    def search(self, what, cat='all'):
        for page in range(6):
            search_url = f"https://subsplease.org/api/?f=search&tz=$&s={what}&p={page}"
            response = retrieve_url(search_url)
            response_json = json.loads(response)
            
            for result_name, result_data in response_json.items():
                for download in result_data["downloads"]:
                    magnet_link = download["magnet"]
                    parsed_url = urlparse(magnet_link)
                    size = parse_qs(parsed_url.query)['xl'][0]
                    
                    res = {'link': magnet_link,
                        'name': f"[SubsPlease] {result_name} ({download['res']}p)",
                        'size': size,
                        'seeds': '-1',
                        'leech': '-1',
                        'engine_url': search_url,
                        'desc_link': '-1'}
                    prettyPrinter(res)
        