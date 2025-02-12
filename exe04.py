#Peça ao usuário para inserir sua cor favorita. Se ele digitar "vermelho", "VERMELHO" ou "Vermelho" exibem a mensagem "Eu também gosto de vermelho", caso contrário, 
# exibem a mensagem "Eu não gosto de [cor], eu prefiro vermelho".
cor=input("Digite sua cor Favorita: ")
if cor=="vermelho":
    print("Eu tambem gosto de vermelho Vitor Gulicz")
else:
    if cor=="Vermelho":
        print("Eu tambem gosto de vermelho Vitor Gulicz")
    else:
        if cor=="VERMELHO":
            print("Eu tambem gosto de vermelho Vitor Gulicz")
        else:
            print("Eu não gosto de {} Vitor Gulicz".format (cor))