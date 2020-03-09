from bs4 import BeautifulSoup
import requests
# import parsel
from lxml import etree
import threading


def request_maoyan(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    html = requests.get(url, headers=headers)
    # req = parsel.Selector(html)
    return html.text


# names = xpath_html.xpath("//p[@class='name']/a/text()")
# for name in names:
#     print(name)
def parse_result(html):
    xpath_html = etree.HTML(html)
    grades = xpath_html.xpath("//span[@class='stonefont']/text()")
    for grade in grades:
        print(grade)


def main():
    url = 'https://maoyan.com/board/1'
    res = request_maoyan(url)
    items = parse_result(res)

if __name__ == '__main__':
    main()