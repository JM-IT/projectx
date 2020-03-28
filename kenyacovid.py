print("\nPlease Wait as it loads the data set.....\n")
import pandas as pd
covid_data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-26-2020.csv')
country =input("Enter Country here to search for cases:")
data = covid_data[covid_data['Country_Region'] == country]
data = data[['Province_State','Confirmed','Deaths','Recovered']]
result = data.sort_values(by='Confirmed',ascending=False)
result.reset_index(drop=True)
print(result)
