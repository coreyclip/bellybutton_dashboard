import pandas as pd 

df = pd.read_csv('Belly_Button_Biodiversity_Metadata.csv')

print(df.info())
print(df.describe())