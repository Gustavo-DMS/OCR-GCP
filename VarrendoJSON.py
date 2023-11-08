import json
import os

def is_float(string):
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False

for i in os.listdir("resultados"):
# Convert the image to base64 format
    with open(f"resultados/{i}", "r") as resultado:
        print(i)
        resultado_json = json.load(resultado)
        for i in resultado_json["textAnnotations"]:

            if(is_float(i["description"]) ):
                print(i["description"])

