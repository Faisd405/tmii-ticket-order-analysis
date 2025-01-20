import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score  

def forecasting(data_dict, prediction_range):
    # Konversi data dict ke DataFrame
    data = pd.DataFrame.from_dict(data_dict)
    
    # Konversi kolom tanggal
    data['Tanggal Kunjungan'] = pd.to_datetime(data['Tanggal Kunjungan'], errors='coerce')
    data['Total Item'] = pd.to_numeric(data['Total Item'], errors='coerce')
    
    # Agregasi berdasarkan tanggal
    daily_visits = data.groupby('Tanggal Kunjungan')['Total Item'].sum().reset_index()
    daily_visits = daily_visits.rename(columns={'Tanggal Kunjungan': 'Date', 'Total Item': 'Total_Visits'})
    
    # Model Exponential Smoothing
    daily_visits = daily_visits.sort_values(by='Date')  # Pastikan data terurut
    model = ARIMA(daily_visits['Total_Visits'], order=(5, 1, 0))
    arima_result = model.fit()

    # 4. Prediksi jumlah kunjungan (misalnya, 7 hari ke depan)
    forecast = arima_result.get_forecast(steps=prediction_range)
    forecast_index = pd.date_range(daily_visits['Date'].iloc[-1] + pd.Timedelta(days=1), periods=prediction_range)

    # Data prediksi
    forecast_df = pd.DataFrame({
        'Date': forecast_index,
        'Forecast': forecast.predicted_mean
    })

    # Tampilkan data prediksi
    st.write(forecast_df)
    
    # Visualisasi
    st.write("### Data Aktual dan Hasil Forecasting")
    plt.figure(figsize=(10, 6))
    plt.plot(daily_visits['Date'], daily_visits['Total_Visits'], label='Actual', color='blue')
    plt.plot(forecast_df['Date'], forecast_df['Forecast'], label='Forecast', color='red', linestyle='--')
    plt.title('ARIMA Forecasting')
    plt.xlabel('Date')
    plt.ylabel('Total Visits')
    plt.legend()
    plt.grid()
    st.pyplot(plt)

    # Evaluasi model ARIMA
    actual = daily_visits['Total_Visits'][-len(forecast_df):]
    mae = mean_absolute_error(actual, forecast_df['Forecast'])
    mse = mean_squared_error(actual, forecast_df['Forecast'])
    r2 = r2_score(actual, forecast_df['Forecast'])
    st.write(f"### Evaluasi Model ARIMA")
    st.write(f"Mean Absolute Error (MAE): {mae}")
    st.write(f"Mean Squared Error (MSE): {mse}")
    st.write(f"R^2 Score: {r2}")

    return forecast_df
