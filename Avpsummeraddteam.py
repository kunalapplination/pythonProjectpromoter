import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="D:\\Seleinum Project\\AVP Promoter\\chromedriver.exe")

print(type(driver))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://promoter.applination.in/")

myPageTitle = driver.title
print(myPageTitle)

# Login user id
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[1]/input").send_keys("karishma@applination.in")
# Password
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[2]/input").send_keys("123456")
# Login Button click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[3]").click()
time.sleep(1)
# driver.execute_script("window.scrollBy(0,3000)","")


driver.execute_script("window.scrollTo({},{});".format(0, 1500))

driver.get("https://promoter.applination.in/RegEventEdit/8473")

# Add team with Player  icon click details
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[1]/div/span/img").click()
time.sleep(1)

#### Hambergar icon click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[1]/div/div/img").click()
# time.sleep(1)

#########################################
# path="/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]"
# print(path)
# driver.find_element(By.XPATH, finalPath).click()
# path="/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/img"
# driver.find_element(By.XPATH, path).click()

# path="#points-hamburger > div > img"
# driver.findElement(By.cssSelector(path[0]));
#app-content > div > div:nth-child(3) > div.container.regEventEdit.text-center.px-md-5.false > div > div > div > div.ant-collapse.ant-collapse-icon-position-end.ant-collapse-ghost.w-100.text-left > div > div.ant-collapse-header > div > span > img

# path="#points-hamburger > div > img"
# driver.find_element_by_css_selector(path)[1].click()
# time.sleep(1)
driver.execute_script("window.scrollTo({},{});".format(0, 200))
# + icon click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]").click()
# time.sleep(200)
# driver.execute_script("window.scrollTo({},{});".format(0, 200))

# write script
playerCount=2
bufferTeam=2
##### All XPATH ###################
##### Team 1 --> Player 1 ####
addInputPath = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[{}]/div/div[4]"
addInputPathClick = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]/input"
setInputValue = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]/input"
setInputValueClick = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]"
invoicePath = "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input"
okClickButtOnPath = "/html/body/div[2]/div/div[2]/div/div[3]/div/button[{}]/span"

######### Team 1 --> Player 2 ####
addPlayer1InputPath = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[{}]/div/div[4]/div/div/img"
addInputPathClick = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]/input"
addInputPathSetValue = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]/input"
addPlayer1InputSetInputValueClick = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]"
crossPlayer1click = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[{}]/div/div[4]"



#########################################

##### Team 2 --> Player 1 ####
addInputTeam2Player1Path = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[{}]/div[2]/div[{}]/div/div[4]"
deletePlayer2No = "/html/body/div[3]/div/div[2]/div/div/div[2]/div/div[1]"

addInputTeam2Player1PathClick = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[{}]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]/input"
setInputTeam2Player1Value     = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[{}]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]/input"

setInputTeam2Player1ValueClick = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[{}]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]"
invoiceTeam2Player1Path = "/html/body/div[2]/div/div[2]/div/div[{}]/div/div[{}]/label/input"
okClickTeam2Player1ButtOnPath = "/html/body/div[2]/div/div[2]/div/div[{}]/div/button[{}]/span"

##### Team 2 --> Player 2 ####

addInputTeam2Player2Path = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[{}]/div[{}]/div[{}]/div/div[4]"
deleteTeam2Player2No = "/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[1]"

