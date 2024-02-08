import sys

sys.path.insert(0, 'config')
sys.path.insert(0, 'models')

import config
from url_scraper import UrlScraper

if __name__ == "__main__":
    
    # Iterate over each website defined in the configuration
    for web in config.dataset["webs"]:
        
        # Skip websites marked as 'ignore' in the configuration
        if "ignore" in web.keys():
            continue
        
        # Create a UrlScraper object with the specified parameters
        scraper = UrlScraper(
            path = config.dataset["path"],
            patch_cache = config.dataset["path_cache"],
            category = web["category"],
            name = web["name"],
            url = web["url"],
            headers = config.dataset["headers"],
            namespace = web["namespace"],
            xpath = web["xpath"],
            options = web["options"],
            limit = web["limit"] if "limit" in web.keys() else None
        )

        # Execute the scraping process
        scraper.run()