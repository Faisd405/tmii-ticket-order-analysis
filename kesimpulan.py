import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score  

def kesimpulan(forecastingData, linearRegressionData):
        st.write("### Perbandingan Hasil Forecasting dan Regresi Linear")

        # Gabungkan hasil prediksi ARIMA dan Regresi Linear
        forecastingData = forecastingData.set_index('Date')
        linearRegressionData = linearRegressionData.set_index('Date')
        combined_results = pd.concat([forecastingData, linearRegressionData], axis=1)
        combined_results.columns = ['ARIMA', 'Linear Regression']
        
        # Tampilkan hasil prediksi
        st.write("#### Hasil Prediksi:")
        st.dataframe(combined_results)

        # Visualisasi hasil prediksi
        st.write("#### Visualisasi Perbandingan Prediksi")
        plt.figure(figsize=(10, 6))
        plt.plot(combined_results.index, combined_results['ARIMA'], label='ARIMA', color='blue')
        plt.plot(combined_results.index, combined_results['Linear Regression'], label='Linear Regression', color='red', linestyle='--')
        plt.xlabel("Tanggal")
        plt.ylabel("Jumlah Kunjungan")
        plt.title("Perbandingan Hasil Prediksi ARIMA dan Regresi Linear")
        plt.legend()
        plt.grid()
        st.pyplot(plt)

        # Evaluasi hasil analisis
        st.write("### Kesimpulan Hasil Analisis")
        st.write("""
        1. **ARIMA** lebih cocok digunakan untuk data deret waktu dengan pola autokorelasi yang kuat. 
           Hasil prediksinya mampu menangkap tren data historis dengan baik.
        2. **Regresi Linear** lebih sederhana dan efektif jika pola hubungan antar variabel independen dan dependen mudah terlihat.
        3. Perbedaan hasil prediksi pada kedua model memberikan wawasan strategis untuk berbagai skenario perencanaan.
        """)

        # Tujuan dan Manfaat Hasil Analisis
        st.write("### Tujuan dan Manfaat Hasil Analisis untuk Provider IT")
        st.write("""
        **Tujuan**:
        - Memberikan wawasan prediktif mengenai jumlah kunjungan harian untuk mendukung pengambilan keputusan operasional.
        - Mengoptimalkan pengelolaan sumber daya IT, seperti alokasi server, bandwidth, atau kapasitas sistem.
        - Mendukung penyusunan strategi pemasaran berbasis data.

        **Manfaat**:
        1. **Prediksi Operasional**:
           - Provider IT dapat memprediksi kebutuhan infrastruktur sistem berdasarkan lonjakan kunjungan, terutama selama acara besar atau musim liburan.
        2. **Efisiensi Pengelolaan Sistem**:
           - Data prediksi dapat digunakan untuk menerapkan autoscaling pada infrastruktur cloud, menghemat biaya operasional.
        3. **Personalisasi Layanan**:
           - Dengan mengetahui pola kunjungan, sistem dapat merekomendasikan kategori tiket atau layanan tambahan secara proaktif.
        4. **Analisis Tren dan Musiman**:
           - Hasil analisis dapat digunakan untuk mendukung perencanaan strategis TMII, seperti promosi pada waktu tertentu.
        """)