import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score  
import matplotlib.pyplot as plt

def linearRegression(data_dict, prediction_range):
    # Konversi data dict ke DataFrame
    data = pd.DataFrame.from_dict(data_dict)

    # Konversi kolom tanggal dan total item
    data['Tanggal Kunjungan'] = pd.to_datetime(data['Tanggal Kunjungan'], errors='coerce')
    data['Total Item'] = pd.to_numeric(data['Total Item'], errors='coerce')

    # Agregasi berdasarkan tanggal
    daily_visits = data.groupby('Tanggal Kunjungan')['Total Item'].sum().reset_index()
    daily_visits = daily_visits.rename(columns={'Tanggal Kunjungan': 'Date', 'Total Item': 'Total_Visits'})

    # Tambahkan kolom hari sebagai variabel independen
    daily_visits['Day'] = (daily_visits['Date'] - daily_visits['Date'].min()).dt.days

    # Pisahkan data untuk pelatihan
    X = daily_visits[['Day']]
    y = daily_visits['Total_Visits']

    # Buat model regresi linear
    model = LinearRegression()
    model.fit(X, y)

    # Prediksi data masa depan (7 hari ke depan)
    future_days = prediction_range
    last_day = daily_visits['Day'].max()
    future_X = np.array(range(last_day + 1, last_day + 1 + future_days)).reshape(-1, 1)
    future_predictions = model.predict(future_X)

    # Buat DataFrame untuk hasil prediksi
    future_dates = pd.date_range(daily_visits['Date'].iloc[-1] + pd.Timedelta(days=1), periods=future_days)
    forecast_df = pd.DataFrame({'Date': future_dates, 'Forecast': future_predictions})

    # Tampilkan data prediksi
    st.write(forecast_df)

    # Visualisasi hasil
    st.write("### Data Aktual dan Hasil Linear Regression")
    plt.figure(figsize=(10, 6))
    plt.plot(daily_visits['Date'], daily_visits['Total_Visits'], label='Actual Data', color='blue')
    plt.plot(forecast_df['Date'], forecast_df['Forecast'], label='Forecast', color='red', linestyle='--')
    plt.xlabel("Date")
    plt.ylabel("Total Visits")
    plt.title("Linear Regression Forecasting")
    plt.legend()
    plt.grid()
    st.pyplot(plt)

    # Evaluasi model regresi linear
    y_pred = model.predict(X)
    mae = mean_absolute_error(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    st.write(f"### Evaluasi Model Regresi Linear")
    st.write(f"Mean Absolute Error (MAE): {mae}")
    st.write(f"Mean Squared Error (MSE): {mse}")
    st.write(f"R^2 Score: {r2}")

    return forecast_df
