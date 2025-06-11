import streamlit as st
import numpy as np
import tensorflow as tf

# Coba load model (pastikan model.h5 ada di direktori yang sama)
try:
    model = tf.keras.models.load_model('model.h5')
except Exception as e:
    st.error(f"Gagal memuat model: {e}")
    st.stop()

# Judul
st.title("Prediksi Harga Mobil Toyota")

# Deskripsi
st.write("Masukkan fitur-fitur berikut untuk memprediksi harga mobil:")

# Input pengguna
fitur1 = st.number_input("Fitur 1", step=0.1)
fitur2 = st.number_input("Fitur 2", step=0.1)
fitur3 = st.number_input("Fitur 3", step=0.1)
fitur4 = st.number_input("Fitur 4", step=0.1)
fitur5 = st.number_input("Fitur 5", step=0.1)

# Tombol prediksi
if st.button("Prediksi"):
    try:
        input_data = np.array([[fitur1, fitur2, fitur3, fitur4, fitur5]])
        hasil = model.predict(input_data)[0][0]
        st.success(f"Perkiraan harga mobil: Rp {hasil:,.2f}")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat prediksi: {e}")
