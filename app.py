import streamlit as st
from utils import get_localised_text, icons


st.set_page_config(layout="wide")


st.session_state.setdefault("language", "English")
text = get_localised_text("4Bio", st.session_state["language"])


pg = st.navigation([
st.Page("pages/1_pendahuluan.py", title="Pendahuluan", icon=icons["house"]),
st.Page("pages/2_teori.py", title="Teori Fotosintesis", icon=icons["books"]),
st.Page("pages/3_simulasi.py", title="Simulasi Interaktif", icon=icons["bar_chart"]),
st.Page("pages/4_kuis.py", title="Kuis", icon=icons["chart_with_upwards_trend"]),
])


with st.sidebar:
st.write("## Pengaturan :gear:")
st.selectbox("Bahasa", ["English", "Indonesian"], key="language")


pg.run()
