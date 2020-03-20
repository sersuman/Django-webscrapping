from bs4 import BeautifulSoup
import requests
import csv

# acquires html file from the website in source variable
source = requests.get('http://coreyms.com').text

file = open('scrape.csv','w')
csv_writer = csv.writer(file)
csv_writer.writerow(['Title','body','video_link'])
soup = BeautifulSoup(source, 'lxml')

# prettify does indentation to html file
# print(soup.prettify())

for article in soup.find_all('article'):
    title = article.header.h2.a.text
    print(title)
    print()
    body = article.div.p.text
    print(body)
    print()
    try:
        video_src = article.find('iframe', class_='youtube-player')['src']
        video_id = video_src.split('/')[4]
        video_id = video_id.split('?')[0]
        link = f'https://youtube.com/watch?v={video_id}'
    except Exception as e:
        link = None
    print(link)
    csv_writer.writerow([title, body, link])

file.close()


