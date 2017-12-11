from bs4 import BeautifulSoup
import requests

url = 'http://www.xvideos.com/tags'
req_head = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}
info_dict = {}

page = requests.get(url, headers=req_head)
soup = BeautifulSoup(page.text, 'html.parser')
need_unfo = soup.find_all('ul', class_='tags-list')

for num, lol in enumerate(need_unfo):
    for tag in lol.contents:
        if num == 0:
            if tag.find('a').get('title').split(' ')[2] != "English":
                if tag.find('a').get('title'):
                    info_dict.update({tag.find('a').get('title') : int(tag.find('span', class_='navbadge default').get_text().replace(',', ''))})
        else:
            info_dict.update({tag.find('b').get_text(): int(tag.find('span', class_='navbadge default').get_text().replace(',', ''))})

top_tags = sorted(info_dict.items(), key=lambda x: x[1], reverse=True)
print("Top five tags:\n")
for i in range(10):
    print(top_tags[i])