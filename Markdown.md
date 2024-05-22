# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Perusahaan Edutech Jaya Jaya Institut menghadapi tantangan dalam mempertahankan siswa untuk menyelesaikan pendidikan mereka, yang terlihat dari tingginya tingkat dropout (keluarnya siswa sebelum lulus). Tingginya dropout dapat menyebabkan reputasi institusi menurun dan kehilangan potensi lulusan yang berkualitas. Tujuan dari proyek ini adalah untuk menganalisis faktor-faktor yang mempengaruhi dropout dan membuat model prediktif untuk mengidentifikasi siswa yang berisiko tinggi meninggalkan institusi.

## Permasalahan Bisnis
1. **Tingginya Tingkat Dropout:** Jaya Jaya Institut memiliki tingkat dropout yang tinggi. Jumlah siswa yang tidak menyelesaikan pendidikan mereka merupakan masalah serius yang dapat mempengaruhi reputasi dan kinerja institusi.

## Cakupan Proyek
Proyek ini mencakup beberapa aspek utama:
- **Analisis Data Siswa:** Memahami distribusi dan karakteristik data siswa.
- **Preprocessing Data:** Membersihkan dan mempersiapkan data untuk analisis lebih lanjut.
- **Modeling:** Membangun dan mengevaluasi model prediktif menggunakan algoritma Random Forest.
- **Visualisasi Data:** Membuat visualisasi untuk memahami pola dropout berdasarkan berbagai fitur siswa.

## Persiapan
**Sumber data:**
- Data siswa (data.csv) | Link : https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

**Setup environment:**
1. Buat virtual environment
python -m venv myenv

2. Aktifkan virtual environment
.\myenv\Scripts\activate

3. Install library dari requirements.txt
pip install -r requirements.txt

## Business Dashboard
Dashboard yang saya buat di metabase ini memberikan visualisasi mengenai distribusi dropout berdasarkan fitur seperti jumlah kursus semester pertama dan kedua. Visualisasi ini membantu dalam memahami pola dropout dan faktor-faktor yang mempengaruhinya.

## Conclusion
Dari analisis yang dilakukan, ditemukan bahwa faktor-faktor seperti jumlah kursus dan evaluasi pada semester pertama dan kedua, serta nilai kualifikasi sebelumnya dan nilai penerimaan memiliki pengaruh signifikan terhadap tingkat dropout. Model Random Forest yang dibangun menunjukkan kinerja yang baik dalam memprediksi siswa yang berisiko tinggi meninggalkan institusi, dengan akurasi sebesar 73%.

## Rekomendasi Action Items
Berikut beberapa rekomendasi action items yang dapat dilakukan perusahaan guna menyelesaikan permasalahan:

1. **Meningkatkan Kualitas Pengajar:** Korelasi positif yang kuat antara jumlah kursus yang diambil dan jumlah evaluasi pada kedua semester menunjukkan pentingnya kualitas pengajaran. Institusi dapat meningkatkan kualitas pengajar dan metode pengajaran untuk memastikan siswa memahami materi dengan baik dan siap menghadapi evaluasi.

2. **Memberikan Standarisasi pada Jumlah Kursus yang Diambil:** Jumlah kursus yang diambil pada semester pertama dan kedua memiliki korelasi positif yang kuat dengan jumlah kursus yang disetujui. Institusi dapat menetapkan standar minimum dan maksimum jumlah kursus yang harus diambil oleh setiap siswa per semester untuk memastikan beban akademik yang optimal dan mengurangi risiko dropout.

## Prediksi dan Penggunaan Model
1. **Pastikan Anda memiliki file berikut dalam satu folder:**
    - model.joblib
    - scaler.joblib
    - Script Python Streamlit (Streamlit.py)

2. **Buka terminal atau command prompt**
3. **Arahkan direktori ke folder yang berisi app.py, model.joblib, dan scaler.joblib.**
4. **Jalankan perintah berikut untuk memulai aplikasi Streamlit:**
    - streamlit run app.py
5. **Mengisi Nilai Input di Streamlit:**
Di halaman aplikasi, Anda akan melihat input form untuk memasukkan nilai pada enam kolom utama:
Jumlah kursus yang diambil pada Semester 1: Masukkan jumlah kursus yang diambil pada semester 1 (contoh: 5).
Jumlah evaluasi pada Semester 1: Masukkan jumlah evaluasi pada semester 1 (contoh: 3).
Jumlah kursus yang diambil pada Semester 2: Masukkan jumlah kursus yang diambil pada semester 2 (contoh: 5).
Jumlah evaluasi pada Semester 2: Masukkan jumlah evaluasi pada semester 2 (contoh: 3).
Nilai kualifikasi sebelumnya: Masukkan nilai kualifikasi sebelumnya (contoh: 80.5).
Nilai penerimaan: Masukkan nilai penerimaan (contoh: 75.0).

## Link Streamlit
- https://project-akhir-dicoding-wicak.streamlit.app/