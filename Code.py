import enum
from bs4 import BeautifulSoup

import requests
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

html_page = requests.get(START_URL).text

time.sleep(10)

headers = ["Constellation", "Distance", "Mass", "Radius"]

brown_dwarfs_data = []


def scrape():
    soup = BeautifulSoup(html_page, 'html.parser')

    table_tag = soup.find_all('table')[4].find('tbody')
    tr_tags = table_tag.find_all('tr')

    for count, tr_tag in enumerate(tr_tags):
        temp_list = []
        td_tags = tr_tag.find_all('td')
        for index, td_tag in enumerate(td_tags):
            if index == 1 or index == 5 or index == 7 or index == 8:
                value = td_tag.text.strip()
                if value == "":
                    value = "NA"

                temp_list.append(value)

        brown_dwarfs_data.append(temp_list)


scrape()
brown_dwarfs_data.pop(0)
print(brown_dwarfs_data)

with open(r'Projects\C128\venv\data.csv', 'w+', encoding="utf-8") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(brown_dwarfs_data)
