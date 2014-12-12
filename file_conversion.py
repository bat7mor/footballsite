import pandas
import simplejson
import math

predictions = pandas.read_csv("./predictions.csv")

predictions['home'] = 0
predictions['away'] = 0
predictions['score'] = 0
predictions['line'] = 0
predictions['home prediction'] = 0
predictions['away prediction'] = 0

bigdata = [] 

for i in predictions.index: 
	if (predictions.ix[i]['Site'] == 'V'):
		away = predictions.ix[i]['TeamName']
		home = predictions.ix[i]['Opponent']
		homecity = (home).rsplit(' ', 1)[0]
		awaycity = (away).rsplit(' ', 1)[0]
		if math.isnan(predictions.ix[i]['ScoreOff']): 
			score = "Undetermined"
		else:
			score = homecity + " " + str(int(predictions.ix[i]['ScoreDef'])) + " - " + awaycity + " " + str(int(predictions.ix[i]['ScoreOff']))
		awaypredict = predictions.ix[i]['PredictedScore']
		homepredict = 0
		lineval = float(predictions.ix[i]['Line'])
		if (lineval < 0): 
			line = predictions.ix[i]['Opponent'] + ": " + str(lineval)
		else: 
			line = predictions.ix[i]['Opponent'] + ": +" + str(lineval)

	else: 
		if(predictions.ix[i]['Site'] != 'H'): 
			print (predictions.ix[i]['Site'])
		home = predictions.ix[i]['TeamName']
		away = predictions.ix[i]['Opponent']
		homecity = (home).rsplit(' ', 1)[0]
		awaycity = (away).rsplit(' ', 1)[0]
		homepredict = predictions.ix[i]['PredictedScore']
		awaypredict = 0
		if math.isnan(predictions.ix[i]['ScoreOff']): 
			score = "Undetermined"
		else: 
			score =  homecity + " " + str(int(predictions.ix[i]['ScoreOff'])) + " - " + awaycity + " " + str(int(predictions.ix[i]['ScoreDef']))
		lineval = -1.0 * float(predictions.ix[i]['Line'])
		if (lineval < 0): 
			line = predictions.ix[i]['TeamName'] + ": " + str(lineval)
		else: 
			line = predictions.ix[i]['TeamName'] + ": +" + str(lineval)		

	predictions.loc[i, 'away'] = away
	predictions.loc[i, 'home'] = home
	predictions.loc[i, 'score'] = score
	predictions.loc[i, 'line'] = line
	predictions.loc[i, 'home prediction'] = homepredict
	predictions.loc[i, 'away prediction'] = awaypredict


predictions = predictions[['Date', 'home', 'away', 'score', 'line', 'home prediction', 'away prediction']]

predictcombined = predictions.groupby(['Date', 'home', 'away', 'score', 'line'], as_index=False).sum()

predictcombined['Date'] = pandas.to_datetime(predictcombined['Date'])
predictcombined = predictcombined.sort(['Date'])

print predictcombined.head()


for i in predictcombined.index:
	homecity = (str(predictcombined.ix[i]['home'])).rsplit(' ', 1)[0]
	awaycity = (str(predictcombined.ix[i]['away'])).rsplit(' ', 1)[0]
	prediction = homecity + str(predictcombined.ix[i]['home prediction']) + " - " + awaycity + str(predictcombined.ix[i]['away prediction'])
	date = (predictcombined.ix[i]['Date']).strftime('%m/%d/%Y')

	miniarr = [date, predictcombined.ix[i]['home'], predictcombined.ix[i]['away'], predictcombined.ix[i]['score'], predictcombined.ix[i]['line'], prediction]
	bigdata.append(miniarr)

#print bigdata

gameinfo = {"data" : bigdata}

f = open('gameinfo.txt', 'w')
simplejson.dump(gameinfo, f)
f.close()