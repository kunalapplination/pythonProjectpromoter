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

# driver.get("https://promoter.applination.in/RegEventEdit/8380")
driver.get("https://promoter.applination.in/RegEventEdit/8383")
# driver.get("https://promoter.applination.in/RegEventEdit/8461")

driver.execute_script("window.scrollTo({},{});".format(0, 3500))


# Add team with Player  icon click details
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[1]/div/span/img").click()
time.sleep(2)
################ 4 Team ################

############ For 1st Team Again Add ##############
# 1 st time add - Add team with Player Hamberger icon 1st time   click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[1]/div/div/img").click()
# time.sleep(2)

# #1st time add - Add Team in Hambergar icon click in 2nd times Add Team option
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[1]/div/div/span/ul/li").click()
# time.sleep(1)
################# for 2nd Team Add ##############

# ##2nd time  add - Again # Add team with Player Hamberger icon 1st time    click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[1]/div/div/img").click()
# time.sleep(2)

# ### 2nd  time add - Add Team in Hambergar icon click in 2nd times Add Team option
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[1]/div/div/span/ul/li").click()
# time.sleep(1)

########## 1st Team 1st Player Add #########
# 1st Team 1st player + click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# 1stTeam 1st Player Search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 1stTeam 1st Player Search option  name  a send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("a")
time.sleep(1)
# 1stTeam 1st Player Search option  name  a -> Richard Abiador, Bothell, WA  click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[2]/div[2]").click()
time.sleep(1)
# 1stTeam 1st Player Search option  name  a -> Richard Abiador, Bothell, WA  -> Donation 40 click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[3]/label/input").click()
time.sleep(1)
# 1stTeam 1st Player Search option  name  a -> Richard Abiador, Bothell, WA-> Donation 40 -> Next Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[5]/div/button[2]/span").click()
time.sleep(1)
# 1stTeam 1st Player Search option  name  a -> Richard Abiador, Bothell, WA -> Donation 40 -> Next Button -> Do you wish to generate the invoice for the team?  No click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
time.sleep(1)
# 1stTeam 1st Player Search option  name  a -> Richard Abiador, Bothell, WA -> Donation 40 -> Next Button -> Do you wish to generate the invoice for the team? -> OK click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
time.sleep(1)

############## 1st Team 2nd Player Add ###############
# 1st Team 2nd player + click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div/img").click()
time.sleep(1)
# 1stTeam 2nd Player Search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 1stTeam 2nd Player Search option  name  b send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("b")
time.sleep(1)
# 1stTeam 2nd Player Search option  name  b -> Bryan McLaughlin, Staten Island, NY  click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div/span/div[7]/div[2]").click()
time.sleep(1)

####### 2nd Team with Player  ########
# 2nd Team 1st player + click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# 2ndTeam 1st Player Search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 2ndTeam 1st Player Search option  name  c send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("c")
time.sleep(1)
# 2ndTeam 1st Player Search option  name  c -> Colin  Beebe, Chevy Chase, MDclick
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/span/div[2]/div[2]").click()
time.sleep(1)
# 2ndTeam 1st Player Search option  name  c -> Colin  Beebe, Chevy Chase, MD-> Donation 50 click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[2]/label/input").click()
time.sleep(1)
# 2ndTeam 1st Player Search option  name  c -> Colin  Beebe, Chevy Chase, MD-> Donation 50 -> Next Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[5]/div/button[2]/span").click()
time.sleep(1)
# 2ndTeam 1st Player Search option  name  c-> Colin  Beebe, Chevy Chase, MD -> Donation 50 -> Next Button -> Do you wish to generate the invoice for the team? -> No Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
time.sleep(1)
# 2ndTeam 1st Player Search option  name  c -> Colin  Beebe, Chevy Chase, MD-> Donation 50 -> Next Button -> Do you wish to generate the invoice for the team? -> OK click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
time.sleep(1)

############## 2nd Team 2nd Player Add ###############
# 2nd Team 2nd player + click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/img").click()
time.sleep(1)
# 2nd Team 2nd Player Search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 2nd Team2nd Player Search option  name  d send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("d")
time.sleep(1)
# 2nd Team 2nd Player Search option  name d -> Darren Chaumont, Lake Charles, LA click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/span/div[4]/div[2]").click()
time.sleep(1)

