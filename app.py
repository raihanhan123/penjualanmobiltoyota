import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# Judul Aplikasi
st.title("Prediksi Harga Mobil Toyota")

# Load model
model = load_model('model.h5')

# Input data dari pengguna
st.header("Masukkan Fitur Mobil:")
fitur1 = st.number_input("Fitur 1", step=0.1)
fitur2 = st.number_input("Fitur 2", step=0.1)
fitur3 = st.number_input("Fitur 3", step=0.1)
fitur4 = st.number_input("Fitur 4", step=0.1)
fitur5 = st.number_input("Fitur 5", step=0.1)

# Tombol prediksi
if st.button("Prediksi Harga"):
    try:
        input_data = np.array([[fitur1, fitur2, fitur3, fitur4, fitur5]])
        hasil_prediksi = model.predict(input_data)[0][0]
        st.success(f"Perkiraan harga mobil: Rp {hasil_prediksi:,.2f}")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {str(e)}")
