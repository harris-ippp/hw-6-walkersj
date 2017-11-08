#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

addr = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"

resp = requests.get(addr)
soup = BeautifulSoup (resp.content , "html.parser") #import the data and spit out html code

soup.find('table')
rows = soup.find_all('tr', 'election_item') #look for the table with all the rows and elections items

Year = [] #create an empty list, and add the contents of years in there
for row in rows:
    Year.append(row.contents[1].text)

Election_ID = [] #create an empty list, and add the last 5 digits in the id entry
for i in range(len(rows)):
    Election_ID.append(rows[i]['id'][-5:])

#print(Year, Election_ID) #check for correct output

base = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"

d = dict(zip(Election_ID, Year)) #create a dictionary for all the years and election ids together

for id in Election_ID:
    lastyear_url = base.format(id)
    lastyear_text = requests.get(lastyear_url).text
    ElecYearData = d[id] + ".csv" #puts the ids in csv format to prepare to download

    with open(ElecYearData, 'w') as output:
        output.write(lastyear_text) #downloads all the csv files for election years
