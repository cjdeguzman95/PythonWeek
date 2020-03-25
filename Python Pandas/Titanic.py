import pandas as pd
import os

path = os.getcwd()
dfTitanic = pd.read_csv(path+"/"+"Titanic.csv")

print(dfTitanic.head(5))
