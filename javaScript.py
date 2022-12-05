
import time
import js2py
from js2py import require
import csv

import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="D:\\Seleinum Project\\AVP Promoter\\chromedriver.exe")


print(type(driver))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://promoter.applination.in/")

# driver.execute_script("window.scrollBy(0,2000)","")
myPageTitle = driver.title
print(myPageTitle)
# Login user id
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[1]/input").send_keys("kaushiki@applination.in")
# Password
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[2]/input").send_keys("123456")
# Login Button click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[3]").click()
time.sleep(2)

##21 Team
driver.get("https://promoter.applination.in/RegEventEdit/8403")

# driver.get("https://promoter.applination.in/RegEventEdit/8380")
# driver.get("https://promoter.applination.in/RegEventEdit/8383")

# driver.execute_script("window.scrollTo({},{});".format(0, 3500))

# Mens Open 35+ , Team 1-0  (+) icon click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div[1]/div[1]/div[2]/img").click()
# time.sleep(1)

driver.execute_script("window.scrollTo({},{});".format(0, 2000))

######### 1 st Division Mens open 35+ ##########

# Mens open 35+ -> Open after team 1-0 icon click next page -> details Mens 35_ open -> division  -> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[1]/div/span/img").click()
time.sleep(1)


# # 1 Team 2nd player + icon click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/img").click()
# time.sleep(1)

########### Commented Code #############
# ref_code1 = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[3]").text
# setattr(ref_code, 'aa')
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()

# path="/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]"
# ref_code = driver.find_element_by_xpath(path.__setattr__('//*[@id="app-content"]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]','Vishal'))
# # # ref_code.send_keys("aa")
# print (ref_code.text)
# driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("Vishal")

################## Javascript Code Running Code#####################
# driver.execute_script(open("setDomattribute.js").read())

 ########## Set value from Excel file ##############
#load dataframe from csv
# df = pd.read_csv("add_team_csv_file.csv", index_col ="Team1")
# #print dataframe
# print(df)
# print(df.index)
# first = df.ix[1]
# print(first)

# opening the CSV file
with open ( 'add_team_csv_file.csv' ,'r' ) as file:
    # reading the CSV file
    csvFile = csv.DictReader ( file )
    # csvFile = list ( csv.reader ( file , delimiter="," ) )

    team1Data = []
    team2 = []
    team3 = []
    counter = 0
    for col in csvFile:
     team1Data.append ( col['team1'] )
    # team2.append ( col['team2'] )
    # team3.append ( col['team3'] )

    print ( counter , team1Data )
    counter += 1
    for i in enumerate ( team1Data ):
      playerName1 =  i
    print ( 'playerName1' , playerName1 )
    # print ( 'team2' , team2 )
    # print ( 'team3' , team3 )


    # displaying the contents of the CSV file
    # for lines in csvFile:
    #     print ( 'team1:' , lines['team1'] )
    #     team1.append ( lines['team1'] )
    #     team2.append ( lines['team2'] )
    #     team3.append ( lines['team3'] )
    # # printing lists
    # print ( 'team1:' , team1 )
    # print ( 'team2:' , team2 )
    # print ( 'team3:' , team3 )
    # data = [tuple ( row ) for row in csvFile]
##################################################################
    # open the file in read mode
# with open ( 'add_team_csv_file.csv' , 'r' ) as file:
# csvFile = csv.DictReader ( file )
# team1 = []
# team2 = []
# team3 = []
#
# # iterating over each row and append
# # values to empty list
# for col in csvFile:
# team1.append ( col['team1'] )
# team2.append ( col['team2'] )
# team3.append ( col['team3'] )
#
# # printing lists
# print ( 'team1:' , team1 )
# print ( 'team2:' , team2 )
# print ( 'team3:' , team3 )

## For Team 1 ##########################
playerName2="Kunal"

## For Team 2 ##
playerName3="John"
playerName4="Roy"

# path="/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]"
# driver.execute_script(open("setDomattribute.js").xPathEven(path.textContent=playerName))

# eval_res, tempfile = js2py.run_file("setDomattribute.js")
# driver.execute_script(return testData(path,playerName))

# write script
script = """function xPathEvent(xpathToExecute){ var result = []; var nodesSnapshot = document.evaluate(xpathToExecute, document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null ); for ( var i=0 ; i < 
nodesSnapshot.snapshotLength; i++ ){ result.push( nodesSnapshot.snapshotItem(i) ); } return result;}  
xPathEvent("/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]")[0].textContent="""+repr(playerName1)+""" 
xPathEvent("/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[3]")[0].textContent="""+repr(playerName2)+""" 
xPathEvent("/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[3]/div[2]/div[1]/div/div[3]")[0].textContent="""+repr(playerName3)+""" 
xPathEvent("/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[3]/div[2]/div[2]/div/div[3]")[0].textContent="""+repr(playerName4)

driver.execute_script ( script)

###################################################################################################################




#####################################################################################################
# range_1 = range(0, totalTeamSize)
# list_1 = list(range_1)
# for index, val in enumerate(list_1, start=0):


###### For Loop for Plus icon click based on total team size ###
# for index in range(totalTeamSize):
#  imgAddPlayer = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div["+str(index)+"]/div/div[4]/div/div/img"
# script = """
#
# function xPathEvent(xpathToExecute){ var result = []; var nodesSnapshot = document.evaluate(xpathToExecute, document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null ); for ( var i=0 ; i <
# nodesSnapshot.snapshotLength; i++ ){ result.push( nodesSnapshot.snapshotItem(i) ); } return result;}
#
# for(let i=0;i<totalTeamSize;i++){
#
# imgAddPlayer = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[i]/div/div[4]/div/div/img"
# const fruits = driver.findElement(By.id('fruits'));
# } """


#############################################
# x. addEventListener('click', function(event) {
#      x.focus();
#       x.style.backgroundColor = "red";
# })
#
# querySelector = """
# $( document ).ready(function() {
#     console.log( "ready!" );
#  var x = document.querySelector("#points-hamburger > div > img");
#  x.addEventListener('focus', (event) => {
#    event.target.style.background = 'red';
#
# });
#
#  });
#
#   """

# driver.execute_script(querySelector)


#
# # write script
# script = """
# function xPathEvent(xpathToExecute){ var result = []; var nodesSnapshot = document.evaluate(xpathToExecute, document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null ); for ( var i=0 ; i <
# nodesSnapshot.snapshotLength; i++ ){ result.push( nodesSnapshot.snapshotItem(i) ); } return result;}
#
# let teamSize=xPathEvent("/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[1]/span/div/div[2]/div/span")[0].textContent;
# let teamSize_text = teamSize.substring(5, teamSize.indexOf("/"));
# let team_size_length = parseInt(teamSize_text.replace('/', ' '));
# let totalTeamSize=team_size_length+2;
#
# let playerCount=2;
# for(let i=0;i<totalTeamSize;i++){
# let path="/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div["+i+"]/div/div[4]/div/div/img";
# console.log('plus sign path'+i,path);
#
#
# for(let j=0;j<playerCount;j++){
# let playerPath="/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div["+j+"]/div/div[4]/div/div/span/div[1]/div[2]/input";
# console.log('playerPath'+j,playerPath);
#
#
#
#   }
#
# }
# """
# print(script);
#driver.execute_script(script)
#########################################


