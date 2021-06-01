import json



def clearJsonFile():
	res = []

	data = {
		"Status" : "Football API Prediction",
		"result" : res
	}
	with open("prediction/prediction.json",'w') as jsonFile:
		json.dump(data, jsonFile, indent=4)
	jsonFile.close()

def loadJsonData(dateOfMatch):
	with open("sofa-API/H2H-API-{0}.json".format(dateOfMatch)) as apiFile:
		data = json.load(apiFile)
		return data

def addTodayMatchPrediction(data, dateOfMatch):
	with open("prediction/prediction.json") as jsonFile:
		dtemp = json.load(jsonFile)
	jsonFile.close()


	is_find = False
	index_ofFind =-1
	if len(dtemp['result']) < 1:
		data1 = {
			dateOfMatch:[data]
		}
		dtemp['result'].append(data1)
	else:
		for i in dtemp['result']:
			if dateOfMatch in i:
				is_find = True
				index_ofFind +=1
				break

		if is_find:
			dtemp['result'][index_ofFind][dateOfMatch].append(data)
		else:
			data1 = {
				dateOfMatch:[data]
			}
			dtemp['result'].append(data1)

	

	with open("prediction/prediction.json",'w') as jsonFile:
		json.dump(dtemp, jsonFile, indent=4)
	jsonFile.close()

### over 0.5

def getPredictionOver(data):
	matchlist = data['response']
	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				total = j['home'] + j['away']

				if total > 0.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				selectedList.append(i['team'])
	return selectedList

### over 1.5

def getPredictionOver(data):
	matchlist = data['response']
	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				total = j['home'] + j['away']

				if total > 1.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				selectedList.append(i['team'])
	return selectedList


### over 2.5

def getPredictionOver(data):
	matchlist = data['response']
	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				total = j['home'] + j['away']

				if total > 2.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				selectedList.append(i['team'])
	return selectedList


### under 2.5

def getPredictionUnder(data):
	matchlist = data['response']
	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				total = j['home'] + j['away']

				if total < 2.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				selectedList.append(i['team'])
	return selectedList



### under 3.5

def getPredictionUnder(data):
	matchlist = data['response']
	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				total = j['home'] + j['away']

				if total < 3.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				selectedList.append(i['team'])
	return selectedList



def makeApiOFPrediction(dateOfMatch, selectedList, typePred):
	SelectListDict = []

	for i in selectedList:
		dt = {
			"Team" : i,
			"Status" : False
		}
		SelectListDict.append(dt)

	predDetail = {
		"Prediction Detail": typePred,
		"No of Match" : len(selectedList),
		"MatchList" : SelectListDict
	}
	

	addTodayMatchPrediction(predDetail, dateOfMatch)
	


	


def main():
	dateOfMatch = "2021-05-14"

	data = loadJsonData(dateOfMatch)
	selectedList = getPredictionOver(data)
	makeApiOFPrediction(dateOfMatch ,selectedList, "Over 1.5")

	selectedList = getPredictionUnder(data)
	makeApiOFPrediction(dateOfMatch ,selectedList, "Under 2.5")
	# clearJsonFile()

	# with open("prediction/prediction.json") as jsonFile:
	# 	dtemp = json.load(jsonFile)
	# jsonFile.close()
	# print(len(dtemp['result']))
	



if __name__ == "__main__":
	main()