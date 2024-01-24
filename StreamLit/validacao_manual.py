import streamlit as st

def validacao_manual(equipamento,resultado) -> list:
    resultado = []
    if(equipamento == 'Termômetro'):
        temp = st.text_input("Qual a temperatura?")
        resultado.append(temp)
        return resultado
    elif(equipamento == 'Balança'):
        peso = st.text_input("Qual o peso?")
        resultado.append(peso)
        return resultado
    elif(equipamento == 'Medidor de pressão'):
        pressao_sis = st.text_input("Qual a pressão sistólica?")
        pressao_dia= st.text_input("Qual a pressão diastólica?")
        resultado.append(pressao_sis)
        resultado.append(pressao_dia)
        return resultado
    else:
        st.text("Equipamento não reconhecido")
        return resultado

