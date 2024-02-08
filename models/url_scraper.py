import sys

sys.path.insert(0, 'utils')

import os
import csv
import hashlib
import requests
from lxml import etree
from bs4 import BeautifulSoup
from utils import create_path

class UrlScraper(object):
    """
    A class for scraping URLs from web pages.
    """

    def __init__(self, *, path: str = None, patch_cache: str = None, category: str = None, name: str = None, url: str = None, headers: dict = None, namespace: str = None, xpath: str = None, options: dict = None, limit: int) -> None:
        """
        Initialize UrlScraper with necessary parameters.

        Args:
        - path (str): The base path for storing scraped data.
        - patch_cache (str): The cache path for storing cached data.
        - category (str): The category of the web page.
        - name (str): The name of the web page.
        - url (str): The URL of the web page.
        - headers (dict): The HTTP headers to be sent with the request.
        - namespace (str): The namespace for XPath.
        - xpath (str): The XPath expression to extract URLs.
        - options (dict): The options to get the scraped data.
        - limit (int): The maximum number of urls to scrape.
        """

        self.path = path
        self.patch_cache = patch_cache
        self.category = category
        self.name = name
        self.url = url
        self.headers = headers
        self.namespace = namespace
        self.xpath = xpath
        self.options = options
        self.limit = limit

    def get_response(self) -> str:
        """
        Get the HTTP response from the web page.

        Returns:
        - str: The HTTP response content.
        """

        create_path(os.path.join(self.path, self.patch_cache, self.category, self.name))

        response = requests.get(self.url, headers = self.headers)

        if (response.status_code == 200):
            with open(os.path.join(self.path, self.patch_cache, self.category, self.name, "response.txt"), "w", encoding = "utf-8")  as f:
                response.encoding = "utf-8"
                f.write(response.text.replace("ï»¿", ""))
            
            print("[INFO] Response saved successfully")
        else:
            print(f"[ERROR] Response code is {response.status_code}")
            exit(1)

        return response.text

    def get_urls(self, response: str = None):
        """
        Extract URLs from the HTTP response.

        Args:
        - response (str): The HTTP response content.

        Returns:
        - list[str]: A list of URLs extracted from the response.
        """

        print("[INFO] Getting urls from response")

        document = etree.fromstring(response.encode("utf-8"))

        return document.xpath(self.xpath, namespaces = self.namespace)

    def export_urls(self, urls = None) -> None:
        """
        Export the extracted URLs to a file.

        Args:
        - urls (list[str]): A list of URLs to be exported.
        """

        print("[INFO] Exporting urls from response")

        fields = ['category', 'url'] 
        
        with open(os.path.join(self.path, self.patch_cache, self.category, self.name, "urls.txt"), "w") as f:            
            write = csv.writer(f)
            
            write.writerow(fields)
            write.writerows([[self.category, url] for url in urls])

    def get_content(self, url: str = None) -> None:
        """
        Get the content of the URL.

        Args:
        - url (str): A URL to be exported.
        """
        
        url = url.strip()

        if os.path.exists(os.path.join(self.path, self.patch_cache, self.category, self.name, hashlib.sha1(url.encode()).hexdigest() + ".txt")) == True:
            print(f"[INFO] Response already exists: {url}")
            return

        try:
            response = requests.get(url, headers = self.headers)
            
            if (response.status_code == 200):
                soup = BeautifulSoup(response.text, "html.parser")

                """
                with open("test.html", "w") as f:
                    f.write(soup.prettify())
                """

                content = soup.find(self.options["container"], attrs = self.options["container_attrs"])
                elements = content.find_all(self.options["elements_to_extract"])

                if self.options["elements_ignore_last"]:
                    elements = elements[:-1]

                with open(os.path.join(self.path, self.patch_cache, self.category, self.name, (hashlib.sha1(url.encode()).hexdigest() + ".txt")), "w") as f:
                    for element in elements:
                        print(element.text, file = f, end = "")
                
                print(f"[INFO] Response saved successfully: {url}")
            else:
                print(f"[ERROR] Response code is {response.status_code}: {url}")
        except Exception as e:
            print(f"[ERROR] Something bad is going on: {url}")

    def run(self) -> None:
        """
        Executes the URL scraping process.
        """

        response = self.get_response()
        urls = self.get_urls(response)
        self.export_urls(urls)

        with open(os.path.join(self.path, self.patch_cache, self.category, self.name, "urls.txt"), "r", newline = "") as f:            
            reader = csv.DictReader(f)

            counter = 0

            for url in reader:
                if self.limit != None and counter >= self.limit:
                    continue
                
                self.get_content(url["url"])

                counter += 1