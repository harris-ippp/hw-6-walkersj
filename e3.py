#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
%matplotlib inline

dataframe = []

years = ['2016', '2012', '2008', '2004', '2000', '1996', '1992', '1988', '1984', '1980', '1976', '1972', '1968', '1964', '1960', '1956', '1952', '1948', '1944', '1940', '1936', '1932', '1928', '1924']
for y in range(0, len(years)):

    file = years[y] + ".csv"
    header = pd.read_csv(file, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()

    dff = pd.read_csv(file, index_col = 0, thousands = ",", skiprows = [1])

    dff.rename(inplace = True, columns = d) # rename to democrat/republican
    dff.dropna(inplace = True, axis = 1)    # drop empty columns
    dff["Year"] = years[y]

    df1 = dff[["Republican", "Democratic", "Total Votes Cast", "Year"]].head()

    dataframe.append(df1.head(4))

BAMMM = pd.concat(dataframe)

BAMMM["Rshare"] = BAMMM["Republican"]/BAMMM["Total Votes Cast"]
BAMMM.sort_index()

fig, ax = plt.subplots()
BAMMM.reset_index().groupby("County/City").plot(x="Year", y="Rshare", ax=ax, legend=False)
plt.show()
ax.figure.savefig('counties.pdf')
