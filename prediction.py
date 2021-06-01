import json

def loadJsonData(dateOfMatch):
	with open("sofa-API/H2H-API-{0}.json".format(dateOfMatch)) as apiFile:
		data = json.load(apiFile)
		apiFile.close()
	return data

### Prediction OVER 0.5
def PredOver0(data):
	matchlist = data['result']

	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				h2hlist = list(j.values()) 
				total = h2hlist[1]+h2hlist[2]

				if total > 0.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				tdata = {
					"team" : i['team'],
					"status" : False
				}
				selectedList.append(tdata)
	data = {
	"type" : "OVER-0.5",
	"range" : "ALL",
	"total-match" : len(selectedList),
	"match-list" : selectedList
	}
	return data


### Prediction OVER 1.5
def PredOver1(data):
	matchlist = data['result']

	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				h2hlist = list(j.values()) 
				total = h2hlist[1]+h2hlist[2]

				if total > 1.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				tdata = {
					"team" : i['team'],
					"status" : False
				}
				selectedList.append(tdata)
	data = {
	"type" : "OVER-1.5",
	"range" : "ALL",
	"total-match" : len(selectedList),
	"match-list" : selectedList
	}
	return data

### Prediction OVER 2.5
def PredOver2(data):
	matchlist = data['result']

	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				h2hlist = list(j.values()) 
				total = h2hlist[1]+h2hlist[2]

				if total > 2.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				tdata = {
					"team" : i['team'],
					"status" : False
				}
				selectedList.append(tdata)
	data = {
	"type" : "OVER-2.5",
	"range" : "ALL",
	"total-match" : len(selectedList),
	"match-list" : selectedList
	}
	return data

### Prediction OVER 3.5
def PredOver3(data):
	matchlist = data['result']

	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				h2hlist = list(j.values()) 
				total = h2hlist[1]+h2hlist[2]

				if total > 3.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				tdata = {
					"team" : i['team'],
					"status" : False
				}
				selectedList.append(tdata)
	data = {
	"type" : "OVER-3.5",
	"range" : "ALL",
	"total-match" : len(selectedList),
	"match-list" : selectedList
	}
	return data



### UNDER 1.5

def PredUnder1(data):
	matchlist = data['result']

	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				h2hlist = list(j.values()) 
				total = h2hlist[1] + h2hlist[2]

				if total < 1.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				tdata = {
					"team" : i['team'],
					"status" : False
				}
				selectedList.append(tdata)
				
	data = {
	"type" : "UNDER-1.5",
	"range" : "ALL",
	"total-match" : len(selectedList),
	"match-list" : selectedList
	}
	return data

### UNDER 2.5

def PredUnder2(data):
	matchlist = data['result']

	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				h2hlist = list(j.values()) 
				total = h2hlist[1] + h2hlist[2]

				if total < 2.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				tdata = {
					"team" : i['team'],
					"status" : False
				}
				selectedList.append(tdata)
				
	data = {
	"type" : "UNDER-2.5",
	"range" : "ALL",
	"total-match" : len(selectedList),
	"match-list" : selectedList
	}
	return data

	### UNDER 3.5

def PredUnder3(data):
	matchlist = data['result']

	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				h2hlist = list(j.values()) 
				total = h2hlist[1] + h2hlist[2]

				if total < 3.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				tdata = {
					"team" : i['team'],
					"status" : False
				}
				selectedList.append(tdata)
				
	data = {
	"type" : "UNDER-3.5",
	"range" : "ALL",
	"total-match" : len(selectedList),
	"match-list" : selectedList
	}
	return data

### UNDER 4.5

def PredUnder4(data):
	matchlist = data['result']

	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				h2hlist = list(j.values()) 
				total = h2hlist[1] + h2hlist[2]

				if total < 4.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				tdata = {
					"team" : i['team'],
					"status" : False
				}
				selectedList.append(tdata)
				
	data = {
	"type" : "UNDER-4.5",
	"range" : "ALL",
	"total-match" : len(selectedList),
	"match-list" : selectedList
	}
	return data



