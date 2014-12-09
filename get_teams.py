import pandas 
import simplejson

data2013 = pandas.read_csv("./nfl2013stats.csv")

teams = []

for i in data2013.index: 
	if (not (data2013.ix[i]['TeamName'] in teams)): 
		teams.append(data2013.ix[i]['TeamName'])

f = open('teams.json', 'w')
simplejson.dump(teams, f)
f.close()