addInputTeam2Player2PathClick = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[{}]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]/input"
setInputTeam2Player2Value     = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[{}]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]/input"
setInputTeam2Player2ValueClick = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[{}]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]"
########################Team 3 1st Player######################################
'''##### Team 3 --> Player 1 ####
addInputTeam2Player1Path = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[{}]/div[2]/div[{}]/div/div[4]"
deletePlayer2No = "/html/body/div[3]/div/div[2]/div/div/div[2]/div/div[1]"

addInputTeam2Player1PathClick = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[{}]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]/input"
setInputTeam2Player1Value     = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[{}]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]/input"

setInputTeam2Player1ValueClick = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[{}]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]"
invoiceTeam2Player1Path = "/html/body/div[2]/div/div[2]/div/div[{}]/div/div[{}]/label/input"
okClickTeam2Player1ButtOnPath = "/html/body/div[2]/div/div[2]/div/div[{}]/div/button[{}]/span"

##### Team 3 --> Player 2 #################

addInputTeam2Player2Path = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[{}]/div[{}]/div[{}]/div/div[4]"
deleteTeam2Player2No = "/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[1]"

addInputTeam2Player2PathClick = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[{}]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]/input"
setInputTeam2Player2Value     = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[{}]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]/input"
setInputTeam2Player2ValueClick = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[{}]/div[2]/div[{}]/div/div[4]/div/div/span/div[{}]/div[2]"

##########################################################################'''
########### End ###############
teamSize = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[1]/span/div/div[2]/div/span").text
totalTeamSize =   int(teamSize[4]) + int(bufferTeam)
for playerCount in range(totalTeamSize):
    playerCount=playerCount+1

