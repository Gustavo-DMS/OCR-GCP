import streamlit as st

st.title("Bem vindo ao projeto de OCR em dispositivos de diagnóstico domiciliar")
st.write("Esse projeto tem como objetivo reunir os recursos tecnologicos disponíveis para digitalizar, classificar e disponibilizar ao médico os dados obtidos de forma remota fotgrafados por smartphones, a partir de aparelhos diagnósticos domiciliares que possuem display digital.")
st.write("Abaixo estão as páginas disponíveis:")
st.write("1. Página do médico: Nessa página o médico poderá verificar os dados extraídos pelo paciente.")
if st.button("Página do médico"):
    st.switch_page("pages/Médico.py")
st.write("2. Página do paciente: Nessa página o paciente poderá enviar uma foto do aparelho diagnóstico e verificar se os dados extraídos estão corretos.")
if st.button("Página do paciente"):
    st.switch_page("pages/Paciente.py")


