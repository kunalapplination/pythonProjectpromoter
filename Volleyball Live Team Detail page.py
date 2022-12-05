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
driver.execute_script("window.scrollBy(0,3000)","")


# driver.execute_script("window.scrollTo({},{});".format(0, 2400))

driver.get("https://promoter.applination.in/regEvent/8471")


############After Team Added Event Volleyball Details shown ##############

# Mens Open 35+
# 8 / 8 teams registered, 1 teams on waitlist
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div/div[1]/div/span/img").click()
time.sleep(1)

# After click arrow down sign then click on Hambarger Icon
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div[2]/a/div/img").click()
time.sleep(1)

#### After click Hambergar icon then click for closed registration
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div[2]/a/div/span/ul/li[2]").click()
time.sleep(1)


### After Closed registration
# Reference Page of Event shown

driver.get("https://promoter.applination.in/regEvent/8471")
time.sleep(1)

# driver.get("https://promoter.applination.in/eventProfileSaved/8466")


#  After click Hambergar icon for view registration clicl
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/a/div/img").click()
# time.sleep(1)



# # click on Trophy icon for next page going
driver.find_element(By, "/html/body/div/div[2]/div[2]/div/div[1]/nav/div/div/ul[1]/li[2]").click()
time.sleep(1)
# # After click on trophy icon Next page open Event Page -> click on Hambarger icon
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/a/div/img").click()
time.sleep(1)


########## Open event profile saved page #############
driver.get("https://promoter.applination.in/eventProfileSaved/8471")

# After  > Hambarger icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/a/div/img").click()
time.sleep(1)
# Click on View Division Button
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/a/div/span/ul/li[3]").click()
time.sleep(1)

### After vie division click then go to next page ######

driver.get("https://promoter.applination.in/TemplateDivisionSavedMain/8471")

 # After View division click then -> Hambarger icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[1]/div/a/div/img").click()
time.sleep(1)

# After clicking on Generate schedule then - > click on Scores tab button
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[1]/div/a/div/span/ul/li[2]").click()
time.sleep(1)


driver.get("https://promoter.applination.in/DashboardScores")

# Scores button -> View in Recent created event click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div/div[4]/div[1]/div[1]/div").click()
time.sleep(1)



# Edit -> click on Arrow down icon
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/span/img").click()
# time.sleep(1)

driver.get("https://promoter.applination.in/scores/8471")
time.sleep(200)


