import streamlit as st
from utils.localisation import get_localised_text

language = st.session_state["language"]
text = get_localised_text(language)

st.title(text("HOME_TITLE"))
st.write(text("HOME_DESC"))

st.info("""
🧭 Gunakan menu di sebelah kiri untuk berpindah halaman:
- Teori Fotosintesis  
- Simulasi Interaktif  
- Kuis Evaluasi  
""")
