import streamlit as st
import numpy as np

# Fungsi Utama untuk Logika Simulasi Reaksi Terang
def simulasikan_reaksi_terang(intensitas_cahaya, ketersediaan_air):
    """
    Mensimulasikan produksi ATP dan NADPH berdasarkan intensitas cahaya dan air.
    (Ini adalah model penyederhanaan untuk tujuan pendidikan)
    """
    
    # 1. Cahaya menentukan Batas Atas (Potensi Maksimal)
    # Semakin terang, semakin tinggi potensi produksi ATP/NADPH
    potensi_maksimal = intensitas_cahaya * 0.8
    
    # 2. Air membatasi proses fotolisis (pemecahan air)
    # Jika air kurang, produksi akan turun drastis, meskipun cahaya tinggi
    keterbatasan_air = ketersediaan_air * 0.01 
    
    # Produksi yang dihitung berdasarkan gabungan potensi dan batasan
    produksi_dasar = (potensi_maksimal + keterbatasan_air) / 2
    
    # Jika ketersediaan air sangat rendah, produksi akan sangat terhambat
    if ketersediaan_air < 30:
        produksi_dasar *= 0.2  # Pengurangan drastis

    # Hitung Hasil (Produk utama Reaksi Terang)
    # ATP dan NADPH dihasilkan dalam rasio tertentu, kita asumsikan ATP sedikit lebih banyak
    produksi_atp = produksi_dasar * np.random.uniform(0.9, 1.1)  # Tambahkan sedikit variasi acak
    produksi_nadph = produksi_dasar * np.random.uniform(0.7, 0.9) # Tambahkan sedikit variasi acak
    
    # Batasi hasil agar tidak melebihi 100
    produksi_atp = min(100, produksi_atp)
    produksi_nadph = min(100, produksi_nadph)

    return produksi_atp, produksi_nadph

# --- Streamlit App Interface ---

st.set_page_config(
    page_title="Simulasi Reaksi Terang",
    layout="wide"
)

st.title("💡 Virtual Lab: Reaksi Terang Fotosintesis")
st.markdown("Gunakan *slider* di bawah untuk mengatur kondisi lingkungan dan amati dampaknya pada hasil Reaksi Terang (ATP dan NADPH).")

# 1. Sidebar untuk Input (Kondisi Lingkungan)
with st.sidebar:
    st.header("⚙️ Atur Kondisi Lingkungan")
    
    # Slider untuk Intensitas Cahaya
    intensitas_cahaya = st.slider(
        'Intensitas Cahaya', 
        min_value=10, 
        max_value=100, 
        value=60, 
        step=10,
        help="Semakin tinggi, semakin banyak energi yang tersedia untuk pigmen."
    )
    
    # Slider untuk Ketersediaan Air
    ketersediaan_air = st.slider(
        'Ketersediaan Air (H₂O)', 
        min_value=10, 
        max_value=100, 
        value=70, 
        step=10,
        help="Air adalah donor elektron dalam fotolisis. Kekurangan air akan menghambat reaksi."
    )
    
    tombol_simulasi = st.button("Jalankan Simulasi")

# 2. Area Utama untuk Hasil
st.header("Hasil Praktikum")

if tombol_simulasi:
    # Panggil fungsi simulasi
    atp, nadph = simulasikan_reaksi_terang(intensitas_cahaya, ketersediaan_air)
    
    st.success("Simulasi Selesai! Berikut hasil reaksi terang di stroma kloroplas:")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="✅ Produksi ATP (Energi)", value=f"{atp:.2f} Unit", delta=None)
        
    with col2:
        st.metric(label="✅ Produksi NADPH (Pembawa Elektron)", value=f"{nadph:.2f} Unit", delta=None)

    st.subheader("Analisis Data")
    
    # Logika untuk menampilkan kesimpulan berdasarkan hasil
    if ketersediaan_air < 30 and intensitas_cahaya > 50:
        st.error("⚠️ Meskipun intensitas cahaya **tinggi**, produksi ATP dan NADPH **terhambat** karena **kekurangan air (fotolisis terganggu)**.")
        st.caption("Kesimpulan: Air merupakan faktor pembatas utama dalam kondisi ini.")
        
    elif intensitas_cahaya < 30 and ketersediaan_air > 70:
        st.warning("Meski ketersediaan air **tinggi**, produksi **rendah** karena **intensitas cahaya sangat kurang**.")
        st.caption("Kesimpulan: Cahaya merupakan faktor pembatas utama dalam kondisi ini.")
        
    elif atp > 80 and nadph > 70:
        st.balloons()
        st.info("🎉 Kondisi optimal! Intensitas cahaya dan ketersediaan air mencukupi, menghasilkan produk energi dan pembawa elektron yang tinggi.")
        
    st.markdown("---")
    st.caption("Catatan: Unit di sini adalah nilai relatif dari 0 hingga 100.")

else:
    st.info("Tekan tombol 'Jalankan Simulasi' di *sidebar* untuk melihat hasilnya.")