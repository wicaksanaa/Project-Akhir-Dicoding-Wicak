import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from joblib import load

# Memuat model, scaler, dan PCA yang telah disimpan
model_loaded = load('model_randomforest.joblib')
scaler = load('scaler.joblib')
pca = load('pca.joblib')

# Judul aplikasi
st.title('Prediksi Status Kelulusan Mahasiswa Baru')

# Input nilai untuk keenam kolom
curricular_units_1st_sem_enrolled = st.number_input('Jumlah kursus yang diambil pada Semester 1', min_value=0)
curricular_units_1st_sem_evaluations = st.number_input('Jumlah evaluasi pada Semester 1', min_value=0)
curricular_units_2nd_sem_enrolled = st.number_input('Jumlah kursus yang diambil pada Semester 2', min_value=0)
curricular_units_2nd_sem_evaluations = st.number_input('Jumlah evaluasi pada Semester 2', min_value=0)
previous_qualification_grade = st.number_input('Nilai kualifikasi sebelumnya', min_value=0.0, format="%.2f")
admission_grade = st.number_input('Nilai penerimaan', min_value=0.0, format="%.2f")

# Membuat DataFrame dari input pengguna
data_baru = pd.DataFrame({
    'Curricular_units_2nd_sem_enrolled': [curricular_units_2nd_sem_enrolled],
    'Curricular_units_2nd_sem_evaluations': [curricular_units_2nd_sem_evaluations],
    'Curricular_units_1st_sem_enrolled': [curricular_units_1st_sem_enrolled],
    'Curricular_units_1st_sem_evaluations': [curricular_units_1st_sem_evaluations],
    'Previous_qualification_grade': [previous_qualification_grade],
    'Admission_grade': [admission_grade]
})

# Prediksi hasil saat tombol ditekan
if st.button('Prediksi'):
    # Standarisasi fitur pada data baru
    data_baru_scaled = scaler.transform(data_baru)
    
    # Mengaplikasikan PCA pada data baru
    data_baru_pca = pca.transform(data_baru_scaled)
    
    # Memprediksi hasil untuk data baru
    prediksi_baru = model_loaded.predict(data_baru_pca)
    
    # Menampilkan hasil prediksi
    if prediksi_baru[0] == 0:
        st.write("Hasil Prediksi: Dropout")
    else:
        st.write("Hasil Prediksi: Graduate")
