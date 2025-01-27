import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def dataset(data_dict):
    data = pd.DataFrame.from_dict(data_dict)

    st.write("### Data Mentah")
    st.write(data)

    data['Tanggal Kunjungan'] = pd.to_datetime(data['Tanggal Kunjungan'], errors='coerce')
    data['Total Item'] = pd.to_numeric(data['Total Item'], errors='coerce')
    daily_visits = data.groupby('Tanggal Kunjungan').sum().reset_index()
    daily_visits = daily_visits.rename(columns={'Tanggal Kunjungan': 'Date'})

    st.write("### Data Tiket Kunjungan per Hari")
    daily_visits = daily_visits.drop(columns=['No Order', 'Nama Pembeli', 'Tanggal Order', 'Aktivitas', 'Nama Item', 'day_of_week'])

    st.write(daily_visits)

    plt.figure(figsize=(10, 6))
    plt.plot(daily_visits['Date'], daily_visits['Total Item'], color='blue')
    plt.xlabel("Date")
    plt.ylabel("Total Visits")
    plt.title("Data Tiket Kunjungan")
    plt.grid()
    st.pyplot(plt)

