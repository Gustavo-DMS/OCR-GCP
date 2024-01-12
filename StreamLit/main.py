import json
import base64
import streamlit as st
from google.cloud import vision
from PIL import ImageOps, Image
from verificacao_dados import verificar_dados
import mysql.connector


@st.cache_data
def get_users():
    mydb = mysql.connector.connect(
  host="us-imm-web538.main-hosting.eu",
  user="u664201219_ztbIa",
  password="OcrDiag@2bd",
  database="u664201219_3H9aE",
)
    mycursor = mydb.cursor()
    response = mycursor.execute("SELECT nome FROM paciente")
    response = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return response


@st.cache_data
def get_paciente_cuidador(paciente):
    mydb = mysql.connector.connect(
  host="us-imm-web538.main-hosting.eu",
  user="u664201219_ztbIa",
  password="OcrDiag@2bd",
  database="u664201219_3H9aE",
)
    mycursor = mydb.cursor()
    response = mycursor.execute("SELECT	cuidador_paciente.nome_cuidador FROM cuidador_paciente LEFT JOIN paciente_has_cuidador_paciente ON paciente_has_cuidador_paciente.cuidador_paciente_id_cuidador_paciente = cuidador_paciente.id_cuidador_paciente LEFT JOIN paciente ON paciente.id_paciente = paciente_has_cuidador_paciente.paciente_id_paciente WHERE paciente.nome LIKE %s", (paciente,))
    response = mycursor.fetchall()
    return response

@st.cache_data
def get_paciente_medico(paciente):
    mydb = mysql.connector.connect(
  host="us-imm-web538.main-hosting.eu",
  user="u664201219_ztbIa",
  password="OcrDiag@2bd",
  database="u664201219_3H9aE",
)
    mycursor = mydb.cursor()
    response = mycursor.execute("SELECT rm.nome FROM	responsavel_medico rm LEFT JOIN paciente_has_responsavel_paciente phrp ON phrp.responsavel_medico_id_responsavel_medico = rm.id_responsavel_medico LEFT JOIN paciente p ON p.id_paciente = phrp.paciente_id_paciente WHERE p.nome  LIKE  %s", (paciente,))
    response = mycursor.fetchall()
    return response

@st.cache_data
def get_annotations(img):
    encoded_image = base64.b64encode(img).decode()
    client = vision.ImageAnnotatorClient()
    response = client.annotate_image({
        'image':  {'content': f"{encoded_image}"},
        'features': [{'type_': vision.Feature.Type.TEXT_DETECTION}],
        })
    response_json = vision.AnnotateImageResponse.to_json(response)
    resultado_json = json.loads(response_json)
    return resultado_json

def is_float(string):
    if string.replace(".", "").replace(",","").isnumeric():
        return True
    else:
        return False

st.title("OCR em dispositivos diagnósticos")

equipamento = st.radio(
    "Qual o aparelho da imagem?",
    ["Termômetro", "Balança", "Medidor de pressão"],horizontal=True,index=None)

batimentos = False
altura = 0
paciente = get_users()
nome = st.selectbox("Nome do paciente:", [x[0] for x in paciente],index=None)
cuidador = st.selectbox("Nome do cuidador:", [x[0] for x in get_paciente_cuidador(nome)])
medico = st.selectbox("Nome do médico:", [x[0] for x in get_paciente_medico(nome)])
if equipamento == "Balança":
    altura = st.text_input("Altura do paciente:")
elif equipamento == "Medidor de pressão":
    batimentos = st.checkbox("Com batimentos cardíacos?")

imagem_upload = st.file_uploader("Adicione um arquivo", type=("png", "jpg"))

if imagem_upload is not None:
    imagem_orientada = Image.open(imagem_upload)
    imagem_orientada = ImageOps.exif_transpose(imagem_orientada)
    st.image(imagem_orientada, caption='Imagem enviada', use_column_width='auto', )

    bytes_data = imagem_upload.getvalue()
    resultado_json = get_annotations(bytes_data)
    st.write("Texto extraído da imagem:")
    resultado = []
    for x in resultado_json["textAnnotations"]:
        if(is_float(x["description"]) ):
            resultado.append(x["description"])

    if equipamento == "Balança":
        resultado.append(altura)
    for x in resultado:
        st.write(x)
    st.write("O restultado da extração acima está correto?")
    left_column, right_column = st.columns(2)
    botao_sim = left_column.button("Sim")
    botao_nao = right_column.button("Não")
    st.write("Parecer:")
    parecer = verificar_dados(equipamento, resultado, batimentos)
    st.write(parecer)
else:
    st.write("Houve um erro ao carregar a imagem. Por favor, tente novamente.")
