import pandas as pd

data=pd.read_csv("https://raw.githubusercontent.com/rishipawani/Student-Data/refs/heads/main/T%20test.xlsx%20-%20Sheet1.csv")

df=pd.DataFrame(data)

print(df.head())
