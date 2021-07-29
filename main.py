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




print(financials.groupby(['Sector']).sum())

print(financials.loc[financials['Sector'] == 'Materials'])
Avg_PE_Sector=financials.groupby("Sector")['Price/Earnings'].mean()
Avg_PE_Sector.plot(x="Price/Earnings", y="Sector", kind='bar', title="Mean_P/E_by_Sector", rot=45)
plt.show()

financials['year'] = pd.DatetimeIndex(financials['date']).year
print(financials['year'])

Consumer_Discretionary = financials.loc[financials['Sector'] == 'Consumer Discretionary']
Consumer_Staples = financials.loc[financials['Sector'] == 'Consumer Staples']
Health_Care = financials.loc[financials['Sector'] == 'Health Care']
Information_Technology = financials.loc[financials['Sector'] == 'Information Technology']
Energy = financials.loc[financials['Sector'] == 'Energy']
Real_Estate = financials.loc[financials['Sector'] == 'Real Estate']

Avg_high_Consumer_Discretionary = Consumer_Discretionary.groupby('year')['high'].mean()
Avg_high_Consumer_Staples = Consumer_Staples.groupby('year')['high'].mean()
Avg_high_Health_Care = Health_Care.groupby('year')['high'].mean()
Avg_high_Information_Technology = Information_Technology.groupby('year')['high'].mean()
Avg_high_Energy = Energy.groupby('year')['high'].mean()
Avg_high_Real_Estate = Real_Estate.groupby('year')['high'].mean()



fig, ax = plt.subplots()
Avg_high_Consumer_Discretionary.plot(x='year', y='high', kind='line', label='Consumer Disc', rot=45)
Avg_high_Consumer_Staples.plot(x='year', y='high', kind='line', label='Consumer Staples', rot=45)
Avg_high_Health_Care.plot(x='year', y='high', kind='line', label='Health Care', rot=45)
Avg_high_Information_Technology.plot(x='year', y='high', kind='line', label='Information Tech', rot=45)
Avg_high_Energy.plot(x='year', y='high', kind='line', label='Energy', rot=45)
Avg_high_Real_Estate.plot(x='year', y='high', kind='line', label='Real Estate', rot=45)
plt.title("Mean 'High' per Year")
plt.xlabel('Year')
plt.ylabel('High $')
plt.legend()
plt.show()