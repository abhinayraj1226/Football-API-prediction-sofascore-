###

# update the prediction result in prediction file status value


###


import json



def getResultFile(dateOfMatch):
    with open("result/result-API-{0}.json".format(dateOfMatch)) as jsonFile:
        data = json.load(jsonFile)
        jsonFile.close()
    return data


def getPredictionFile(dateOfMatch):
    with open("prediction/pred-API-{0}.json".format(dateOfMatch)) as jsonFile:
        data = json.load(jsonFile)
        jsonFile.close()
    return data

def checkResult(result, team, type):
    for i in result:
        if i['team'] == team:
            llist = list(i['h2h_score'].values())
            # total = llist[0] + llist[1]
            total = llist[1] + llist[2]
            if type == "OVER-0.5" and total > 0.5:
                return True
            elif type == "OVER-1.5" and total > 0.5:
                return True
            elif type == "OVER-2.5" and total > 1.5:
                return True
            elif type == "OVER-3.5" and total > 1.5:
                return True
            elif type == "UNDER-1.5" and total < 2.5:
                return True
            elif type == "UNDER-2.5" and total < 3.5:
                return True
            elif type == "UNDER-3.5" and total < 4.5:
                return True
            elif type == "UNDER-4.5" and total < 5.5:
                return True
            else:
                return False
            
            


def UpdateResult(dateOfMatch):
    data = getResultFile(dateOfMatch)
    result = data['result']

    data = getPredictionFile(dateOfMatch)

    for i in data['result']:
        type = i['type']
        for j in i['match-list']:
            team = j['team']
            if checkResult(result, team, type):
                j['status'] = True

    with open("prediction/pred-API-{0}.json".format(dateOfMatch),'w') as jsonFile:
        json.dump(data, jsonFile, indent=4)
        jsonFile.close()





def main():
    dateOfMatch = "2021-05-10"
    UpdateResult(dateOfMatch)


if __name__ == "__main__":
    main()


