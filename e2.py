#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

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

#print(Year, Election_ID)

base = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"

d = dict(zip(Election_ID, Year))

for id in Election_ID:
    lastyear_url = base.format(id)
    lastyear_text = requests.get(lastyear_url).text
    ElecYearData = d[id] + ".csv"

    with open(ElecYearData, 'w') as output:
        output.write(lastyear_text)
