import os
import base64
from google.cloud import vision

for i in os.listdir("Fotos HC"):
# Convert the image to base64 format
    with open(f"Fotos HC/{i}", "rb") as imagem:
        encoded_image = base64.b64encode(imagem.read()).decode()
        client = vision.ImageAnnotatorClient()
        response = client.annotate_image({
            'image':  {'content': f"{encoded_image}"},
          'features': [{'type_': vision.Feature.Type.TEXT_DETECTION}],
        })
        # print(response)
        salvar = i.split(".")[0]
        fds = open(f"resultados/{salvar}.json","w")
        teste = vision.AnnotateImageResponse.to_json(response)
        fds.write(f"{teste}")


