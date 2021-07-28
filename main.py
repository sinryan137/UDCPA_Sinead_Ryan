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

sectors_column=df['Sector']
sectors=df['Sector'].unique()
print(sectors)

fig, ax = plt.subplots()
for sector in sectors:
    sector_df=df[df['Sector'] == sector]
    ax.plot(sector, sector_df['Price'].mean(), yerr=sector_df['Price'].std())
    ax.set_ylabel='Price'
    ax.set_xlabel='sector'
    plt.show()
Consumer_Discretionary = df.loc[df['Sector'] == 'Consumer Discretionary']
Consumer_Staples = df.loc[df['Sector'] == 'Consumer Staples']
Health_Care = df['Sector'] == 'Health Care'
Information_Technology = df.loc[df['Sector'] == 'Information Technology']
Energy = df.loc[df['Sector'] == 'Energy']
Real_Estate = df.loc[df['Sector'] == 'Real Estate']

fig, ax = plt.subplots()
ax.plot(Real_Estate['Price/Earnings'], Real_Estate['Price'], color='red', label=Consumer_Discretionary)
ax.set_xlabel('Sector')
ax.set_ylabel('Price/Earnings')

plt.show()


