import pandas as pd

data = pd.read_excel("data/data.xlsx", engine="openpyxl")
data['Sum'] = data['A']+data['B']
data.to_excel("data/Output.xlsx")

print('Data Processing Complete')