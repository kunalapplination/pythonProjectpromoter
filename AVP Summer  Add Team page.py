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
time.sleep(2)
# driver.execute_script("window.scrollBy(0,3000)","")


driver.execute_script("window.scrollTo({},{});".format(0, 4000))

driver.get("https://promoter.applination.in/RegEventEdit/8473")
# Add team with Player  icon click details
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[1]/div/span/img").click()
time.sleep(2)

#########################################
path="/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]"
print(path)
# driver.find_element(By.XPATH, finalPath).click()
driver.find_element_by_xpath(path).click()
time.sleep(200)


# write script
# playerCount=2
# bufferTeam=2
# teamSize = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[1]/span/div/div[2]/div/span").text
# totalTeamSize =   int(teamSize[4]) + int(bufferTeam)
# for index in range(totalTeamSize):
#     index=index+1
#     addPath = "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[{}]/div/div[4]/div/div/img".format(index)
#     print(addPath)
#     driver.find_element(By.XPATH, addPath).click()
#     time.sleep(50)
    ##### Add Player for 1st Team ###
# for playerCount in range (playerCount):
#     playerCount=playerCount+1
#     inputPath= "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[{}]/div/div[4]/div/div/span/div[1]/div[2]/input".format(playerCount)
#     print(inputPath)
#     driver.find_element(By.XPATH, inputPath).click()
#     time.sleep(1)
