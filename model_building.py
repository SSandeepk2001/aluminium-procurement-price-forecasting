import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import pmdarima as pm
from fbprophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error



# Load dataset
df = pd.read_csv("aluminium_prices.csv", parse_dates=["date"], index_col="date")
df = df.asfreq("D")  # Ensure daily frequency
df["price"] = df["price"].fillna(method="ffill")  # Fill missing values

result = adfuller(df["price"])
print(f"ADF Statistic: {result[0]}")
print(f"P-Value: {result[1]}")  # Should be < 0.005 for stationarity

if result[1] > 0.005:
    df["price_diff"] = df["price"].diff().dropna()
    
    
    
auto_arima_model = pm.auto_arima(df["price"], seasonal=True, stepwise=True, suppress_warnings=True)
print(auto_arima_model.summary())




p, d, q = auto_arima_model.order
P, D, Q, s = auto_arima_model.seasonal_order

sarima_model = ARIMA(df["price"], order=(p, d, q), seasonal_order=(P, D, Q, s))
sarima_model_fit = sarima_model.fit()
print(sarima_model_fit.summary())




forecast = sarima_model_fit.get_forecast(steps=30)
forecast_index = pd.date_range(start=df.index[-1], periods=30, freq="D")
forecast_df = pd.DataFrame({"Forecasted Price": forecast.predicted_mean}, index=forecast_index)

plt.figure(figsize=(12,5))
plt.plot(df.index, df["price"], label="Actual Prices", color="blue")
plt.plot(forecast_df.index, forecast_df["Forecasted Price"], label="Forecast", color="red")
plt.legend()
plt.show()

y_true = df["price"].iloc[-30:]  # Last 30 days
y_pred = forecast.predicted_mean

mae = mean_absolute_error(y_true, y_pred)
rmse = np.sqrt(mean_squared_error(y_true, y_pred))

print(f"MAE: {mae}")
print(f"RMSE: {rmse}")

df_prophet = df.reset_index().rename(columns={"date": "ds", "price": "y"})
prophet_model = Prophet()
prophet_model.fit(df_prophet)

future = prophet_model.make_future_dataframe(periods=30)
forecast_prophet = prophet_model.predict(future)

prophet_model.plot(forecast_prophet)
plt.show()