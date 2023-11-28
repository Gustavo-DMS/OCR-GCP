import cv2
import json
import os
import pyperclip

def showInMovedWindow(winname, img, x, y):
    cv2.namedWindow(winname)        # Create a named window
    cv2.moveWindow(winname, x, y)   # Move it to (x,y)
    cv2.resizeWindow(winname, 700, 100)
    cv2.imshow(winname,img)
    cv2.waitKey(0)

def is_float(string):
    if string.replace(".", "").replace(",","").isnumeric():
        return True
    else:
        return False

for i in os.listdir("resultados crop"):
# Convert the image to base64 format
    with open(f"resultados crop/{i}", "r") as resultado:
        # print(i)
        resultado_json = json.load(resultado)
        for x in resultado_json["textAnnotations"]:
            print(x["description"])
            if(is_float(x["description"]) ):
                print('Is float: ',x["description"])
    path = i.split(".")[0]
    print(path)
    pyperclip.copy(f"{path}")
    img = cv2.imread(f"Fotos HC Crop/{path}.jpg")
    showInMovedWindow(path, img, 400, 0)
    cv2.destroyAllWindows()
