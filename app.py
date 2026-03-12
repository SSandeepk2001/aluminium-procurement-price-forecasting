import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Load trained models
sarima_model = pickle.load(open("sarima_model.pkl", "rb"))
prophet_model = pickle.load(open("prophet_model.pkl", "rb"))

st.title("Aluminium Price Forecasting")

# Date Input
date_input = st.date_input("Select a future date")

if st.button("Predict Price"):
    date = pd.to_datetime(date_input)
    
    # SARIMA Prediction
    forecast = sarima_model.get_forecast(steps=30)
    forecast_index = pd.date_range(start=pd.Timestamp.today(), periods=30, freq="D")
    sarima_forecast_df = pd.DataFrame({"Forecasted Price": forecast.predicted_mean}, index=forecast_index)

    if date in sarima_forecast_df.index:
        sarima_predicted_price = sarima_forecast_df.loc[date, "Forecasted Price"]
        sarima_display_price = f"${sarima_predicted_price:.2f}"
    else:
        sarima_display_price = "N/A"

    # Prophet Prediction
    future = prophet_model.make_future_dataframe(periods=30)
    forecast_prophet = prophet_model.predict(future)
    prophet_forecast_df = forecast_prophet.set_index("ds")["yhat"]

    if date in prophet_forecast_df.index:
        prophet_predicted_price = prophet_forecast_df.loc[date]
        prophet_display_price = f"${prophet_predicted_price:.2f}"
    else:
        prophet_display_price = "N/A"
    
    # Display Predictions
    if sarima_display_price != "N/A":
        st.success(f"SARIMA Predicted Price on {date_input}: {sarima_display_price}")
    else:
        st.warning(f"SARIMA Prediction not available for {date_input}.")

    if prophet_display_price != "N/A":
        st.success(f"Prophet Predicted Price on {date_input}: {prophet_display_price}")
    else:
        st.warning(f"Prophet Prediction not available for {date_input}.")

    # Plot predictions
    st.subheader("Forecast Visualization")
    fig, ax = plt.subplots()
    ax.plot(sarima_forecast_df.index, sarima_forecast_df["Forecasted Price"], label="SARIMA Forecast", color="red")
    ax.plot(prophet_forecast_df.index, prophet_forecast_df, label="Prophet Forecast", color="blue")
    ax.legend()
    st.pyplot(fig)
