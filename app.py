import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# Load model
model = load_model('model.h5')

st.title('Prediksi Harga Mobil')

# Input form
fitur1 = st.number_input('Fitur 1')
fitur2 = st.number_input('Fitur 2')
fitur3 = st.number_input('Fitur 3')
fitur4 = st.number_input('Fitur 4')
fitur5 = st.number_input('Fitur 5')

if st.button('Prediksi'):
    input_data = np.array([[fitur1, fitur2, fitur3, fitur4, fitur5]])
    hasil = model.predict(input_data)[0][0]
    st.success(f'Perkiraan harga mobil: Rp {hasil:,.2f}')
