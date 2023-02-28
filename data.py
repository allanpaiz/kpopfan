import json
import csv

with open('jihyo fancam.json', encoding='utf8') as f:
    data = json.load(f)

### Make naming of file a variable, pull it from api file
    #from api import search
    # open('{search}.csv', 'w', encoding='utf8', newline='') as file:

url_list = data['items']

link_list = []
title_list = []

for i in url_list:
    result = i['id']
    if result['kind'] == 'youtube#playlist':
        continue

    url = result['videoId']
    link_list.append(f'https://www.youtube.com/watch?v={url}')


for i in url_list:
    result = i['snippet']
    presult = i['id']
    if presult['kind'] == 'youtube#playlist':
        continue

    title = result['title']
    title_list.append(title)


with open('jihyofc.csv', 'w', encoding='utf8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["title", "link"])
    
    for i in range(len(title_list)):
        writer.writerow([title_list[i], link_list[i]])

