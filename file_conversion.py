import pandas 
import simplejson

data2013 = pandas.read_csv("./nfl2013stats.csv")

data2013 = data2013[['Date','TeamName','ScoreOff', 'Opponent', 'ScoreDef', 'Site', 'Line']]

data2013['home'] = 0
data2013['away'] = 0
data2013['score'] = 0
data2013['line'] = 0

bigdata = [] 

for i in data2013.index: 
	if (data2013.ix[i]['Site'] == 'V'):
		away = data2013.ix[i]['TeamName']
		home = data2013.ix[i]['Opponent']
		score = str(data2013.ix[i]['ScoreDef']) + "-" + str(data2013.ix[i]['ScoreOff'])
		lineval = (-1.0 * float(data2013.ix[i]['Line']))
		if (lineval < 0): 
			line = data2013.ix[i]['Opponent'] + ": " + str(lineval)
		else: 
			line = data2013.ix[i]['Opponent'] + ": +" + str(lineval)

	else: 
		if(data2013.ix[i]['Site'] != 'H'): 
			print (data2013.ix[i]['Site'])
		home = data2013.ix[i]['TeamName']
		away = data2013.ix[i]['Opponent']
		score = str(data2013.ix[i]['ScoreOff']) + "-" + str(data2013.ix[i]['ScoreDef'])
		lineval = data2013.ix[i]['Line']
		if (lineval < 0): 
			line = data2013.ix[i]['TeamName'] + ": " + str(lineval)
		else: 
			line = data2013.ix[i]['TeamName'] + ": +" + str(lineval)		


	data2013.loc[i, 'away'] = away
	data2013.loc[i, 'home'] = home
	data2013.loc[i, 'score'] = score
	data2013.loc[i, 'line'] = line

data2013 = data2013[['Date', 'home', 'away', 'score', 'line']]
data2013 = data2013.drop_duplicates() 

for i in data2013.index:
	miniarr = [data2013.ix[i]['Date'], data2013.ix[i]['home'], data2013.ix[i]['away'], data2013.ix[i]['score'], data2013.ix[i]['line']]
	bigdata.append(miniarr)

#print bigdata

gameinfo = {"data" : bigdata}

f = open('gameinfo.txt', 'w')
simplejson.dump(gameinfo, f)
f.close()