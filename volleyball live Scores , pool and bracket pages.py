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
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[1]/input").send_keys("kaushiki@applination.in")
# Password
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[2]/input").send_keys("123456")
# Login Button click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[3]").click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,2000)","")


# ##### After score entered forward next page Scores details ######
driver.get("https://promoter.applination.in/scoresEdit/8466")
# click on Save button for next in score sheet
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/span").click()
time.sleep(1)
########## Next Page go score page ###########
driver.get("https://promoter.applination.in/scores/8466")

# After scores details find -> Next page Pool Page
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]").click()
time.sleep(1)

# Pool checked then click Initiate bracket
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div/div/div").click()
time.sleep(1)

#####
driver.get("https://promoter.applination.in/bracketDivisionEdit/8466")

#### Mens Open 35+ click Down icon
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/div/span/img").click()
time.sleep(1)

#### click on Generate Bracket Button ######
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/span").click()
time.sleep(1)
# The bracket may have already been initiated Do you want to continue? click on Yes continue Button
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/button[2]").click()
time.sleep(200)