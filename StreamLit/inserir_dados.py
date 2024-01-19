import mysql.connector
 from datetime import datetime

def insercao_banco(resultado,paciente):
    mydb = mysql.connector.connect(
      host="us-imm-web538.main-hosting.eu",
      user="u664201219_ztbIa",
      password="OcrDiag@2bd",
      database="u664201219_3H9aE",
    )
    data = datetime.now()
    data.strftime('%Y-%m-%d %H:%M:%S')
    mycursor = mydb.cursor()
    response = mycursor.execute("INSERT  FROM paciente")
    response = mycursor.fetchall()
    mycursor.close()
    mydb.close()
