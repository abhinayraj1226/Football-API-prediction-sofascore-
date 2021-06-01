###
#INFO
# seprate the API of h2h score and result


###


import json

def openJsonFile(dateOfMatch):
    with open("sofa-API/H2H-API-{0}.json".format(dateOfMatch)) as jsonFile:
        data = json.load(jsonFile)

    return data

def makeApiFile(date,result):
    data = {
        "Date" : date,
        "Total Match": len(result),
        "result" : result

    }
    with open("sofa-API/H2H-API-{0}.json".format(date),'w') as jsonFile:
        json.dump(data, jsonFile, indent=4)
    jsonFile.close()


def makeResultApi(date, result):
    data = {
        "Date" : date,
        "Total Match" : len(result),
        "result" : result
    }
    with open("result/result-API-{0}.json".format(date), 'w') as jsonFile:
        json.dump(data, jsonFile, indent=4)
    jsonFile.close()


def makeSeprateAPI_Result(dateOfMatch ,mDate):
    data = openJsonFile(dateOfMatch)
    date = data['date']
    total_match = data['total_match']

    pred_result = []
    h2h_score_api = []


    for i in data['response']:
        team = i['team']
        if len(i['h2h_score']) > 1:
            for j in i['h2h_score']:
                if mDate == j['Date']:
                    result = {
                        "team" : team,
                        "h2h_score" : j
                    }
                    pred_result.append(result)
                score = i['h2h_score']
                score.remove(j)
                data = {
                    "team" : team,
                    "h2h_score" : score
                }
                h2h_score_api.append(data)
                break

    makeApiFile(date, h2h_score_api)
    makeResultApi(date, pred_result)

    

    
def main():
    dateOfMatch = "2021-05-11"
    mdate = "11/05/21"
    makeSeprateAPI_Result(dateOfMatch,mdate)

if __name__ == "__main__":
    main()