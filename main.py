import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from forecasting import forecasting
from linear_regression import linearRegression
from dataset import dataset
from kesimpulan import kesimpulan
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score  

def get_data_from_document():  
    """
    Fase Pengumpulan Data:
    - Sumber: Goers
    - Jenis Data: Laporan Order Tiket Kunjungan
    - Periode: 1 Desember 2024 - 1 Januari 2025
    - Format: CSV
    """
    # Nama File: Laporan Order Tiket Kunjungan_2024-12-01-2025-01-01
    file_path = "Laporan Order Tiket Kunjungan_2024-12-01-2025-01-01.csv"

    # Load data dari file CSV
    data = pd.read_csv(file_path)
    return data.to_dict()

#==============================================================================
# BUSINESS UNDERSTANDING
#==============================================================================
# Tujuan:
# - Membuat model untuk memprediksi jumlah kunjungan harian berdasarkan data historis.
#
# Target:
# - Memberikan estimasi jumlah kunjungan untuk periode tertentu di masa depan.
# - Mendukung pengambilan keputusan operasional seperti alokasi sumber daya.
#==============================================================================
def main(): 
    st.set_page_config(
        page_title="Prediksi Data Tiket Kunjungan Goers",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Title
    st.title("Perbandingan Forecasting dan Regresi Linear pada Data pemesanan Tiket Kunjungan pada aplikasi Goers")

    # Introduction
    st.markdown("""
    ### Pendahuluan:
    - Aplikasi Goers menyediakan layanan pemesanan tiket kunjungan ke berbagai tempat wisata.
    - Data pemesanan tiket kunjungan disimpan dalam bentuk CSV.
    - Tujuan: Memprediksi jumlah kunjungan ke tempat wisata di masa depan.
            
    ### Langkah:
    1. **Pengumpulan Data**: Data pemesanan tiket kunjungan.
    2. **Preprocessing Data**: Konversi data ke DataFrame.
    3. **Forecasting**: Prediksi jumlah kunjungan menggunakan ARIMA.
    4. **Linear Regression**: Prediksi jumlah kunjungan menggunakan regresi linear.
    5. **Kesimpulan**: Perbandingan hasil prediksi.
    """)

    # Slider untuk rentang prediksi
    prediction_range = st.slider("Pilih jumlah hari untuk prediksi:", min_value=1, max_value=30, value=7)


    datasetTab, forecastingTab, linearTab, kesimpulanTab = st.tabs([
        "Data Tiket Kunjungan",
        "Time Series (Forecasting)", 
        "Regresi Linear",
        "Kesimpulan"
    ])

    data = get_data_from_document()

    # Generate data
    with datasetTab:
        st.header("Data Tiket Kunjungan")
        dataset(data)
    with forecastingTab:
        st.header("Time Series (Forecasting) with Arima")
        forecastingData = forecasting(data, prediction_range)
    with linearTab:
        st.header("Regresi Linear")
        linearRegressionData = linearRegression(data, prediction_range)
    with kesimpulanTab:
        st.header("Kesimpulan dan Hasil Analisis")
        kesimpulan(forecastingData, linearRegressionData)

        # forecastingData just Date and Forecast

if __name__ == "__main__":
    main()  
