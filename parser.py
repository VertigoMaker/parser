import requests as req
import bs4
import time


def get_urls():
    agents = {"User-Agent": "Mozilla/5.0"}
    source = req.get('https://yummyanime.club/top', headers=agents).text
    soup = bs4.BeautifulSoup(source, 'lxml')
    urls = [url['href'] for url in soup.find_all(class_="image-block")]
    urls_str = []
    for url in urls:
        url = "https://yummyanime.club" + str(url)
        urls_str.append(url)
    return urls_str


def get_source(url):
    agents = {"User-Agent" : "Mozilla/5.0"}
    source = req.get(url, headers = agents).text
    return source


def extract_data(source):
    soup = bs4.BeautifulSoup(source, "lxml")
    text = [t for t in soup.find_all(text=True) if t.parent.name == "p"]
    print(text[0])


urls = get_urls()
i=0
while(i<len(urls)):
    time.sleep(5)
    print(extract_data(get_source(urls[i])))
    i+=1