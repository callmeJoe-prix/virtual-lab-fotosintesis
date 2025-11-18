import streamlit as st
import pandas as pd
from modules.simulator import PhotosynthesisSimulator
from modules.utils import load_parameters
from modules.graph import plot_light_curve, plot_o2_output

st.set_page_config(
    page_title="Virtual Photosynthesis Lab",
    layout="wide",
    page_icon="🌱"
)

st.title("🌱 Virtual Photosynthesis Laboratory – Advanced Version")
st.write("Simulasi fotosintesis berbasis parameter fisiologi tanaman.")

# Sidebar parameters
st.sidebar.header("Input Parameter")

light = st.sidebar.slider("Intensitas Cahaya (µmol m⁻² s⁻¹)", 0, 2000, 500)
co2 = st.sidebar.slider("Konsentrasi CO₂ (ppm)", 100, 2000, 400)
temp = st.sidebar.slider("Suhu (°C)", 5, 45, 25)

# Load parameters
params = load_parameters("data/parameters.json")
sim = PhotosynthesisSimulator(params)

# Run simulation
curve = sim.generate_light_curve()
o2 = sim.calculate_o2_production(light, temp, co2)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Kurva Respon Cahaya")
    st.pyplot(plot_light_curve(curve))

with col2:
    st.subheader("Produksi Oksigen")
    st.metric("O₂ (mg/L/jam)", f"{o2:.2f}")
    st.pyplot(plot_o2_output(light, o2))

# Download button
df = pd.DataFrame({"Intensity": [light], "O2": [o2]})
st.download_button("Download hasil simulasi (CSV)", df.to_csv(), "result.csv")

st.info(
    "Aplikasi ini dikembangkan untuk mendukung pembelajaran fotosintesis "
    "serta laporan aktualisasi CPNS."
)
