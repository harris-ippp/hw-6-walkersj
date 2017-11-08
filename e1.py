#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

addr = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"

resp = requests.get(addr)
soup = BeautifulSoup (resp.content , "html.parser") #import the data and spit out html code

soup.find('table') #look for the table with all the rows and elections items
rows = soup.find_all('tr', 'election_item')

Year = [] #create an empty list, and add the contents of years in there
for row in rows:
    Year.append(row.contents[1].text) 

Election_ID = [] #create an empty list, and add the last 5 digits in the id entry
for i in range(len(rows)):
    Election_ID.append(rows[i]['id'][-5:])

print(Year, Election_ID)
