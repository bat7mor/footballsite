import pandas 
import simplejson

data2013 = pandas.read_csv("./nfl2013stats.csv")

data2013 = data2013[['Date','TeamName','ScoreOff', 'Opponent', 'ScoreDef']]

bigdata = [] 

for i in data2013.index: 
	score = str(data2013.ix[i]['ScoreOff']) + "-" + str(data2013.ix[i]['ScoreDef'])
	miniarr = [data2013.ix[i]['Date'], data2013.ix[i]['TeamName'], data2013.ix[i]['Opponent'], score]
	bigdata.append(miniarr)

#print bigdata

gameinfo = {"data" : bigdata}

f = open('gameinfo.txt', 'w')
simplejson.dump(gameinfo, f)
f.close()