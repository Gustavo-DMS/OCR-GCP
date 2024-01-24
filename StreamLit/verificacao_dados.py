def verificar_dados(tipo_equipamento,valores:list,batimentos:bool):

    if tipo_equipamento == "Balança":
        if len(valores) != 2:
            return "Erro"
        valores[1] = valores[1].replace(",", ".")
        IMC = float(valores[0]) / (float(valores[1])**2)
        if IMC < 16.0:
            return "Magreza grave"
        elif IMC < 17.0:
            return "Magreza moderada"
        elif IMC < 18.5:
            return "Magreza leve"
        elif IMC < 25.0:
            return "Saudável"
        elif IMC < 30.0:
            return "Sobrepeso"
        elif IMC < 35.0:
            return "Obesidade grau I"
        elif IMC < 40.0:
            return "Obesidade severa"
        elif IMC >= 40.0:
            return "Obesidade mórbida"
        else:
            return "Erro"

    if tipo_equipamento == "Termômetro":
        if len(valores) != 1:
            return "Erro"
        print(valores[0])
        if float(valores[0]) < 35.0:
            return "Hipotermia"
        elif float(valores[0]) < 37.0:
            return "Normal"
        elif float(valores[0]) <= 41:
            return "Febre"
        elif float(valores[0]) >= 41.1:
            return "Hipértemia"
        else:
            return "Erro"

    if tipo_equipamento == "Medidor de pressão":
        if batimentos:
            if len(valores) != 3:
                return "Erro"
            return "Batimentos cardiacos não implementados"
        if not batimentos:
            valores.sort()
            if len(valores) != 2:
                return "Erro"
            elif float(valores[0]) < 85.0 and valores[1] < 130.0:
                return "Normal"
            elif float(valores[0]) < 90 and valores[1] < 140.0:
                return "Normal límitrofe"
            elif float(valores[0]) < 100 and valores[1] < 160.0:
                return "Hipertensão leve"
            elif float(valores[0]) < 110 and valores[1] < 180.0:
                return "Hipertensão moderada"
            elif float(valores[0]) >= 110 and valores[1] >= 180.0:
                return "Hipertensão grave"
            elif float(valores[0]) < 90 and valores[1] >= 140.0:
                return "Hipertensão sistólica isolada"
            else:
                return "Erro"
