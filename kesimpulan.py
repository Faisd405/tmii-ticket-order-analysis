import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

def kesimpulan(forecastingData):
   # Evaluasi hasil analisis
   st.write("### Kesimpulan Hasil Analisis")
   st.write("""
   1. **ARIMA** cocok digunakan untuk data deret waktu dengan pola autokorelasi yang kuat. 
      Hasil prediksinya mampu menangkap tren data historis dengan baik.
   2. **Mean Absolute Error (MAE)** adalah metrik evaluasi yang paling sesuai untuk data deret waktu,
      karena memberikan informasi tentang seberapa akurat model dalam memprediksi data aktual.
   3. **Mean Squared Error (MSE)** memberikan informasi tentang seberapa besar kesalahan prediksi model.
   4. **R^2 Score** memberikan informasi tentang seberapa baik model dalam menjelaskan variasi data aktual.
   5. **Forecasting** dapat memberikan wawasan prediktif untuk membantu pengambilan keputusan operasional.
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