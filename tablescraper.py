import pandas as pd
import wikipedia as wp
html = "https://en.wikipedia.org/wiki/List_of_United_States_presidential_election_results_by_state"
 
df = pd.read_html(html, header=0)[0]  

df.drop(df.index[range(52,98)], inplace=True)
states = df['State']
debateyears = ["1960", "1976", "1980", "1984", "1988", "1992", "1996", "2000 ‡", "2004", "2008", "2012", "2016 ‡"]
wins = ["D", "D", "R", "R", "R", "D", "D", "R", "R", "D", "D", "R"]
swingstates = ["Florida", "Iowa", "Michigan", "Minnesota", "Nevada", "New Hampshire", "North Carolina", "Ohio", "Pennsylvania", "Virginia", "Wisconsin"]



for year, win in zip(debateyears, wins):
    Dem = 0
    Rep = 0
    Dsstates = 0
    Rsstates = 0
    for i in range(52):
        Rhit = 0
        Dhit = 0
        if df[year][i] == "D":
            Dem+=1
            Dhit=1
        elif df[year][i] == "R":
            Rep+=1
            Rhit=1
        for sstate in swingstates:
            if states[i] == sstate and Dhit == 1:
                Dsstates+=1
            elif states[i] == sstate and Rhit == 1:
                Rsstates+=1

    print(year, "\n\nDemocrat Won States:", Dem, "Republican Won States: ", Rep, "\nDemocrat Won Swing States:", Dsstates, "Republican Won Swing States: ", Rsstates)
    if win == "D":
        print("Democrat Won Election\n")
    elif win == "R":
        print("Republican Won Election\n")

for i, state in zip(range(52), states):
    Dem = 0
    Rep = 0

    for year in debateyears:
        if df[year][i] == "D":
            Dem+=1
            Dhit=1
        elif df[year][i] == "R":
            Rep+=1
            Rhit=1


    print(state, "\nTimes Voted Democrat:", Dem, "Times Votes Republican: ", Rep, "\n")