# # After view in recent event click -> then go to page on scores and click on Hambarger icon for edit
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/img").click()
# time.sleep(1)
#
# # After Hambarger Icon click then -> clcik for edit in scores
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/span/ul/li").click()
# time.sleep(1)
# #############3 Scores Edit page ##############s
# driver.get("https://promoter.applination.in/scoresEdit/8466")
#
# # In score Edit page click drop down arrow ###
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/div/span/img").click()
# time.sleep(1)
#
# driver.execute_script("window.scrollTo({},{});".format(0, 3000))
#
# # click set 1
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game A 1 -> set 1 scores 5 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("5")
# time.sleep(1)
# # Game A 1 set 2
# # set 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game A 1 set 2 "6" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("6")
# time.sleep(1)
# #Game A 1 Set 3 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Set 3 send key 8
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("8")
# time.sleep(1)
#
# # Game A 1 Silve Set 1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game A 1 Silve Set 1 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("6")
# time.sleep(1)
# # Game A 1 Silve Set 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game A 1 Silve Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game A 1 click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game A 1 set 3 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("5")
# time.sleep(1)
#
# # driver.execute_script("window.scrollTo({},{});".format(0, 200))
# ################## Game B1 ############
#
# # click set 1
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game B 1 -> set 1 scores 5 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("5")
# time.sleep(1)
# # Game B 1 set 2
# # set 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game B 1 set 2 "6" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("6")
# time.sleep(1)
# #Game B 1 Set 3 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Set 3 send key 9
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("9")
# time.sleep(1)
#
# # Game B 1
# # Zook / Risser Set 1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game B 1 Zook / Risser Set 1 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("6")
# time.sleep(1)
# # Game B 1 Zook / Risser Set 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game B 1 Zook / Risser  Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game B 1 click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game A 1 set 3 send key 4
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("4")
# time.sleep(1)
#
# # driver.execute_script("window.scrollTo({},{});".format(0, 200))
#
# ########### Game A 2 ##############
# # click set 1
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game A 2 -> set 1 scores 5 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("5")
# time.sleep(1)
# # Game A 2 set 2
# # set 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game A 2 set 2 "6" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("6")
# time.sleep(1)
# #Game A 2 Set 3 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Set 3 send key 9
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("4")
# time.sleep(1)
#
# # Game A 2
# # Hutchinson / Brenes Set 1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game A 2
# # Hutchinson / Brenes Set 1 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("6")
# time.sleep(1)
# # Game A 2
# # Hutchinson / BrenesSet 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game A 2
# # Hutchinson / Brenes Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game A 2 click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game A 2 set 3 send key 4
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("4")
# time.sleep(1)
#
#
# # driver.execute_script("window.scrollTo({},{});".format(0, 200))
# ################# Game B 2 #############
#
# # Game B 2 1st
# #
# # Chaumont / Beebe  1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[4]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game B2 1st
# # Chaumont / Beebe Set 1 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[4]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("3")
# time.sleep(1)
# # Game B2 1st
# # Chaumont / Beebe 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[4]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game B2 1st
# # Chaumont / Beebe Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[4]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game B2  1st click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[4]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game B2 1st set 3 send key 4
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[4]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("4")
# time.sleep(1)
#
#
# driver.execute_script("window.scrollTo({},{});".format(0, 200))
# ############### Game B2 2nd #########
# # Game B 2 2nd
# #  Uydess / Gable 1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[4]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game B2 2nd
# # Uydess / Gable Set 1 2 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[4]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("2")
# time.sleep(1)
# # Game B2 2nd
# # Uydess / Gable 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[4]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game B2 2nd
# # Uydess / Gable Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[4]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game B2  2nd click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[4]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game B2 2nd set 3 send key 4
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[4]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("4")
# time.sleep(1)
#
#
# driver.execute_script("window.scrollTo({},{});".format(0, 200))
# ########### Game A 3 #######
# # Huzar / McLaughlin Game A3 set 1
# # Game A 3 1st
# #  Huzar / McLaughlin 1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[5]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game A3 1st
# # Huzar / McLaughlin 1 2 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[5]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("2")
# time.sleep(1)
# # Game A3 1st
# # Huzar / McLaughlin 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[5]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game A3 1st
# # Uydess / Gable Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[5]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game A3  1st click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[5]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game A3 1st set 3 send key 4
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[5]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("4")
# time.sleep(1)
#
# ############### Game A3 # 2nd ####
# # SILVA / Cassel Game A3 set 1
# # Game A 3 1st
# #  Huzar / McLaughlin 1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[5]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game A3 1st
# # Huzar / McLaughlin 1 2 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[5]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("2")
# time.sleep(1)
# # Game A3 1st
# # Huzar / McLaughlin 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[5]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game A3 1st
# # Uydess / Gable Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[5]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game A3  2nd click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[5]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game A3 1st set 3 send key 8
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[5]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("8")
# time.sleep(1)
#
# driver.execute_script("window.scrollTo({},{});".format(0, 200))
#
# ########### Game B 3 #########
# # Chaumont / Beebe Game B3 set 1
# # Game B3   1st
# # Chaumont / Beebe1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[6]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game B3 1st
# # Huzar / McLaughlin 1 2 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[6]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("2")
# time.sleep(1)
# # Game B3 1st
# # Huzar / McLaughlin 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[6]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game B3 1st
# # Uydess / Gable Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[6]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game b3  2nd click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[6]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game B3 1st set 3 send key 8
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[6]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("8")
# time.sleep(1)
#
# ############ Game B3 ##########
# # set 1 Game B 3 1st
# # Zook / Risser 1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[6]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game B3 1st
# # Huzar / McLaughlin 1 5 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[6]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("5")
# time.sleep(1)
# # Game B3 1st
# # Huzar / McLaughlin 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[6]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game B3 1st
# # Uydess / Gable Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[6]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game b3  2nd click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[6]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game B3 1st set 3 send key 8
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[6]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("8")
# time.sleep(1)
# driver.execute_script("window.scrollTo({},{});".format(0, 200))
# ############ Game A4 ########
# # set 1 Game A4 1st
# # Allred / Colafrancesco1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[7]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game A4 1st set 1
# # Allred / Colafrancesco1 5 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[7]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("5")
# time.sleep(1)
# # Game A4 1st
# # Allred / Colafrancesco 2  set 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[7]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game A4 1st
# # Uydess / Gable Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[7]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game A4  1st  click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[7]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game B3 1st set 3 send key 8
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[7]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("8")
# time.sleep(1)
#
# driver.execute_script("window.scrollTo({},{});".format(0, 200))
# ###########
# ############ Game A4 ########
# # set 1 Game A4 2nd
# # Allred / Colafrancesco 1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[7]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game A4 1st set 1
# # Allred / Colafrancesco1 5 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[7]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("5")
# time.sleep(1)
# # Game A4 1st
# # Allred / Colafrancesco 2  set 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[7]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game B3 1st
# # Uydess / Gable Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[7]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game A4  1st  click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[7]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game B3 1st set 3 send key 6
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[7]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("6")
# time.sleep(1)
#
# ################### Game B 4 ##########
# # set 1 Game B4 1st
# # Barra / Abiador 1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[8]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game B4 1st
# # Barra / Abiador 1 5 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[8]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("5")
# time.sleep(1)
# # Game B4 1st
# # Barra / Abiador 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[8]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game B4 1st
# # Uydess / Gable Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[8]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game b4  2nd click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[8]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game B4 1st set 3 send key 8
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[8]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("8")
# time.sleep(1)
#
# ########## Game B4 2nd #######
# # set 1 Game B4 2nd
# # Uydess / Gable1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[8]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game B4 1st
# # Barra / Abiador 1 4 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[8]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("4")
# time.sleep(1)
# # Game B4 1st
# # Barra / Abiador 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[8]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game B4 1st
# # Uydess / Gable Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[8]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game b4  2nd click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[8]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game B4 1st set 3 send key 8
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[8]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("8")
# time.sleep(1)
# driver.execute_script("window.scrollTo({},{});".format(0, 200))
# ############### Game A 5 #########
#
# # set 1 Game A5 1st
# # Hutchinson / Brenes1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[9]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game A5 1st
# # Hutchinson / Brenes 1 5 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[9]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("5")
# time.sleep(1)
# # Game A5 1st
# # Hutchinson / Brenes 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[9]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game A5 1st
# # Hutchinson / Brenes Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[9]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game A5  2nd click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[9]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game A5 1st set 3 send key 8
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[9]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("8")
# time.sleep(1)
#
# ########## Game A5 ####### 2nd ###
# # set 1 Game A5 1st
# # SILVA / Cassel 2nd  click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[9]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game A5 1st
# # Hutchinson / Brenes 1 5 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[9]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("5")
# time.sleep(1)
# # Game A5 1st
# # Hutchinson / Brenes 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[9]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game A5 1st
# # Hutchinson / Brenes Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[9]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game A5  2nd click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[9]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game A5 1st set 3 send key 4
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[9]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("4")
# time.sleep(1)
#
# ############## Game B 5 ###########
# # set 1 Game B5 1st
# # Barra / Abiador 1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[10]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game B5 1st
# # Barra / Abiador 1 4 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[10]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("4")
# time.sleep(1)
# # Game B5 1st
# # Barra / Abiador 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[10]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game B5 1st
# # Uydess / Gable Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[10]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game b5  2nd click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[10]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game B5 1st set 3 send key 8
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[10]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("8")
# time.sleep(1)
#
# driver.execute_script("window.scrollTo({},{});".format(0, 200))
# ############### Game B5 2nd #########
#
# # set 1 Game B5 2nd
# # Barra / Abiador 1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[10]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game B5 1st
# # Barra / Abiador 1 4 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[10]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("4")
# time.sleep(1)
# # Game B5 1st
# # Barra / Abiador 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[10]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game B5 1st
# # Uydess / Gable Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[10]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game b5  2nd click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[10]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game B5 1st set 3 send key 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[10]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("3")
# time.sleep(1)
#
# ######## Game A 6 #############
# # set 1 Game A6 1st
# # Barra / Abiador 1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[11]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game A6 1st
# # Barra / Abiador 1 4 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[11]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("4")
# time.sleep(1)
# # Game A6 1st
# # Barra / Abiador 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[11]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game A6 1st
# # Uydess / Gable Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[11]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game A6  2nd click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[11]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game A6 1st set 3 send key 8
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[11]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("8")
# time.sleep(1)
#
# ################ Game A6 2nd
# # set 1 Game A6 2nd
# # Huzar / McLaughlin 1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[11]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game A6 1st
# # Huzar / McLaughlin 1 4 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[11]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("4")
# time.sleep(1)
# # Game A6 1st
# # Huzar / McLaughlin  2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[11]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game A6 1st
# # Huzar / McLaughlin  Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[11]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game b5  2nd click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[11]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game B5 1st set 3 send key 1
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[11]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("1")
# time.sleep(1)
#
# driver.execute_script("window.scrollTo({},{});".format(0, 200))
#
# ############ Game B 6 ###########
#
# ######## Game B 6 #############
# # set 1 Game B6 1st
# # Barra / Abiador 1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[12]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game A6 1st
# # Barra / Abiador 1 4 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[12]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("4")
# time.sleep(1)
# # Game A6 1st
# # Barra / Abiador 2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[12]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game A6 1st
# # Uydess / Gable Set 2 "7" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[12]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("7")
# time.sleep(1)
# # Game A6  2nd click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[12]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game A6 1st set 3 send key 9
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[12]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("9")
# time.sleep(1)
#
# ################ Game B6 2nd###########
#
# # set 1 Game B6 2nd
# # Huzar / McLaughlin 1 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[12]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").click()
# time.sleep(1)
# # Game B6 2nd
# # Huzar / McLaughlin 1 4 send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[12]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/input").send_keys("4")
# time.sleep(1)
# # Game B6 2nd
# # Huzar / McLaughlin  2 click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[12]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").click()
# time.sleep(1)
# # Game B6 2nd
# # Huzar / McLaughlin  Set 2 "2" send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[12]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/input").send_keys("2")
# time.sleep(1)
# # Game B6  2nd click
# # set 3
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[12]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").click()
# time.sleep(1)
# # Game B6 2nd set 3 send key 1
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[12]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div[6]/div[2]/input").send_keys("1")
# time.sleep(1)
# driver.execute_script("window.scrollTo({},{});".format(0, 200))
#
#
# # Save Button click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/span").click()
# time.sleep(200)












