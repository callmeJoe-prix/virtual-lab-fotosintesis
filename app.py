import streamlit as st

from utils.localisation import get_localised_text
from utils.icons import icons

# Singleton rule
st.set_page_config(layout="wide", page_title="Virtual Lab Fotosintesis")

# Default session states
st.session_state.setdefault("language", "Indonesia")
st.session_state.setdefault("version", "Default")
st.session_state.setdefault("show_video_transcripts", False)

language = st.session_state["language"]
version = st.session_state["version"]
text = get_localised_text(language)

# Navigation Setup
pg = st.navigation(
    [
        st.Page(
            "routes/home.py",
            title=text("PAGE_HOME"),
            icon=icons["home"],
        ),
        st.Page(
            "routes/teori.py",
            title=text("PAGE_TEORI"),
            icon=icons["book"],
        ),
        st.Page(
            "routes/simulasi.py",
            title=text("PAGE_SIMULASI"),
            icon=icons["lab"],
        ),
        st.Page(
            "routes/kuis.py",
            title=text("PAGE_KUIS"),
            icon=icons["quiz"],
        ),
    ]
)

# Sidebar
with st.sidebar:

    st.write(f"## ⚙ Pengaturan")

    # Language selector
    languages = {
        "Indonesia": "🇮🇩 Bahasa Indonesia",
        "English": "🇬🇧 English",
    }
    lang_idx = list(languages.keys()).index(language)

    st.selectbox(
        label="🌍 Bahasa",
        index=lang_idx,
        options=list(languages.keys()),
        key="_language",
        on_change=lambda: st.session_state.update({"language": st.session_state["_language"]}),
        format_func=languages.get,
    )

    # Video transcripts toggle
    st.checkbox(
        label="Tampilkan Transkrip Video",
        key="_show_video_transcripts",
        on_change=lambda: st.session_state.update(
            {"show_video_transcripts": st.session_state["_show_video_transcripts"]}
        ),
    )

# Run selected page
pg.run()