#### Add Player for 1st Team  Player 1 ###
# for playerCount in range (playerCount):
#     playerCount=playerCount+1

    driver.find_element ( By.XPATH , addInputPath.format ( playerCount ) ).click ()
    driver.find_element ( By.XPATH , addInputPathClick.format ( playerCount , playerCount ) ).click ()
    driver.find_element ( By.XPATH , setInputValue.format ( playerCount , playerCount ) ).send_keys ( "a" )
    driver.find_element ( By.XPATH , setInputValueClick.format ( playerCount , playerCount + 1 ) ).click ()
    ## Open box with no option invoice generate Select No option from Dialog box
    ### Do you wish to generate the invoice for the team? -> No click
    driver.find_element ( By.XPATH , invoicePath.format ( playerCount+2 ) ).click ()
    ### Do you wish to generate the invoice for the team? -> No -> Ok button  click
    driver.find_element ( By.XPATH , okClickButtOnPath.format ( playerCount + 1 ) ).click ()
    time.sleep ( 7 ) #10

    ########## Team 2 .....> Player 2 ######################
    driver.find_element ( By.XPATH , addPlayer1InputPath.format ( playerCount+1 ) ).click ()
    time.sleep ( 2 ) # 5
    driver.find_element ( By.XPATH , addInputPathClick.format ( playerCount+1 , playerCount ) ).click ()
    driver.find_element ( By.XPATH , addInputPathSetValue.format ( playerCount + 1 , playerCount ) ).send_keys ( "a" )
    driver.find_element ( By.XPATH , addPlayer1InputSetInputValueClick.format ( playerCount+1, playerCount + 1 ) ).click ()
    # driver.find_element ( By.XPATH , crossPlayer1click ).format ( playerCount+1).click ()
    # time.sleep (1)
    # driver.find_element ( By.XPATH , deletePlayer2No ).format ( playerCount ).click ()
    time.sleep ( 7 )

    ############ Team 2 Player 1 ########################

    driver.find_element ( By.XPATH , addInputTeam2Player1Path.format ( playerCount+2,playerCount ) ).click ()
    time.sleep ( 1 )
    # driver.find_element ( By.XPATH , deleteTeam2Player2No ).click ()
    # time.sleep ( 1 )
    driver.find_element ( By.XPATH , addInputTeam2Player1PathClick.format( playerCount+2 , playerCount,playerCount ) ).click ()
    time.sleep ( 1 )
    driver.find_element ( By.XPATH , setInputTeam2Player1Value.format( playerCount+2 , playerCount,playerCount ) ).send_keys ( "a" )
    time.sleep ( 2 )

    driver.find_element ( By.XPATH , setInputTeam2Player1ValueClick.format( playerCount+2 , playerCount, playerCount+1 ) ).click ()
    ## Open box with no option invoice generate Select No option from Dialog box
    ### Do you wish to generate the invoice for the team? -> No click
    driver.find_element ( By.XPATH , invoiceTeam2Player1Path.format ( playerCount + 1,playerCount + 2 ) ).click ()
    ### Do you wish to generate the invoice for the team? -> No -> Ok button  click
    driver.find_element ( By.XPATH , okClickTeam2Player1ButtOnPath.format ( playerCount + 2,playerCount + 1 ) ).click ()
    time.sleep ( 7 )  # 10

    ############ Team 2 Player 2 ########################
    driver.find_element ( By.XPATH , addInputTeam2Player2Path.format ( playerCount + 2, playerCount + 1, playerCount + 1 ) ).click ()
    time.sleep ( 3 )
    # driver.find_element ( By.XPATH , deleteTeam2Player2No ).click ()
    # time.sleep ( 2 )
    driver.find_element ( By.XPATH , addInputTeam2Player2PathClick.format ( playerCount + 2,playerCount + 1 , playerCount ) ).click ()
    time.sleep ( 2 )
    driver.find_element ( By.XPATH , setInputTeam2Player2Value.format ( playerCount + 2,playerCount + 1 , playerCount ) ).send_keys ( "a" )
    time.sleep ( 2 )
    driver.find_element ( By.XPATH , setInputTeam2Player2ValueClick.format ( playerCount + 2,playerCount + 1 , playerCount + 1 ) ).click ()
    time.sleep ( 7 )
    '''########################### Team 3 ###############
    
    ############ Team 3 Player 1 ########################

    driver.find_element ( By.XPATH , addInputTeam2Player1Path.format ( playerCount + 2 , playerCount ) ).click ()
    time.sleep ( 1 )
    # driver.find_element ( By.XPATH , deleteTeam2Player2No ).click ()
    # time.sleep ( 1 )
    driver.find_element ( By.XPATH , addInputTeam2Player1PathClick.format ( playerCount + 2 , playerCount , playerCount ) ).click ()
    time.sleep ( 1 )
    driver.find_element ( By.XPATH , setInputTeam2Player1Value.format ( playerCount + 2 , playerCount , playerCount ) ).send_keys ( "a" )
    time.sleep ( 2 )

    driver.find_element ( By.XPATH , setInputTeam2Player1ValueClick.format ( playerCount + 2 , playerCount , playerCount + 1 ) ).click ()
    ## Open box with no option invoice generate Select No option from Dialog box
    ### Do you wish to generate the invoice for the team? -> No click
    driver.find_element ( By.XPATH , invoiceTeam2Player1Path.format ( playerCount + 1 , playerCount + 2 ) ).click ()
    ### Do you wish to generate the invoice for the team? -> No -> Ok button  click
    driver.find_element ( By.XPATH , okClickTeam2Player1ButtOnPath.format ( playerCount + 2 , playerCount + 1 ) ).click ()
    time.sleep ( 7 )  # 10

    ############ Team 3 Player 2 ########################
    driver.find_element ( By.XPATH , addInputTeam2Player2Path.format ( playerCount + 2 , playerCount + 1 , playerCount + 1 ) ).click ()
    time.sleep ( 3 )
    # driver.find_element ( By.XPATH , deleteTeam2Player2No ).click ()
    # time.sleep ( 2 )
    driver.find_element ( By.XPATH , addInputTeam2Player2PathClick.format ( playerCount + 2 , playerCount + 1 , playerCount ) ).click ()
    time.sleep ( 2 )
    driver.find_element ( By.XPATH , setInputTeam2Player2Value.format ( playerCount + 2 , playerCount + 1 , playerCount ) ).send_keys ( "a" )
    time.sleep ( 2 )
    driver.find_element ( By.XPATH , setInputTeam2Player2ValueClick.format ( playerCount + 2 , playerCount + 1 , playerCount + 1 ) ).click ()
    time.sleep ( 7 )'''