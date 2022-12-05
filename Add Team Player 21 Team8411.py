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

##21 Team
# driver.get("https://promoter.applination.in/RegEventEdit/8403")

############21 Teams ###############
driver.get("https://promoter.applination.in/RegEventEdit/8411")

# driver.get("https://promoter.applination.in/RegEventEdit/8380")
# driver.get("https://promoter.applination.in/RegEventEdit/8383")

# driver.execute_script("window.scrollTo({},{});".format(0, 3500))

# Mens Open 35+ , Team 1-0  (+) icon click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div[1]/div[1]/div[2]/img").click()
# time.sleep(1)


# Scrolling till the end of page
#driver.get(url) # grab the url
# print("Started Scrolling ... ")
# match=False # change to 'False' for making this work
# lenOfPage = driver.execute_script (
#     "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;" )
# while(match==False):
#         lastCount = lenOfPage
#         lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
#         if lastCount==lenOfPage:
#             match=True
# source_data = driver.page_source # page source code as html

# Get all click buttons , number of buttons collected
#     total_buttons = []
#     try:
#     total_buttons = driver.find_elements_by_class_name("ant-collapse-expand-icon")
#     except:
#     print("Unable to drop down button click")
#     print("Total drop down click: " + str(len(total_buttons)))


driver.execute_script("window.scrollTo({},{});".format(0, 800))



######### 1 st Division Mens open 35+ ##########

# Mens open 35+ -> Open after team 1-0 icon click next page -> details Mens 35_ open -> division  -> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[1]/div/span/img").click()
time.sleep(1)

############# Kunal #################
paths = {
    "iconClick": "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/img" ,
    "searchOptionClick": "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input" ,
    "searchAOption": "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input" ,
    "searchAOptionRandomName": "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[2]/div[2]" ,
    "donation40": "/html/body/div[2]/div/div[2]/div/div[3]/div[3]/label/input" ,
    "nextButtonClick": "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input" ,
    "generateInvoiceNo": "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input" ,
    "generateInvoiceNoOkClick": "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span"}

for x in paths:
    print ( x , paths[x] )
    if x=="iconClick":driver.find_element ( By.XPATH , paths[x] ).click ()
    if x =='searchOptionClick':driver.find_element ( By.XPATH , paths[x] ).click ()
    if x =='searchAOption':driver.find_element ( By.XPATH , paths[x] ).send_keys ( "a" )
    if x == 'searchAOptionRandomName':driver.find_element ( By.XPATH , paths[x] ).click ()
    if x == 'donation40':driver.find_element ( By.XPATH , paths[x] ).click ()
    if x == 'nextButtonClick':driver.find_element ( By.XPATH , paths[x] ).click ()
    if x == 'generateInvoiceNo':driver.find_element ( By.XPATH , paths[x] ).click ()
    if x == 'generateInvoiceNoOkClick':driver.find_element ( By.XPATH , paths[x] ).click ()

time.sleep ( 1 )

################ new Code ##########

### Add Team ####

#Elements = driver.find_elements(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/img")
#for elem in Elements:
    #Required.append(elem)

#
# # 1 Team 1 player + icon click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/img").click()
# time.sleep(1)
# # 1Team 1 Player search option click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
# time.sleep(1)
# # 1Team 1 Player search "a" option -> send key
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("a")
# time.sleep(1)
# # 1Team 1 Player search "a" option -> Richard Abiador, Bothell, WA -> click
# driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[2]/div[2]").click()
# time.sleep(1)
# # Donation
# # Flood 40 click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[3]/label/input").click()
# time.sleep(1)
# # Flood 40 -> Next button click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
# time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
# time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No -> Ok button  click
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
# time.sleep(1)

# # 1st Team 2nd player



# 1 Team 2nd player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div/img").click()
time.sleep(1)
# 1Team 2nd Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 1Team 2nd Player search "b" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("b")
time.sleep(1)
# 1Team 2nd Player search "b" option -> Joe Barra, Eatontown, NJ -> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div/span/div[2]/div[2]").click()
time.sleep(1)


#####2nd Team 1st player
# 2nd Team 1 player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# # 2nd Team 1 Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# # 2nd Team 1 Player search "c" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("a")
time.sleep(1)
# # 2nd Team 1 Player search "c" option -> Colin  Beebe, Chevy Chase, MD-> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/span/div[2]/div[2]").click()
time.sleep(1)
# # Donation
# # Flood 50 click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[2]/label/input").click()
time.sleep(1)
# # Flood 50 -> Next button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[5]/div/button[2]/span").click()
time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No -> Ok button  click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
time.sleep(1)

# # 2nd Team 2nd player

# 2nd Team 2nd player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/img").click()
time.sleep(1)
# 1Team 2nd Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 1Team 2nd Player search "d" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("d")
time.sleep(1)
# 1Team 2nd Player search "d" option -> Darren Chaumont, Lake Charles, LA -> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/span/div[4]/div[2]").click()
time.sleep(2)







driver.execute_script("window.scrollBy(0,1000)","")

################# 2nd Division Mens A 35+ ##########

# Mens A 35+ -> Open after team 1-0 icon click next page -> details Mens A 35+ -> division  -> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[2]/div[1]/div/span/img").click()
time.sleep(1)

###Add Team ####
# 1 Team 1 player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# 1Team 1 Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 1Team 1 Player search "a" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("a")
time.sleep(1)
# 1Team 1 Player search "a" option -> Alan Allred, Elon, NC-> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/span/div[3]/div[2]").click()
time.sleep(1)
# Donation
# Flood 40 click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[3]/label/input").click()
time.sleep(1)
# Flood 40 -> Next button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[5]/div/button[2]/span").click()
time.sleep(1)
# Do you wish to generate the invoice for the team? -> No click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
time.sleep(1)
# Do you wish to generate the invoice for the team? -> No -> Ok button  click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
time.sleep(1)

# # 1st Team 2nd player

# 1 Team 2nd player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div/img").click()
time.sleep(1)
# 1Team 2nd Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 1Team 2nd Player search "b" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("b")
time.sleep(1)
# 1Team 2nd Player search "b" option -> Bryan McLaughlin, Staten Island, NY -> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div/span/div[8]/div[2]").click()
time.sleep(1)


#####2nd Team 1st player
# 2nd Team 1 player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/img").click()
time.sleep(1)
# # 2nd Team 1 Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# # 2nd Team 1 Player search "c" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("c")
time.sleep(1)
# # 2nd Team 1 Player search "c" option -> Chris Gable, Toms River, NJ-> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div/div[4]/div/div/span/div[8]/div[2]").click()
time.sleep(1)
# # Donation
# # Flood 50 click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[2]/label/input").click()
time.sleep(1)
# # Flood 50 -> Next button click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[5]/div/button[2]/span").click()
time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/label/input").click()
time.sleep(1)
# # Do you wish to generate the invoice for the team? -> No -> Ok button  click
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
time.sleep(1)

# # 2nd Team 2nd player

# 2nd Team 2nd player + icon click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/img").click()
time.sleep(1)
# 1Team 2nd Player search option click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").click()
time.sleep(1)
# 1Team 2nd Player search "d" option -> send key
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/span/div[1]/div[2]/input").send_keys("d")
time.sleep(1)
# 1Team 2nd Player search "d" option -> Dominik Huzar, Brick, NJ -> click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/span/div[7]/div[2]").click()
time.sleep(200)
