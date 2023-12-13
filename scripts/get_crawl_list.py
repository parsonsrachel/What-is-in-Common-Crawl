from bs4 import BeautifulSoup
import requests
import json

# Script to get a list of all available CommonCrawl crawls (stores the list in the ./data/ directory

# Get html of getting-started page of common crawl,
# which hosts dropdown menu of all available crawls
url = 'https://commoncrawl.org/get-started'
cc_get_started_html = requests.get(url).text
soup = BeautifulSoup(cc_get_started_html, "html.parser")

# Filter for crawls in dropdown menu
choose_crawl_dropdown_div = soup.find("div", {"id": "choose-crawl-list"})
crawl_list_div = choose_crawl_dropdown_div.find("div", {"role": "list"})

# List of all available crawls
crawl_list = [data.text for data in crawl_list_div.find_all('div')]

# Filter 'CC-MAIN-2012', 'CC-MAIN-2009-2010', and 'CC-MAIN-2008-2009'
# as they have data in older format (.ARC instead of warc)
arc_crawls = ['CC-MAIN-2012', 'CC-MAIN-2009-2010', 'CC-MAIN-2008-2009', 'CC-MAIN-2014-10']
crawl_list_warc = [crawl for crawl in crawl_list if crawl not in arc_crawls]

# Save list to file; for reading use json.load(f)
with open("data/available_crawls.json", "w") as f:
    json.dump(crawl_list_warc, f, indent=2)
