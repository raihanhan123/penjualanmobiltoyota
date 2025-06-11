from flask import Flask, render_template, request
import numpy as np


app = Flask(__name__)

# Muat model yang telah dilatih (pastikan file model.h5 ada di folder yang sama)
model = load_model('model.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ambil nilai dari form input (ubah sesuai jumlah fitur Anda)
        fitur1 = float(request.form['fitur1'])
        fitur2 = float(request.form['fitur2'])
        fitur3 = float(request.form['fitur3'])
        fitur4 = float(request.form['fitur4'])
        fitur5 = float(request.form['fitur5'])

        # Gabungkan menjadi array numpy
        input_data = np.array([[fitur1, fitur2, fitur3, fitur4, fitur5]])

        # Prediksi
        hasil_prediksi = model.predict(input_data)[0][0]

        return render_template('index.html', prediction_text=f'Perkiraan harga mobil: Rp {hasil_prediksi:,.2f}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
