import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time

st.set_page_config(page_title="Virtual Lab Fotosintesis", layout="wide")

st.title("🌿 Virtual Lab Fotosintesis – Simulasi Fotosintesis Sederhana")
st.write("""
Praktikum ini mensimulasikan pengaruh **intensitas cahaya**, **konsentrasi CO₂**, 
**panjang gelombang cahaya**, dan **suhu** terhadap produksi oksigen (O₂).
""")

# Sidebar controls
st.sidebar.header("Kontrol Variabel")

intensity = st.sidebar.slider("Intensitas Cahaya (μmol/m²/s)", 0, 300, 150)
co2 = st.sidebar.slider("Konsentrasi CO₂ (ppm)", 200, 1200, 400)
temperature = st.sidebar.slider("Suhu (°C)", 10, 40, 25)
wavelength = st.sidebar.selectbox("Panjang Gelombang Cahaya", 
                                  ["Merah (650 nm)", "Biru (450 nm)", "Hijau (550 nm)"])

# Button
run = st.sidebar.button("🌱 Jalankan Simulasi")

# Simulation
if run:
    st.subheader("📊 Hasil Simulasi Produksi O₂")
    
    data = []
    progress = st.progress(0)
    placeholder_chart = st.empty()

    # Model simple photosynthesis rate
    for t in range(1, 11):
        base_o2 = intensity * 0.04 + (co2 / 1000) * 10  

        # wavelength effect
        if "Biru" in wavelength:
            wave_factor = 1.2
        elif "Merah" in wavelength:
            wave_factor = 1.0
        else:
            wave_factor = 0.5

        temp_factor = np.exp(-(temperature - 25)**2 / 50)

        o2 = base_o2 * wave_factor * temp_factor
        o2 += np.random.uniform(-1, 1)

        data.append({"Waktu (s)": t, "Oksigen (O₂)": o2})

        # animate output
        df_temp = pd.DataFrame(data)
        chart = alt.Chart(df_temp).mark_line(point=True).encode(
            x="Waktu (s)",
            y="Oksigen (O₂)"
        )
        placeholder_chart.altair_chart(chart, use_container_width=True)

        progress.progress(t / 10)
        time.sleep(0.3)

    st.success("Simulasi selesai!")

    df = pd.DataFrame(data)
    st.dataframe(df)

    avg_o2 = df["Oksigen (O₂)"].mean()
    st.info(f"**Rata-rata produksi O₂: {avg_o2:.2f} unit**")

    # Download CSV
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Unduh Data CSV", csv, "hasil_fotosintesis.csv")

    # Reflection
    st.subheader("🧠 Refleksi Pembelajaran")
    reflection = st.text_area("Tuliskan jawaban refleksi Anda di sini:")

    if st.button("📄 Download Refleksi"):
        st.download_button("Klik untuk Unduh", reflection, "refleksi_fotosintesis.txt")
