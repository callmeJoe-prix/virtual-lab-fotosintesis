import streamlit as st
import numpy as np


st.title("📊 Simulasi Interaktif Fotosintesis")
st.markdown("Sesuaikan parameter di bawah untuk melihat perubahan laju fotosintesis.")


# sliders
light = st.slider("Intensitas Cahaya", 0, 100, 50)
co2 = st.slider("Konsentrasi CO₂", 0, 1000, 400)
temp = st.slider("Suhu (°C)", 0, 50, 25)


# simple model
def photosynthesis_rate(light, co2, temp):
temp_factor = np.exp(-((temp-25)**2)/50)
return (light/100) * (co2/1000) * temp_factor * 100


rate = photosynthesis_rate(light, co2, temp)


st.metric("Laju Fotosintesis (model sederhana)", f"{rate:.2f} unit")


st.progress(min(1.0, rate/100))
