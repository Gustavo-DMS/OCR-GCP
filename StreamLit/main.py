import json
import base64
import streamlit as st
from google.cloud import vision
from PIL import ImageOps, Image

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

genre = st.radio(
    "Qual o aparelho da imagem?",
    ["Termômetro", "Balança", "Medidor de pressão"],horizontal=True,index=None)

nome = st.text_input("Nome do paciente:")
cuidador = st.text_input("Nome do cuidador:")
medico = st.text_input("Nome do médico:")
if genre == "Termômetro":
    altura = st.text_input("Altura do paciente:")

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
    st.write(resultado)
else:
    st.write("Houve um erro ao carregar a imagem. Por favor, tente novamente.")

