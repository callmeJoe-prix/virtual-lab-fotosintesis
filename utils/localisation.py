def get_localised_text(language):
    text_id = {
        "PAGE_HOME": "Pendahuluan",
        "PAGE_TEORI": "Teori Fotosintesis",
        "PAGE_SIMULASI": "Simulasi Interaktif",
        "PAGE_KUIS": "Kuis Evaluasi",
        "HOME_TITLE": "Selamat Datang di Virtual Lab Fotosintesis",
        "HOME_DESC": """
Laboratorium virtual ini dirancang untuk membantu mahasiswa memahami 
proses fotosintesis dengan media interaktif, simulasi, dan evaluasi.
""",
    }

    text_en = {
        "PAGE_HOME": "Introduction",
        "PAGE_TEORI": "Photosynthesis Theory",
        "PAGE_SIMULASI": "Interactive Simulation",
        "PAGE_KUIS": "Quiz",
        "HOME_TITLE": "Welcome to the Virtual Photosynthesis Lab",
        "HOME_DESC": """
This virtual laboratory is designed to help students understand 
the process of photosynthesis using interactive pages, simulations, and quizzes.
""",
    }

    if language == "English":
        return lambda key: text_en.get(key, key)
    return lambda key: text_id.get(key, key)
