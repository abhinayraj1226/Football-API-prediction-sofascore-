import json
import os

def openFile(fileName):
    with open("prediction/{0}".format(fileName)) as jsonFile:
        data = json.load(jsonFile)
        jsonFile.close()
    return data



def getFileName(path):
    fileList = []
    for path in os.listdir(path) :
        fileList.append(path)
    return fileList

def getResultStatus(fileName):
    print("\t\t##################################################################################################")
    data = openFile(fileName)

    correct = []
    total_match = []

    result = data['result']
    date = data['Date']
    print("{0}:".format(date))
    for i in result:
        count = 0
        for j in i['match-list']:
            if j['status']:
                count+=1
            # else:
                # print(j['team'])
        total_match.append(i['total-match'])
        correct.append(count)
    #     print("Range: {0}".format(i['range']))
    #     print("\tType:{0}\n".format(i['type']), end=" ")
    #     print("\t{0}%".format(percent), end= " ")
    #     print("\t{0}/{1}\n\n".format(count,total))
    # print("")
    DisplayData(correct, total_match)


def DisplayData(correct, total_match):
    for i in range(0, len(correct)):
        try:
            percent = int((correct[i]/total_match[i])*100)
        except:
            percent = 0
        print("\t{0}%".format(percent), end=" ")
    print("")
    flag = False
    for i in range(0, len(correct)):
        if flag:
            print("\t\t")
            flag = False
        print("\t{0}/{1}".format(correct[i], total_match[i]), end="")
    print("")


def main():
    pathName = "prediction/"
    fileList = getFileName(pathName)
    print("\t ALL\t ALL\t ALL\t ALL\t ALL\t ALL\t ALL\t ALL\t last-2\t last-2\t last-2\t last-2\t last-2\t last-2\t last-2\t last-2\t last-2\t")
    print("\t O-0.5\t O-1.5\t O-2.5\t O-3.5\t U-1.5\t U-2.5\t U-3.5\t U-4.5\t O-0.5\t O-1.5\t O-2.5\t O-3.5\t U-0.5\t U-1.5\t U-2.5\t U-3.5\t U-4.5\t")
    for file in fileList:
        getResultStatus(file)



if __name__ == "__main__":
    main()

