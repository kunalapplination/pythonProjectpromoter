import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="D:\Seleinum Project\AVP Promoter\\chromedriver.exe")

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


driver.execute_script("window.scrollTo({},{});".format(0, 2400))

driver.get("https://promoter.applination.in/RegEventEdit/8466")


# Add team with Player  icon click details
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[1]/div/span/img").click()
time.sleep(2)


 ###Add Team ####

# # 1 Team 1 player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# # 1Team 1 Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
# time.sleep(1)

# # 1Team 1 Player search "a" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("a")
time.sleep(1)
# # 1Team 1 Player search "a" option -> Richard Abiador, Bothell, WA -> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[2]/div[2]").click()
time.sleep(1)
# # Donation
# # Flood 40 click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[3]/label/input").click()
# time.sleep(1)
## Flood 40 -> Next button click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
# time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No -> Ok button  click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
time.sleep(1)


# # 1st Team 2nd player

# 1 Team 2nd player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div/img").click()
time.sleep(1)
# 1Team 2nd Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 1Team 2nd Player search "b" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("b")
time.sleep(1)
# 1Team 2nd Player search "b" option -> Joe Barra, Eatontown, NJ -> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div/span/div[2]/div[2]").click()
time.sleep(1)


#####2nd Team 1st player
# 2nd Team 1 player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# # 2nd Team 1 Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# # 2nd Team 1 Player search "c" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("a")
time.sleep(1)
# # 2nd Team 1 Player search "c" option -> Colin  Beebe, Chevy Chase, MD-> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/span/div[2]/div[2]").click()
time.sleep(1)
# # Donation
# # Flood 50 click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[2]/label/input").click()
# time.sleep(1)
# # Flood 50 -> Next button click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[5]/div/button[2]/span").click()
# time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No -> Ok button  click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
time.sleep(1)

# # 2nd Team 2nd player

# 2nd Team 2nd player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/img").click()
time.sleep(1)
# 1Team 2nd Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 1Team 2nd Player search "d" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("d")
time.sleep(1)
# 1Team 2nd Player search "d" option -> Darren Chaumont, Lake Charles, LA -> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/span/div[4]/div[2]").click()
time.sleep(1)


########## Team 3 1st Player ###########

# 3rd Team 1 player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# # 3rd Team 1 Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# # 3rd Team 1 Player search "c" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("a")
time.sleep(1)
# # 3rd Team 1 Player search "c" option -> Greg Cassel, Harrisburg, PA-> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[4]/div/div/span/div[3]/div[2]").click()
time.sleep(1)
# # Donation
# # Flood 50 click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[2]/label/input").click()
# time.sleep(1)
# # Flood 50 -> Next button click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[5]/div/button[2]/span").click()
# time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No -> Ok button  click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
time.sleep(1)


### 3rd Team 2nd Player ########

# 3rd Team 2nd player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[4]/div[2]/div[2]/div/div[4]/div/div/img").click()
time.sleep(1)
# 3rd Team 2nd Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[4]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 3rd Team 2nd Player search "d" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[4]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("d")
time.sleep(1)
# 3rd Team 2nd Player search "d" option -> DAVID SILVA, Long Island City, NY-> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[4]/div[2]/div[2]/div/div[4]/div/div/span/div[7]/div[2]").click()
time.sleep(1)

#######Team 4th 1st Player #############

# 4th Team 1 player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# # 4th Team 1 Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# # 4th Team 1 Player search "c" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("a")
time.sleep(1)
# # 4th Team 1 Player search "c" option -> Chris Gable, Toms River, NJ-> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div[1]/div/div[4]/div/div/span/div[4]/div[2]").click()
time.sleep(1)
# # Donation
# # Flood 50 click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[2]/label/input").click()
# time.sleep(1)
# # Flood 50 -> Next button click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[5]/div/button[2]/span").click()
# time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No -> Ok button  click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
time.sleep(1)

### 4th Team 2nd Player ########

# 4th Team 2nd player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div[2]/div/div[4]/div/div/img").click()
time.sleep(1)
# 4th Team 2nd Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 4th Team 2nd Player search "d" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("d")
time.sleep(1)
# 4th Team 2nd Player search "d" option -> Joe Uydess, St Louis, MO -> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div[2]/div/div[4]/div/div/span/div[7]/div[2]").click()
time.sleep(1)

##############5th Team ################
#######Team 5th 1st Player #############

# 5th Team 1 player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[6]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# # 5th  Team 1 Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[6]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# # 5th  Team 1 Player search "c" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[6]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("a")
time.sleep(1)
# # 5th  Team 1 Player search "c" option -> Bryan McLaughlin, Staten Island, NY-> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[6]/div[2]/div[1]/div/div[4]/div/div/span/div[6]/div[2]").click()
time.sleep(1)
# # Donation
# # Flood 50 click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[2]/label/input").click()
# time.sleep(1)
# # Flood 50 -> Next button click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[5]/div/button[2]/span").click()
# time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No -> Ok button  click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
time.sleep(1)

### 5thTeam 2nd Player ########

# 5th Team 2nd player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[6]/div[2]/div[2]/div/div[4]/div/div/img").click()
time.sleep(1)
# 5th Team 2nd Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[6]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 5th Team 2nd Player search "d" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[6]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("d")
time.sleep(1)
# 5th Team 2nd Player search "d" option -> Dominik Huzar, Brick, NJ-> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[6]/div[2]/div[2]/div/div[4]/div/div/span/div[6]/div[2]").click()
time.sleep(1)