####### Team 3  ########
# 3rd Team 1st player + click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# 3rdTeam  1st Player Search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 3rdTeam  1st Player Search option  name  e send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("e")
time.sleep(1)
# 3rdTeam  1st Player Search option  name  e -> Joe Barra, Eatontown, NJ click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[4]/div/div/span/div[3]/div[2]").click()
time.sleep(1)
# 3rdTeam  1st Player Search option  name  e -> Joe Barra, Eatontown, NJ MD-> Donation 50 click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[2]/label/input").click()
time.sleep(1)
# 3rdTeam  1st Player Search option  name  e -> Joe Barra, Eatontown, NJ-> Donation 50 -> Next Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[5]/div/button[2]/span").click()
time.sleep(1)
# 3rdTeam 1st Player Search option  name  e-> Colin  Joe Barra, Eatontown, NJ-> Donation 50 -> Next Button -> Do you wish to generate the invoice for the team? -> No Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
time.sleep(1)
# 3rdTeam  1st Player Search option  name  e -> Joe Barra, Eatontown, NJ-> Donation 50 -> Next Button -> Do you wish to generate the invoice for the team? -> OK click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
time.sleep(1)

############## 3rd Team 2nd Player Add ###############
# 3rdTeam 2nd player + click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[4]/div[2]/div[2]/div/div[4]/div/div").click()
time.sleep(1)
# 3rd Team 2nd Player Search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[4]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 3rd Team 2nd Player Search option  name  f send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[4]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("f")
time.sleep(1)
# 3rdTeam 2nd Player Search option  name f -> Fernando  Brenes, Myrtle Beach , SC click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[4]/div[2]/div[2]/div/div[4]/div/div/span/div[2]/div[2]").click()
time.sleep(1)

####### Team 4th   ########
# 4th Team 1st player + click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# 4th Team  1st Player Search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 4th Team  1st Player Search option  name  g send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("g")
time.sleep(1)
# 4th Team  1st Player Search option  name  g -> Greg Cassel, Harrisburg, PA click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div[1]/div/div[4]/div/div/span/div[2]/div[2]").click()
time.sleep(1)
# 4th Team  1st Player Search option  name  g -> Greg Cassel, Harrisburg, PA-> Donation 50 click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[2]/label/input").click()
time.sleep(1)
# 4th Team  1st Player Search option  name  g -> Greg Cassel, Harrisburg, PA-> Donation 50 -> Next Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[5]/div/button[2]/span").click()
time.sleep(1)
# 4th Team 1st Player Search option  name  g-> Greg Cassel, Harrisburg, PA-> Donation 50 -> Next Button -> Do you wish to generate the invoice for the team? -> No Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
time.sleep(1)
# 4th Team  1st Player Search option  name  g -> Greg Cassel, Harrisburg, PA-> Donation 50 -> Next Button -> Do you wish to generate the invoice for the team? -> OK click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
time.sleep(1)


############## 4th Team 2nd Player Add ###############
# 4th Team2nd player + click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div[2]/div/div[4]/div/div/img").click()
time.sleep(1)
# 4th Team 2nd Player Search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 4th Team 2nd Player Search option  name  f send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("f")
time.sleep(1)
# 4th Team 2nd Player Search option  name f -> Frank Primiano, Toms River, click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div[2]/div/div[4]/div/div/span/div[3]/div[2]").click()
time.sleep(1)



############### Team 5 ############################
####### Team 5th   ########
# 5th Team 1st player + click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[6]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# 5th Team  1st Player Search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[6]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 5th Team  1st Player Search option  name  g send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[6]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("g")
time.sleep(1)
# 5th Team  1st Player Search option  name  g -> Henry Ping, BELLEVUE, WA click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[6]/div[2]/div[1]/div/div[4]/div/div/span/div[5]/div[2]").click()
time.sleep(1)
# 5th Team  1st Player Search option  name  g -> Henry Ping, BELLEVUE, WA -> Donation 50 click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[2]/label/input").click()
time.sleep(1)
# 5th Team  1st Player Search option  name  g -> Henry Ping, BELLEVUE, WA -> Donation 50 -> Next Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[5]/div/button[2]/span").click()
time.sleep(1)
# 5th Team 1st Player Search option  name  g-> Henry Ping, BELLEVUE, WA-> Donation 50 -> Next Button ->Team will be Created. Do you want to continue? -> Ok Button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/button[2]/span").click()
time.sleep(1)

#####5th Team 2nd Player #####

############## 5th Team 2nd Player Add ###############
# 5th Team 2nd player + click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[6]/div[2]/div[2]/div/div[4]/div/div/img").click()
time.sleep(1)
# 5th Team 2nd Player Search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[6]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 5th Team 2nd Player Search option  name  d send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("d")
time.sleep(1)
# 5th Team 2nd Player Search option  name d -> Dominik Huzar, Brick, NJ click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div/div[2]/div/div/div[6]/div[2]/div[2]/div/div[4]/div/div/span/div[5]/div[2]").click()
time.sleep(1)

driver.execute_script("window.scrollTo({},{});".format(0, 600))

# save button click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/span").click()
time.sleep(1)

# After Save Team then Details page on icon to view teams details
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div/div/div/span/img").click()
time.sleep(2)

