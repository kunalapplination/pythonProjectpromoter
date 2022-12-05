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
# Login user id
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[1]/input").send_keys("kaushiki@applination.in")
# Password
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[2]/input").send_keys("123456")
# Login Button click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[3]").click()
time.sleep(2)

########
# Template
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/button[9]/span").click()
time.sleep(1)
# New Teplate + click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div/div[1]/div/div").click()
time.sleep(1)
# Click Template Button
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/a/div/img").click()
time.sleep(2)
# Division Template choose and click
driver.execute_script("window.scrollTo({},{});".format(0, 200))
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/a/div/span/ul/li[3]").click()
time.sleep(2)
## Division Template choose  and Next Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/button[2]/span").click()
time.sleep(1)
# Choose Age of Bracket  icon click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div/div/a/div/img").click()
time.sleep(3)
# Choose age of bracket -> Adult click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div/div/a/div/span/ul/li[1]").click()
time.sleep(3)
# Choose age of bracket -> Adult -> Next Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[2]/button[2]/span").click()
time.sleep(3)
# Gender group(s) are needed for this Division? Male click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div/label[1]/input").click()
time.sleep(3)
# Gender group(s) are needed for this Division? Male -> Next button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[2]/button[2]/span").click()
time.sleep(1)
# What is the age range needed for this Division? open
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div/div[1]/label[1]/span[2]").click()
time.sleep(1)
# What is the age range needed for this Division? 35+ ->Next Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[2]/button[2]/span").click()
time.sleep(1)

#### 2 Skills taken
# skill level needed for this Division? Open
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div/div[1]/label[2]/input").click()
time.sleep(1)

#### 2 Skills taken

# skill level needed for this Division? A
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div/div[2]/label[1]/input").click()
time.sleep(1)
# skill level needed for this Division? Open and A -> Next button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[2]/button[2]/span").click()
time.sleep(1)
# Total no. of teams in this division icon click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div/div/a/div/img").click()
time.sleep(1)
driver.execute_script("window.scrollTo({},{});".format(0, 2000))
# Total no. of teams in this division 18Teams   click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div/div/a/div/span/ul/li[15]").click()
time.sleep(1)
# Total no. of teams in this division 18Teams -> Next Button  click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[2]/button[2]/span").click()
time.sleep(1)
# Players per team click icon
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div/div/a/div/img").click()
time.sleep(1)
# Players per team click 2v2
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div/div/a/div/span/ul/li[1]").click()
time.sleep(1)
# Players per team click 2v2 -> Next Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[2]/button[2]/span").click()
time.sleep(1)
# Discount Section Next button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[3]/button[2]/span").click()
time.sleep(1)
# Will these Divisions need an Early Bird entry? No click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div/label[2]/input").click()
time.sleep(1)
# Will these Divisions need an Early Bird entry? No -> Next Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[2]/button[2]/span").click()
time.sleep(1)
# Normal Entry Send keys $700
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div/div[1]/input").send_keys("$700")
time.sleep(3)
# Normal Entry Send keys Click Next Button
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[2]/button[2]/span").click()
time.sleep(2)
# Late Entry $900 send keys
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div/div[1]/input").send_keys("$900")
time.sleep(3)
# Late Entry $900 Next Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[2]/button[2]/span").click()
time.sleep(1)
# Division Template Name click 24Teams35+Open Skill A
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/label/input").click()
time.sleep(1)
# Division Template Name  18TeamsOpen Open Skill A  send key
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/label/input").send_keys("18TeamsOpenSkill open A")
time.sleep(3)
# # Division Template Name  18Teams35+Open Skill A -> save button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div/button").click()
time.sleep(200)
# After save go to edit division section click hambergar icon click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[1]/div/a/div/img").click()
# time.sleep(1)
# After  hambergar icon click then edit opetion click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[1]/div/a/div/span/ul/li[1]").click()
# time.sleep(1)
# Go to edit in age range click option
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[5]/div[4]/label[1]/input").click()
# time.sleep(1)
# Go to edit in age range Save  Button click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/span").click()
# time.sleep(200)



