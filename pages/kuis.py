import streamlit as st

st.title("📝 Kuis Fotosintesis")

questions = {
    "Apa produk utama reaksi terang?": ["ATP dan NADPH", "Glukosa", "CO₂", "Air"],
    "Dimana reaksi gelap terjadi?": ["Stroma kloroplas", "Tilakoid", "Sitoplasma", "Nukleus"],
    "Apa faktor yang meningkatkan laju fotosintesis?": ["Cahaya", "Nitrogen", "Protein hewani", "Tekanan tanah"]
}

score = 0
for q, options in questions.items():
    answer = st.radio(q, options, key=q)
    if answer == options[0]:
        score += 1

if st.button("Lihat Hasil"):
    st.success(f"Nilai Anda: {score} / {len(questions)}")
