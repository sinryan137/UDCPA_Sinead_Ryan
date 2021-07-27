import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests

data = requests.get("http://api.open-notify.org/iss-now.json")
parsed_data = data.json()
print(parsed_data["timestamp"])

data1 = requests.get(
    "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=8HKU2KODGW7DY1OA")
print(data1)

df=pd.read_csv("financials.csv")
print(df.head(5))
print(df.describe)
print(df.info())

missing = df.isnull().sum()
print(missing)
