import streamlit as st
from mostrar_resultado import mostrar_extracao
import mysql.connector

@st.cache_data
def get_medicos():
    mydb = mysql.connector.connect(
    host="us-imm-web538.main-hosting.eu",
    user="u664201219_ztbIa",
    password="OcrDiag@2bd",
    database="u664201219_3H9aE",)
    mycursor = mydb.cursor()
    response = mycursor.execute("SELECT id_responsavel_medico, nome FROM responsavel_medico")
    response = mycursor.fetchall()
    return response

@st.cache_data
def get_medicos_pacientes(id_medico):
    mydb = mysql.connector.connect(
    host="us-imm-web538.main-hosting.eu",
    user="u664201219_ztbIa",
    password="OcrDiag@2bd",
    database="u664201219_3H9aE",)
    mycursor = mydb.cursor()
    response = mycursor.execute("SELECT paciente.nome, paciente.id_paciente FROM paciente LEFT JOIN paciente_has_responsavel_paciente ON paciente_has_responsavel_paciente.paciente_id_paciente = paciente.id_paciente LEFT JOIN responsavel_medico ON responsavel_medico.id_responsavel_medico = paciente_has_responsavel_paciente.responsavel_medico_id_responsavel_medico WHERE responsavel_medico.id_responsavel_medico = %s", (id_medico,))
    response = mycursor.fetchall()
    return response

@st.cache_data
def get_extracoes(id_paciente):
    mydb = mysql.connector.connect(
    host="us-imm-web538.main-hosting.eu",
    user="u664201219_ztbIa",
    password="OcrDiag@2bd",
    database="u664201219_3H9aE",)
    mycursor = mydb.cursor()
    response = mycursor.execute("SELECT re.hora_extracao,re.tipo_dispositivo_id_tipo_dispositivo, re.resultado_extraido FROM resultado_extracao as re WHERE re.paciente_id_paciente = %s", (id_paciente,))
    response = mycursor.fetchall()
    return response

st.title("OCR em dispositivos diagnósticos")
st.header("Página do médico")
left_column, right_column = st.columns(2)
if left_column.button("Página do médico"):
    st.switch_page("pages/Médico.py")
if right_column.button("Página do paciente"):
    st.switch_page("pages/Paciente.py")

medicos = get_medicos()
medico = st.selectbox("Selecione o médico", [medico[1] for medico in medicos])
id_medico = 0
if medico:
    id_medico = [x[0] for x in medicos if x[1] == medico][0]
pacientes = get_medicos_pacientes(id_medico)
paciente = st.selectbox("Selecione o paciente", [paciente[0] for paciente in pacientes])
id_paciente = 0
if paciente:
    id_paciente = [x[1] for x in pacientes if x[0] == paciente][0]
extracoes = get_extracoes(id_paciente)
st.header("Extracoes de paciente")
dict_equipment = {"Termômetro":1,"Balança":2,"Medidor de pressão":3}
equipamento = st.selectbox("Selecione o equipamento", [x for x in dict_equipment])
for extracao in extracoes:
    if(equipamento):
        mostrar_extracao(extracao,dict_equipment.get(equipamento))



