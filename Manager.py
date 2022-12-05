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
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[1]/input").send_keys("kaushiki@applination.in")
# Password
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[2]/input").send_keys("123456")
# Login Button click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[4]/div[3]").click()
time.sleep(2)

# Manager icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/button[2]/span").click()
time.sleep(1)
# New Manager Icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div/div[1]/div/div").click()
time.sleep(1)
# First Name Jonshan send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/input").send_keys("Jonshan ")
time.sleep(1)
# last name Mark send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/input").send_keys("Mark")
time.sleep(1)
# Add Photo icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/label").click()
time.sleep(1)
# Contact
# Location zip code send key 90009
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div[2]/div[2]/div[2]/input").send_keys(90009)
time.sleep(1)
# Mobile send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div[2]/div[3]/div[2]/input").send_keys("987 456 1236")
time.sleep(1)
# email id  jonshanmark1@gmail.com send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div[2]/div[4]/div[2]/input").send_keys("jonshanmark1@gmail.com")
time.sleep(1)
# Save Button click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[3]/div/button[2]").click()
time.sleep(200)
