#Pergunte ao usuário se está chovendo e converta sua resposta em minúsculas para que não importe em que caso ele digite. Se ele responder "sim", pergunte se está ventando.
#  Se ele responder "sim" a esta segunda pergunta, exiba a resposta "Está ventando muito para um guarda-chuva", caso contrário, exiba a mensagem "Pegue um guarda-chuva". 
# Se ele não respondera sim à primeira pergunta, mostre a resposta "Aproveite o seu dia".
chovendo=input("Está chovendo?")
if "sim" in chovendo.lower():
    chovendo=input("Está ventando?")
    if "sim" in chovendo.lower():
        print("Está ventando muito para um guarda chuva Vitor Gulicz")
    else:
        print("Pegue um guarda chuva Vitor Gulicz")
else:
    print("Aproveite seu dia Vitor Gulicz")