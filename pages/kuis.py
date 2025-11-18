import streamlit as st


st.title("📈 Kuis Fotosintesis")


questions = [
{
"q": "Apa bahan utama fotosintesis?",
"options": ["Oksigen", "Karbon dioksida dan air", "Protein"],
"answer": 1,
},
{
"q": "Dimana fotosintesis terjadi?",
"options": ["Mitokondria", "Kloroplas", "Inti sel"],
"answer": 1,
}
]


score = 0
for i, q in enumerate(questions):
st.write(f"### {i+1}. {q['q']}")
choice = st.radio("Pilih jawaban:", q["options"], key=f"q{i}")
if choice == q["options"][q["answer"]]:
score += 1


st.write("---")
st.subheader(f"Skor Anda: {score} / {len(questions)}")
