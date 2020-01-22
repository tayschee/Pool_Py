import pandas as pd
from FileLoader import FileLoader


def YoungestFellah(df, year):
    dico = {}
    df = df[df.Year == year]
    dfs = df[df.Sex == 'F']
    dico['Female'] = dfs.Age.min()
    dfs = df[df.Sex == 'M']
    dico['Male'] = dfs.Age.min()
    print(dico)

df = FileLoader()
data = df.load('../resources/athlete_events.csv')
YoungestFellah(data, 2008)