### Prediction OVER 0.5 from last 2 match Recent

def PredOver0Recent(data):
	matchlist = data['result']

	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				h2hlist1 = list(i['h2h_score'][0].values())
				h2hlist2 = list(i['h2h_score'][1].values())
				total1 = h2hlist1[1] + h2hlist1[2]
				total2 = h2hlist2[1] + h2hlist2[2]

				if total1 > 0.5 and total2 > 0.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				tdata = {
					"team" : i['team'],
					"status" : False
				}
				selectedList.append(tdata)
				
	data = {
	"type" : "OVER-0.5",
	"range" : "last-2",
	"total-match" : len(selectedList),
	"match-list" : selectedList
	}
	return data

### Prediction OVER 1.5 from last 2 match Recent

def PredOver1Recent(data):
	matchlist = data['result']

	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				h2hlist1 = list(i['h2h_score'][0].values())
				h2hlist2 = list(i['h2h_score'][1].values())
				total1 = h2hlist1[1] + h2hlist1[2]
				total2 = h2hlist2[1] + h2hlist2[2]

				if total1 > 1.5 and total2 > 1.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				tdata = {
					"team" : i['team'],
					"status" : False
				}
				selectedList.append(tdata)
				
	data = {
	"type" : "OVER-1.5",
	"range" : "last-2",
	"total-match" : len(selectedList),
	"match-list" : selectedList
	}
	return data

### Prediction OVER 2.5 from last 2 match Recent

def PredOver2Recent(data):
	matchlist = data['result']

	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				h2hlist1 = list(i['h2h_score'][0].values())
				h2hlist2 = list(i['h2h_score'][1].values())
				total1 = h2hlist1[1] + h2hlist1[2]
				total2 = h2hlist2[1] + h2hlist2[2]

				if total1 > 2.5 and total2 > 2.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				tdata = {
					"team" : i['team'],
					"status" : False
				}
				selectedList.append(tdata)
				
	data = {
	"type" : "OVER-2.5",
	"range" : "last-2",
	"total-match" : len(selectedList),
	"match-list" : selectedList
	}
	return data

### Prediction OVER 3.5 from last 2 match Recent

def PredOver3Recent(data):
	matchlist = data['result']

	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				h2hlist1 = list(i['h2h_score'][0].values())
				h2hlist2 = list(i['h2h_score'][1].values())
				total1 = h2hlist1[1] + h2hlist1[2]
				total2 = h2hlist2[1] + h2hlist2[2]

				if total1 > 3.5 and total2 > 3.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				tdata = {
					"team" : i['team'],
					"status" : False
				}
				selectedList.append(tdata)
				
	data = {
	"type" : "OVER-3.5",
	"range" : "last-2",
	"total-match" : len(selectedList),
	"match-list" : selectedList
	}
	return data

### Prediction UNDER 0.5 from last 2 match Recent

def PredUnder0Recent(data):
	matchlist = data['result']

	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				h2hlist1 = list(i['h2h_score'][0].values())
				h2hlist2 = list(i['h2h_score'][1].values())
				total1 = h2hlist1[1] + h2hlist1[2]
				total2 = h2hlist2[1] + h2hlist2[2]

				if total1 < 0.5 and total2 < 0.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				tdata = {
					"team" : i['team'],
					"status" : False
				}
				selectedList.append(tdata)
				
	data = {
	"type" : "UNDER-0.5",
	"range" : "last-2",
	"total-match" : len(selectedList),
	"match-list" : selectedList
	}
	return data

### Prediction UNDER 1.5 from last 2 match Recent

def PredUnder1Recent(data):
	matchlist = data['result']

	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				h2hlist1 = list(i['h2h_score'][0].values())
				h2hlist2 = list(i['h2h_score'][1].values())
				total1 = h2hlist1[1] + h2hlist1[2]
				total2 = h2hlist2[1] + h2hlist2[2]

				if total1 < 1.5 and total2 < 1.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				tdata = {
					"team" : i['team'],
					"status" : False
				}
				selectedList.append(tdata)
				
	data = {
	"type" : "UNDER-1.5",
	"range" : "last-2",
	"total-match" : len(selectedList),
	"match-list" : selectedList
	}
	return data


