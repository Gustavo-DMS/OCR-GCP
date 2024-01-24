import mysql.connector
from datetime import datetime
import streamlit as st

@st.cache_data
def insercao_banco(resultado,paciente,dispositivo):
    try:
        if dispositivo == "Termômetro":
            id_Dispositivo = 1
        elif dispositivo == "Balança":
            id_Dispositivo = 2
        elif dispositivo == "Medidor de pressão":
            id_Dispositivo = 3
        else:
            return "Dispositivo não encontrado"
        mydb = mysql.connector.connect(
          host="us-imm-web538.main-hosting.eu",
          user="u664201219_ztbIa",
          password="OcrDiag@2bd",
          database="u664201219_3H9aE",
        )
        data = datetime.now()
        data.strftime('%Y-%m-%d %H:%M:%S')
        resultado = ",".join([str(x) for x in resultado])
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO resultado_extracao (paciente_id_paciente,tipo_dispositivo_id_tipo_dispositivo,hora_extracao,resultado_extraido) VALUES (%s,%s,%s,%s)",(str(paciente),str(id_Dispositivo),data,resultado))
        mydb.commit()
        mycursor.close()
        mydb.close()
        return "Dados inseridos com sucesso"
    except Exception as e:
        return e
