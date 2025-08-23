# Install Prophet (works well in Colab)
!pip install prophet

# Import core libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Plot style
sns.set(style="whitegrid")

# Create sample monthly sales dataset
date_rng = pd.date_range(start='2018-01-01', end='2023-12-01', freq='MS')
np.random.seed(42)
sales = np.random.randint(20000, 50000, size=len(date_rng)) + np.linspace(0, 10000, len(date_rng))

df = pd.DataFrame({'Month': date_rng, 'Sales': sales})
df.set_index('Month', inplace=True)

print("Sample Sales Data:")
df.head()

plt.figure(figsize=(12,6))
plt.plot(df.index, df['Sales'], marker='o', linestyle='-')
plt.title("Monthly Sales Revenue Over Time")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# Prophet requires columns: 'ds' (date) and 'y' (value)
prophet_df = df.reset_index().rename(columns={"Month": "ds", "Sales": "y"})

# Train-Test split (last 12 months as test)
train_df = prophet_df.iloc[:-12]
test_df = prophet_df.iloc[-12:]

print("Train Data Range:", train_df['ds'].min(), "to", train_df['ds'].max())
print("Test Data Range:", test_df['ds'].min(), "to", test_df['ds'].max())

model = Prophet()
model.fit(train_df)

# Forecast into future including test period
future = model.make_future_dataframe(periods=12, freq='MS')
forecast = model.predict(future)

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

plt.figure(figsize=(12,6))

# Training data
plt.plot(train_df['ds'], train_df['y'], label='Training Data')

# Actual test data
plt.plot(test_df['ds'], test_df['y'], label='Actual Sales (Test)', color='black')

# Forecast
plt.plot(forecast['ds'], forecast['yhat'], label='Forecasted Sales', color='red')

# Confidence interval
plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'],
                 color='pink', alpha=0.3)

plt.legend()
plt.title("Forecast vs Actual Sales")
plt.show()

# Merge actual vs predicted for test period
pred_test = forecast.set_index('ds').loc[test_df['ds'], 'yhat']
mae = mean_absolute_error(test_df['y'], pred_test)
rmse = np.sqrt(mean_squared_error(test_df['y'], pred_test))

print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

# Forecast 12 more months beyond dataset
future2 = model.make_future_dataframe(periods=24, freq='MS')  # 12 test + 12 future
forecast2 = model.predict(future2)

# Extract only future part
future_forecast = forecast2.set_index('ds').iloc[-12:][['yhat','yhat_lower','yhat_upper']]

plt.figure(figsize=(12,6))
plt.plot(df.index, df['Sales'], label='Historical Sales')
plt.plot(future_forecast.index, future_forecast['yhat'], label='Future Forecast', color='green')
plt.fill_between(future_forecast.index, future_forecast['yhat_lower'], future_forecast['yhat_upper'],
                 color='lightgreen', alpha=0.3)
plt.legend()
plt.title("Future 12-Month Sales Forecast")
plt.show()

future_forecast