############# 6th Team ##########
#######Team 6th 1st Player #############

# 6th Team 1 player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[7]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# # 6th  Team 1 Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[7]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# # 6th  Team 1 Player search "c" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[7]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("a")
time.sleep(1)
# # 6th  Team 1 Player search "c" option -> Charlie  Risser , Lititz , PA-> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[7]/div[2]/div[1]/div/div[4]/div/div/span/div[7]/div[2]").click()
time.sleep(1)
# # Donation
# # Flood 50 click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[2]/label/input").click()
# time.sleep(1)
# # Flood 50 -> Next button click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[5]/div/button[2]/span").click()
# time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No -> Ok button  click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
time.sleep(1)

### 6thTeam 2nd Player ########

# 6th Team 2nd player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[7]/div[2]/div[2]/div/div[4]/div/div/img").click()
time.sleep(1)
# 6th Team 2nd Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[7]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 6th Team 2nd Player search "d" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[7]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("d")
time.sleep(1)
# 6th Team 2nd Player search "d" option -> Eddie Zook, Belews Creek, NC-> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[7]/div[2]/div[2]/div/div[4]/div/div/span/div[6]/div[2]").click()
time.sleep(1)

################# 7th Team ##########

# 7th Team 1 player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[8]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# # 7th  Team 1 Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[8]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# # 7th  Team 1 Player search "c" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[8]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("a")
time.sleep(1)
# # 7th  Team 1 Player search "c" option -> Ronnie Colafrancesco, CRANSTON, RI-> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[8]/div[2]/div[1]/div/div[4]/div/div/span/div[3]/div[2]").click()
time.sleep(1)
# # Donation
# # Flood 50 click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[2]/label/input").click()
# time.sleep(1)
# # Flood 50 -> Next button click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[5]/div/button[2]/span").click()
# time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No -> Ok button  click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
time.sleep(1)

### 8thTeam 1st Player ########

# 8th Team 1st player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[9]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# 8th Team 1st Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[9]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 8th Team 1st Player search "d" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[9]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("d")
time.sleep(1)
# 8th Team 1st Player search "d" option -> Fernando  Brenes, Myrtle Beach , SC-> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[9]/div[2]/div[1]/div/div[4]/div/div/span/div[3]/div[2]").click()
time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No -> Ok button  click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
time.sleep(1)

################ 8team##

#### 9th 1st Player #######
# 9th Team 1 player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[10]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# # 9th  Team 1 Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[10]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# # 9th  Team 1st  Player search "a" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[10]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("a")
time.sleep(1)
# # 9th  Team 1 Player search "a" option -> Jason Stefon, Warwick, RI-> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[10]/div[2]/div[1]/div/div[4]/div/div/span/div[10]/div[2]").click()
time.sleep(1)
# # Donation
# # Flood 50 click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[2]/label/input").click()
# time.sleep(1)
# # Flood 50 -> Next button click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[5]/div/button[2]/span").click()
# time.sleep(1)
# Team will be Created. Do you want to continue? do you want - ok
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/button[2]/span").click()
time.sleep(1)

#### 9th Team  2nd Player ##########
# 9 th Team 2nd player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[10]/div[2]/div[2]/div/div[4]/div/div/img").click()
time.sleep(1)
# 9th Team 2nd Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[10]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 9th Team 2nd Player search "d" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[10]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("d")
time.sleep(1)
# 9 th Team 2nd  Player search "d" option -> Jay Goldmanu , Howell , NJ-> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[10]/div[2]/div[2]/div/div[4]/div/div/span/div[3]/div[2]").click()
time.sleep(1)

#########################
# 9th Team  2nd Player Again  ##########
# 9th Team 2nd player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[10]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# 9th Team 2nd Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[10]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 9th Team 2nd Player search "d" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[10]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("d")
time.sleep(1)
# 9 th Team 2nd  Player search "d" option -> Jay Goldmanu , Howell , NJ-> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[10]/div[2]/div[1]/div/div[4]/div/div/span/div[2]/div[2]").click()
time.sleep(1)
# Do you wish to generate the invoice for the team? No click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
time.sleep(1)
# Ok button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
time.sleep(1)



############## 7th Team 2nd Player again #############

#### 7th Team  2n  Player Again  ##########
# 7th Team 2nd player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[8]/div[2]/div[2]/div/div[4]/div/div/img").click()
time.sleep(1)
# 7th Team 2nd Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[8]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 7th Team 2nd Player search "r" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[8]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("r")
time.sleep(1)
# 7th Team 2nd  Player search "r" option -> Tripp Hewitt, Myrtle Beach, SC-> click
driver.find_element(By.XPATH, "").click()
time.sleep(1)
# Team will be Created. Do you want to continue? ok click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/button[2]/span").click()
# time.sleep(1)

driver.execute_script("window.scrollTo({},{});".format(0, 800))

### After Team Added Save Button Click ####
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/span").click()
time.sleep(200)

# ###### https://promoter.applination.in/RegEventEdit/8466 ############
# driver.get("https://promoter.applination.in/RegEventEdit/8466")
# driver.find_element ( By.XPATH , "/html/body/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/span" ).click ()
# time.sleep ( 200 )






