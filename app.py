import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Fungsi Simulasi Logika Fotosintesis ---
def calculate_photosynthesis_rate(light, co2):
    """
    Menghitung laju fotosintesis berdasarkan dua faktor pembatas.
    Laju ditentukan oleh faktor yang nilainya paling rendah (Hukum Liebig).
    
    Args:
        light (float): Nilai intensitas cahaya (0-100).
        co2 (float): Nilai konsentrasi CO2 (0-100).
        
    Returns:
        tuple: (rate, oxygen_production, glucose_production)
    """
    
    # Faktor Pembatas Utama (Minimum)
    limiting_factor = min(light, co2)
    
    # Laju Fotosintesis (Skala 0-100)
    # Faktor dasar 0.8 untuk menjaga agar hasil tidak selalu 100
    base_rate = limiting_factor * 0.8 
    
    # Asumsi: Kecepatan saturasi terjadi setelah faktor pembatas mencapai 80
    if limiting_factor > 80:
        rate = 80 + (limiting_factor - 80) * 0.2  # Kenaikan melambat (Saturasi)
    else:
        rate = base_rate
        
    # Produksi Hasil (Unit Relatif)
    # Reaksi Fotosintesis: CO2 + H2O (+ Cahaya) -> C6H12O6 + O2
    # Kita asumsikan Oksigen (O2) adalah produk utama yang diukur, dan Glukosa (C6H12O6) sebagai produk akhir.
    oxygen_production = rate * 1.2 # Oksigen biasanya lebih banyak dari Glukosa
    glucose_production = rate * 0.9 # Glukosa sebagai produk akhir
    
    # Batasi hasil di 100
    oxygen_production = min(100, oxygen_production)
    glucose_production = min(100, glucose_production)
    
    # Laju total dibulatkan
    rate = min(100, rate)
    
    return rate, oxygen_production, glucose_production


# --- 2. Streamlit App Interface ---

# Konfigurasi Halaman
st.set_page_config(
    page_title="Simulasi Fotosintesis",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌱 Simulasi Laju Fotosintesis")
st.markdown("Eksplorasi hubungan antara intensitas cahaya dan konsentrasi $\text{CO}_2$ terhadap laju produksi oksigen dan glukosa.")

# --- Bagian Sidebar untuk Input ---
with st.sidebar:
    st.header("🔬 Faktor Pembatas")
    
    # Slider untuk Intensitas Cahaya
    light_intensity = st.slider(
        'Intensitas Cahaya (Unit Relatif)', 
        min_value=0, 
        max_value=100, 
        value=70, 
        step=5,
        help="Energi yang dibutuhkan untuk Reaksi Terang."
    )
    
    # Slider untuk Konsentrasi CO2
    co2_concentration = st.slider(
        'Konsentrasi $\\text{CO}_2$ (Unit Relatif)', 
        min_value=0, 
        max_value=100, 
        value=50, 
        step=5,
        help="Bahan baku yang dibutuhkan untuk Siklus Calvin (Reaksi Gelap)."
    )
    
    st.markdown("---")
    st.caption("Ubah parameter dan hasil akan diperbarui secara otomatis.")


# --- 3. Hitung dan Tampilkan Hasil ---

# Hitung hasil simulasi
rate, oxygen, glucose = calculate_photosynthesis_rate(light_intensity, co2_concentration)

# Tentukan Faktor Pembatas
limiting_factor_name = ""
if light_intensity < co2_concentration:
    limiting_factor_name = "Intensitas Cahaya"
    message_type = st.error
    
elif co2_concentration < light_intensity:
    limiting_factor_name = "Konsentrasi CO₂"
    message_type = st.error
    
else:
    limiting_factor_name = "Keseimbangan Optimal"
    message_type = st.info
    
# Tampilkan Hasil Utama
st.subheader("Laju Reaksi dan Produk")

col_rate, col_o2, col_glukosa = st.columns(3)

with col_rate:
    # Laju Reaksi
    st.metric(label="Laju Fotosintesis Total", value=f"{rate:.2f} Unit/Jam", delta=None)

with col_o2:
    # Produksi Oksigen
    st.metric(label="Produksi Oksigen ($\text{O}_2$)", value=f"{oxygen:.2f} Unit", delta=None)

with col_glukosa:
    # Produksi Glukosa
    st.metric(label="Produksi Glukosa ($\text{C}_6\text{H}_{12}\text{O}_6$)", value=f"{glucose:.2f} Unit", delta=None)

st.markdown("---")

# --- 4. Tampilkan Analisis dan Grafik ---

st.subheader("Analisis Faktor Pembatas")

message_type(
    f"Faktor yang paling membatasi laju fotosintesis saat ini adalah **{limiting_factor_name}** (Nilai: {min(light_intensity, co2_concentration)})."
)

st.markdown("""
<style>
    .stAlert {
        padding: 1rem;
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)


# Data untuk Grafik
data = pd.DataFrame({
    'Faktor': ['Cahaya', 'CO₂'],
    'Nilai Input': [light_intensity, co2_concentration]
})

# Grafik Batang Sederhana untuk Perbandingan Input
st.subheader("Perbandingan Faktor Input")
fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(data['Faktor'], data['Nilai Input'], color=['#FFC300', '#2E86C1'])
ax.set_ylim(0, 100)
ax.set_ylabel('Unit Relatif')
ax.set_title('Keseimbangan Faktor Pembatas')

# Tambahkan label nilai di atas batang
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 2, f"{int(yval)}", ha='center', va='bottom')

st.pyplot(fig)

st.markdown("---")
st.caption("Berdasarkan **Hukum Liebig**, laju pertumbuhan (dalam hal ini, fotosintesis) ditentukan oleh sumber daya yang paling langka, meskipun sumber daya lainnya melimpah.")
