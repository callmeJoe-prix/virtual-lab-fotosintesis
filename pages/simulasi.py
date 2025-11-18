import streamlit as st
import pandas as pd
from modules.simulator import PhotosynthesisSimulator
from modules.utils import load_parameters
from modules.graph import plot_light_curve, plot_o2_output

st.title("🔬 Simulasi Fotosintesis Interaktif")

light = st.slider("Intensitas Cahaya", 0, 2000, 500)
temp = st.slider("Suhu (°C)", 5, 45, 25)
co2 = st.slider("CO₂ (ppm)", 100, 2000, 400)

params = load_parameters("data/parameters.json")
sim = PhotosynthesisSimulator(params)

curve = sim.generate_light_curve()
o2 = sim.calculate_o2_production(light, temp, co2)

st.subheader("Kurva Respon Cahaya")
st.pyplot(plot_light_curve(curve))

st.subheader("Produksi Oksigen")
st.metric("O₂ (mg/L/jam)", f"{o2:.2f}")
st.pyplot(plot_o2_output(light, o2))

df = pd.DataFrame({"Cahaya": [light], "O2": [o2]})
st.download_button("Download CSV", df.to_csv(), "hasil.csv")
