from download import NutcDownloader
from bs4 import BeautifulSoup

import pandas as pd

if __name__ == '__main__':
    downloader = NutcDownloader('1081')

    all_url = downloader.get_all_url()

    html_text = downloader.get_html_text('1320191191')

    soup = BeautifulSoup(html_text, 'html.parser')

    trs = soup.find_all('tr')
    trs = trs[2:]

    tds = [tr.find_all('td') for tr in trs]
    tds = [tuple(map(lambda tag: tag.text, td)) for td in tds]

    columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a = pd.DataFrame(tds)
    a = a[columns]
