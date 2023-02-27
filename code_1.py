import json
import csv

# Open the json file
with open('jihyo fancam.json', encoding='utf8') as f:
    data = json.load(f)

# Create a csv file
with open('jihyofc.csv', 'w', encoding='utf8', newline='') as file:
    writer = csv.writer(file)

    # This makes the headers for the csv
    writer.writerow(["title", "link"])

    # The loop that itterates through the json file
    for num in range(1, 250):
        links = data['items'][num]['id']['videoId']  # this pulls the urls
        title = data['items'][num]['snippet']['title'] # pulls the video titles
        print(f'{num} : {title}')
        print(f'https://www.youtube.com/watch?v={links}')
        writer.writerow([title, f'https://www.youtube.com/watch?v={links}']) # for every title and url it makes a new line



################################################
# Currently breaks here for some reason

# links = data['items'][45]['id']['videoId']
# print(links)