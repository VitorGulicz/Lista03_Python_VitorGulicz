#Peça ao usuário para inserir 1, 2 ou 3. Se ele inserir um 1, exiba a mensagem "Obrigado", se ele inserir um 2, exiba "Muito bem", se ele inserir um 3, exiba "Correto". 
# Se ele inserir qualquer outra coisa, exiba "Mensagem de erro".
num=int(input("Insira 1, 2 ou 3: "))
if num==1:
    print("Obrigado Vitor Gulicz")
else:
    if num==2:
        print("Muito bem Vitor Gulicz")
    else:
        if num==3:
            print("Correto Vitor Gulicz")
        else:
            print("Mensagem de erro Vitor Gulicz")