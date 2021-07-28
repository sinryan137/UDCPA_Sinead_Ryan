import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests

data = requests.get("http://api.open-notify.org/iss-now.json")
parsed_data = data.json()
print(parsed_data["timestamp"])

data2 = requests.get("http://api.open-notify.org/astros.json")
parsed_data2 = data2.json()


for p in parsed_data2['people']:
    print(p['name'])




data1 = requests.get(
    "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=8HKU2KODGW7DY1OA")
print(data1)

df=pd.read_csv("financials.csv")
print(df.head(5))
print(df.describe)
print(df.info())

missing = df.isnull().sum()
print(missing)

print(df.isna().sum())

df.fillna(df.mean(), inplace=True)
print(df.isna().sum())
print(df.Name.duplicated().sum())
print(~df.Name.duplicated().sum())
print(df.loc[df.duplicated(), :])
print(df.groupby(['Sector']).Price.agg([min, max]))
print(df.sort_values(by=['EBITDA', 'Name'], ascending=False)[['EBITDA', 'Name']])
print(df.set_index(['Sector', 'Price/Earnings']))

print(df['Price/Earnings'].mean())
print(df['Price/Earnings'].median())

print(df.loc[1:20, ['Name']])

stockprices = pd.read_csv("SP 500 Stock Prices 2014-2017.csv")
print(stockprices.head(5))
print(stockprices.describe)
print(stockprices.info())

financials = df.merge(stockprices, how='left',
                                      left_on="Symbol",
                                      right_on="symbol")

print(financials.info())

print(financials.sort_values(by=['high', 'Name'], ascending=False)[['high', 'Name']])

company_array = np.array(['A.O. Smith Corp', 'Abbot Laboratories', 'AbbVie Inc.', 'Accenture plc', 'Activision Blizzard', 'Acuity Brands Inc', 'Adobe Systems Inc', 'Advance Auto Parts', 'Advanced Micro Devices Inc', 'AES Corp'])
indexing_array = np.array([1, 3, 5, 7, 9])
company_subset = company_array[indexing_array]
print(company_subset)

def sayhello():
    print("Hello World")
print(sayhello())


Avg_PE_Sector=financials.groupby("Sector")['Price/Earnings'].mean()
Avg_PE_Sector.plot(x="Price/Earnings", y="Sector", kind='bar', title="Mean_P/E_by_Sector", rot=45)
plt.show()

print(financials.groupby(['Sector']).sum())

print(financials.loc[financials['Sector'] == 'Materials'])

Consumer_Discretionary = df['Sector'] == 'Consumer Discretionary'
Consumer_Staples = df['Sector'] == 'Consumer Staples'
Health_Care = df['Sector'] == 'Health Care'
Information_Technology = df['Sector'] == 'Information Technology'
Energy = df['Sector'] == 'Energy'
Real_Estate = df['Sector'] == 'Real Estate'
fig, ax = plt.subplots()
ax.plot(Consumer_Discretionary['Price'], Consumer_Discretionary['Dividend Yield'], color='red', label=Consumer_Discretionary)
ax.plot(Consumer_Staples['Price'], Consumer_Staples['Dividend Yield'], color='blue', label=Consumer_Staples)
ax.plot(Energy['Price'], Energy['Dividend Yield'], color='green', label=Energy)
ax.plot(Health_Care['Price'], Health_Care['Dividend Yield'], color='purple', label=Health_Care)
ax.plot(Real_Estate['Price'], Real_Estate['Dividend Yield'], color='brown', label=Real_Estate)
ax.plot(Information_Technology['Price'], Information_Technology['Dividend Yield'], color='pink', label=Information_Technology)

ax.ledgend()
ax.set_xlabel('Price')
ax.set_ylabel('Dividend Yield')

plt.show()