### Prediction UNDER 2.5 from last 2 match Recent

def PredUnder2Recent(data):
	matchlist = data['result']

	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				h2hlist1 = list(i['h2h_score'][0].values())
				h2hlist2 = list(i['h2h_score'][1].values())
				total1 = h2hlist1[1] + h2hlist1[2]
				total2 = h2hlist2[1] + h2hlist2[2]

				if total1 < 2.5 and total2 < 2.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				tdata = {
					"team" : i['team'],
					"status" : False
				}
				selectedList.append(tdata)
				
	data = {
	"type" : "UNDER-2.5",
	"range" : "last-2",
	"total-match" : len(selectedList),
	"match-list" : selectedList
	}
	return data


### Prediction UNDER 3.5 from last 2 match Recent

def PredUnder3Recent(data):
	matchlist = data['result']

	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				h2hlist1 = list(i['h2h_score'][0].values())
				h2hlist2 = list(i['h2h_score'][1].values())
				total1 = h2hlist1[1] + h2hlist1[2]
				total2 = h2hlist2[1] + h2hlist2[2]

				if total1 < 3.5 and total2 < 3.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				tdata = {
					"team" : i['team'],
					"status" : False
				}
				selectedList.append(tdata)
				
	data = {
	"type" : "UNDER-3.5",
	"range" : "last-2",
	"total-match" : len(selectedList),
	"match-list" : selectedList
	}
	return data

### Prediction UNDER 4.5 from last 2 match Recent

def PredUnder4Recent(data):
	matchlist = data['result']

	selectedList = []

	for i in matchlist:
		if len(i['h2h_score']) > 2:
			flag = False
			for j in i['h2h_score']:
				h2hlist1 = list(i['h2h_score'][0].values())
				h2hlist2 = list(i['h2h_score'][1].values())
				total1 = h2hlist1[1] + h2hlist1[2]
				total2 = h2hlist2[1] + h2hlist2[2]

				if total1 < 4.5 and total2 < 4.5:
					flag = True
				else:
					flag = False
					break
			if flag:
				tdata = {
					"team" : i['team'],
					"status" : False
				}
				selectedList.append(tdata)
				
	data = {
	"type" : "UNDER-4.5",
	"range" : "last-2",
	"total-match" : len(selectedList),
	"match-list" : selectedList
	}
	return data




def makeAPIFile(dateOfMatch, pred):
	data = {
		"INFO" : "Football API prediction",
		"Date" : dateOfMatch,
		"result" : pred
	}
	with open("prediction/pred-API-{0}.json".format(dateOfMatch), 'w') as jsonFile:
		json.dump(data, jsonFile, indent=4)
		jsonFile.close()

def main(dateOfMatch):
	
	data = loadJsonData(date)

	predO0  = PredOver0(data)
	predO1  = PredOver1(data)
	predO2  = PredOver2(data)
	predO3  = PredOver3(data)


	predU1  = PredUnder1(data)
	predU2  = PredUnder2(data)
	predU3  = PredUnder3(data)
	predU4  = PredUnder4(data)

	predO0R = PredOver0Recent(data)
	predO1R = PredOver1Recent(data)
	predO2R = PredOver2Recent(data)
	predO3R = PredOver3Recent(data)

	predU0R = PredUnder0Recent(data)
	predU1R = PredUnder1Recent(data)
	predU2R = PredUnder2Recent(data)
	predU3R = PredUnder3Recent(data)
	predU4R = PredUnder4Recent(data)

	predData = [ predO0, predO1, predO2, predO3,
				 predU1, predU2, predU3, predU4,
				 predO0R, predO1R, predO2R, predO3R,
				 predU0R, predU1R, predU2R, predU3R, predU4R
	]
	makeAPIFile(dateOfMatch, predData)




if __name__ == "__main__":
	date = "2021-05-15"
	main(date)