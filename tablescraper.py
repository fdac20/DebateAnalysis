import pandas as pd
import wikipedia as wp
html = "https://en.wikipedia.org/wiki/List_of_United_States_presidential_election_results_by_state"
 
df = pd.read_html(html, header=0)[0]  

df.drop(df.index[range(52,98)], inplace=True)
states = df['State']
debateyears = ["1960", "1976", "1980", "1984", "1988", "1992", "1996", "2000 ‡", "2004", "2008", "2012", "2016 ‡"]



for year in debateyears:
    Dem = 0
    Rep = 0
    for i in range(52):
        if df[year][i] == "D":
            Dem+=1
        elif df[year][i] == "R":
            Rep+=1
    print(year, "\nDemocrat Won States:", Dem, "Republican Won States: ", Rep, "\n")

for i, state in zip(range(52), states):
    Dem = 0
    Rep = 0
    for year in debateyears:
        if df[year][i] == "D":
            Dem+=1
        elif df[year][i] == "R":
            Rep+=1
    print(state, "\nTimes Voted Democrat:", Dem, "Times Votes Republican: ", Rep, "\n" )

