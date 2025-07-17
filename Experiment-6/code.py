import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import plotly.express as px
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv'
df = pd.read_csv(url, parse_dates=['Month'], index_col='Month')
print("Dataset Head:\n", df.head())
print("\nSummary Statistics:\n", df.describe())
plt.figure(figsize=(10, 5))
plt.plot(df, marker='o', linestyle='-')
plt.title('Monthly Airline Passengers')
plt.xlabel('Year')
plt.ylabel('Passengers')
plt.grid(True)
plt.show()
df['Month_Num'] = df.index.month
df['Year'] = df.index.year
decomp = seasonal_decompose(df['Passengers'], model='multiplicative')
decomp.plot()
plt.suptitle('Seasonal Decomposition', fontsize=16)
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 5))
sns.boxplot(x='Month_Num', y='Passengers', data=df)
plt.title('Monthly Variation in Passengers')
plt.xlabel('Month')
plt.ylabel('Passengers')
plt.grid(True)
plt.show()
rolling_mean = df['Passengers'].rolling(window=12).mean()
rolling_std = df['Passengers'].rolling(window=12).std()
plt.figure(figsize=(12, 5))
plt.plot(df['Passengers'], label='Original')
plt.plot(rolling_mean, label='Rolling Mean (12 months)', color='red')
plt.plot(rolling_std, label='Rolling Std Dev (12 months)', color='green')
plt.legend()
plt.title('Rolling Mean and Standard Deviation')
plt.show()
plot_acf(df['Passengers'], lags=20)
plt.title('Autocorrelation')
plt.show()
plot_pacf(df['Passengers'], lags=20)
plt.title('Partial Autocorrelation')
plt.show()