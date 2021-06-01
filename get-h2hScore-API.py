import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup



# Chrome Driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# List of match of given date
match_list = []


def clickButtonShowAllMatches():
    driver.find_element_by_xpath('//button[normalize-space()="Show all matches"]').click()

def getMatchList(dateOfMatch):
    sofa_url = "https://www.sofascore.com/football/"
    driver.get("{0}{1}".format(sofa_url,dateOfMatch))
    loadMatchList()
    time.sleep(2)
    clickButtonShowAllMatches()
    time.sleep(2)
    loadMatchList()

    
def loadMatchList():
    total_height = driver.execute_script("return document.body.scrollHeight")
    elem = driver.find_element_by_tag_name("body")
    current_height_pos = 0
    is_height_set = False

    while current_height_pos < total_height:
        if not is_height_set:
            total_height = driver.execute_script("return document.body.scrollHeight") - 800
            is_height_set = True
        current_height_pos = driver.execute_script("return window.pageYOffset")
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')
        for ele in soup.find_all('a',attrs={'class':'EventCellstyles__Link-sc-1m83enb-0 dhKVQJ'}):
            h2h_match_team = ele.get('href')
            if h2h_match_team not in  match_list:
                match_list.append(h2h_match_team)
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)


def getH2HScore(h2hid):
    # h2hid = "/alanyaspor-mke-ankaragucu/dmbsmCc"
    sofa_url_forh2h = "https://www.sofascore.com"
    no_of_pagedown  = 6
    h2h_score_list = []
    try:
        driver.get("{0}{1}".format(sofa_url_forh2h,h2hid))
    except:
      return  h2h_score_list


    elem = driver.find_element_by_tag_name("body")

    while no_of_pagedown > 0:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        no_of_pagedown-=1
    no_of_pagedown = 6

    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    head_to_head = soup.find_all('div',attrs={'class':'styles__Wrapper-c0xyrn-0 fxQxZC'})
    a_tag = head_to_head[1].find_all('a', attrs={'class' : 'EventCellstyles__Link-sc-1m83enb-0 dhKVQJ'})

    for i in range(0, len(a_tag)):
        h2h_score = a_tag[i].find_all('div', attrs={'class':'Section-sc-1a7xrsb-0 EventCellstyles__Score-ni00fg-9 gUPqAN'})
        h2h_date = a_tag[i].find_all('div', attrs={'class':'Section-sc-1a7xrsb-0 EventCellstyles__Status-ni00fg-2 dPpfDG'})
        h2h_team = a_tag[i].find_all('div', attrs={'class':'Section-sc-1a7xrsb-0 hwkKwf'})

        for i in range(0,len(h2h_date)):
            try:

                date = h2h_date[i].find_all('div')[0].text
                home_score = int(h2h_score[i].find_all('div')[0].text)
                away_score = int(h2h_score[i].find_all('div')[1].text)
                home_name = h2h_team[i].find_all('div')[0].text
                away_name = h2h_team[i].find_all('div')[1].text
            except:
                continue

            if((home_score != None and away_score !=None)):
                dct = {
                    "date" : date,
                    home_name : home_score,
                    away_name : away_score
                }
                # print(dct)
                h2h_score_list.append(dct)
            else:
                print("Null data found in {0}".format(h2hid))
    return h2h_score_list


def makeApiOfMatchList(dateOfMatch):
    getMatchList(dateOfMatch)

    total_match = len(match_list)
    print("{0} match found on {1}".format(total_match,dateOfMatch))

    index = 1
    match_list_dict = []

    for i in match_list:
        print("#{0}/{1}\n\t {2}:".format(index,total_match,i))
        h2h_score_list = getH2HScore(i) 
        temp_dict = { "team": i, "h2h_score": h2h_score_list}
        index+=1
        match_list_dict.append(temp_dict)
    driver.close()
    return match_list_dict


def generateApiFile(dateOfMatch):
    match_list_dict = makeApiOfMatchList(dateOfMatch)

    data = {
    "INFO" : "H2H SCORE API",
    "date":dateOfMatch,
    "total-match":len(match_list),
    "data": match_list_dict
    }

    with open("sofa-API/H2H-API-{0}.json".format(dateOfMatch),'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

def mainDef(dateOfMatch):
    generateApiFile(dateOfMatch)


dateOfMatch = "2021-05-10"
mainDef(dateOfMatch)


