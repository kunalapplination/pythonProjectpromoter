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

# driver.execute_script("window.scrollBy(0,2000)","")
myPageTitle = driver.title
print(myPageTitle)
# Login user id
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[1]/input").send_keys("karishma@applination.in")
# Password
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[2]/input").send_keys("123456")
# Login Button click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[3]").click()
time.sleep(2)

###### 8Team3Pool3Court
# Template
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/button[9]/span").click()
time.sleep(1)
# New Teplate + click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div/div[1]/div/div").click()
time.sleep(1)
# Click Template Button
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/a/div/img").click()
time.sleep(2)
# Pools Template choose click
driver.execute_script("window.scrollTo({},{});".format(0, 200))
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/a/div/span/ul/li[2]").click()
time.sleep(1)
# Pools Template choose  Next Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/button[2]/span").click()
time.sleep(1)
# Choose Number of Teams click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div/div/a/div/img").click()
time.sleep(3)
# Choose Number of Teams in pool 8 teams click
driver.execute_script("window.scrollTo({},{});".format(0, 200))
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div/div/a/div/span/ul/li[7]").click()
time.sleep(2)
# Choose Number of Teams  Next Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/form/div[2]/button[2]/span").click()
time.sleep(1)
# No. of Pools icon  click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div/div/a/div/img").click()
time.sleep(1)
# No. of Pools  select 2  pools click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div/div/a/div/span/ul/li[1]").click()
time.sleep(1)
# no. of Pools Next Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/form/div[2]/button[2]/span").click()
time.sleep(1)
# Number  of  Courts icon click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div/div/a/div/img").click()
time.sleep(1)
# Number of 2 Courts click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div/div/a/div/span/ul/li[1]").click()
# Number of 2  Courts  Next Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/form/div[2]/button[2]/span").click()
time.sleep(1)
# Template Name click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div/label/input").click()
time.sleep(1)
# Template Name 8Teams2Pool2 Court send key
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div/label/input").send_keys("8Team2pool2court AVP")
time.sleep(1)
# Template Name 8Teams2Pool2 Court save click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div/button").click()
time.sleep(1)
# Template Page open click to save button
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div").click()
time.sleep(200)

