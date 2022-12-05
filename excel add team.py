import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(executable_path="D:\\Seleinum Project\\AVP Promoter\\chromedriver.exe")
import pandas as pds
import xlsxwriter


'''# file =("D:\pythonProjectpromoter\addteam.xlsx")
newData = pds.read_excel(file)
newData
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
driver.execute_script("window.scrollTo({},{});".format(0, 2000))

# Mens open 35+ -> Open after team 1-0 icon click next page -> details Mens 35_ open -> division  -> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[1]/div/span/img").click()
time.sleep(1)'''
# df = pd.read_excel(r'"D:\pythonProjectpromoter\addteam.xlsx')
# print(df)
import pandas as pd

df = pd.read_excel(r'"D:\pythonProjectpromoter\excelsheet.xlsx"\pythonProjectpromoter.xlsx', sheet_name='excelsheet')
print(df)