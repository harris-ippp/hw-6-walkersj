#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

addr = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"

resp = requests.get(addr)
soup = BeautifulSoup (resp.content , "html.parser")

soup.find('table')
rows = soup.find_all('tr', 'election_item')

Year = []
for row in rows:
    Year.append(row.contents[1].text)

Election_ID = []
for i in range(len(rows)):
    Election_ID.append(rows[i]['id'][-5:])

print(Year, Election_ID)
