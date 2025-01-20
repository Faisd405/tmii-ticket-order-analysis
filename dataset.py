import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def dataset(data_dict):
    # Konversi data dict ke DataFrame
    data = pd.DataFrame.from_dict(data_dict)

    # Table Original Data
    st.write(data)

    # Konversi kolom tanggal dan total item
    data['Tanggal Kunjungan'] = pd.to_datetime(data['Tanggal Kunjungan'], errors='coerce')
    data['Total Item'] = pd.to_numeric(data['Total Item'], errors='coerce')

    # Agregasi berdasarkan tanggal
    daily_visits = data.groupby('Tanggal Kunjungan')['Total Item'].sum().reset_index()
    daily_visits = daily_visits.rename(columns={'Tanggal Kunjungan': 'Date', 'Total Item': 'Total_Visits'})

    # Visualisasi data
    st.write("### Data Tiket Kunjungan")
    plt.figure(figsize=(10, 6))
    plt.plot(daily_visits['Date'], daily_visits['Total_Visits'], color='blue')
    plt.xlabel("Date")
    plt.ylabel("Total Visits")
    plt.title("Data Tiket Kunjungan")
    plt.grid()
    st.pyplot(plt)

