import sys
# print(sys.path)
# import time
# initial = time.time()
# Current working directory
'''import os
print(os.getcwd())'''

# Display all files present in the current working directory
# print(os.listdir(os.getcwd()))



import pandas as pd
pd.read_csv("excelsheet.xlsx")

'''# Create a dataframe
raw_data = {'first_name': ['Sam','Ziva','Kia','Robin'],
        'degree': ['PhD','MBA','','MS'],
        'age': [25, 29, 19, 21]}
df = pd.DataFrame(raw_data) n 

df

#Save the dataframe to the current directory
df.to_excel(r'Example1.xlsx')

# Read the excel file
# df = pd.read_excel(r"D:\pythonProjectpromoter\excelsheet.xlsx")
df = pd.read_excel(r'D:\pythonProjectpromoter\excelsheet',sheet_name="excelsheet")

df'''