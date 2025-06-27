import pandas as pd
df = pd.read_csv("weekly_temperatures.csv", parse_dates=["Date"])
df['Month'] = df['Date'].dt.month
monthly_sum = df.groupby(['City', 'Month'])['Temperature'].sum().reset_index()
pivot_table = monthly_sum.pivot(index='City', columns='Month', values='Temperature').fillna(0)
summer_months = [6, 7, 8]
pivot_table['Summer_Total'] = pivot_table[summer_months].sum(axis=1)
max_city = pivot_table['Summer_Total'].idxmax()
max_value = pivot_table['Summer_Total'].max()
print("Month-wise Temperature Summary (Total per City):")
print(pivot_table)
print("\n City with Highest Total Summer Temperature:")
print(f"{max_city} with {max_value:.2f} total temperature in summer months.")
