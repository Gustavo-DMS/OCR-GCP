import streamlit as st

def mostrar_extracao(extracao,equipamento):
    if(extracao[1] == equipamento):
        st.write("Extração realizada em:",extracao[0])
        resultado = extracao[2].split(",")
        if extracao[1] == 1:
            st.write("Tipo de dispositivo: Termômetro")
            st.write("Temperatura do paciente:",resultado[0])
            st.write("Parecer preliminar do paciente: ",resultado[1])
        elif extracao[1] == 2:
            st.write("Tipo de dispositivo: Balança")
            st.write("Peso do paciente: ",resultado[0])
            st.write("Altura do paciente: ",resultado[1])
            st.write("Parecer preliminar do paciente: ",resultado[2])
        elif extracao[1] == 3:
            st.write("Tipo de dispositivo: Medidor de pressão")
            st.write("Pressão sistólica do paciente: ",resultado[0])
            st.write("Pressão diastólica do paciente: ",resultado[1])
            st.write("Parecer preliminar do paciente: ",resultado[2])

        st.write("___________________________________________________________")
