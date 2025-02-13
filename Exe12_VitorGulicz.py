#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular a soma (+), 
# subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada. (usar ELIF)
n1=float(input("Digite o primeiro numero: "))
n2=float(input("Digite o segundo numero: "))
opcao=input('Digite "+" para soma, "-" para subtração, "*" para multiplicação e "/" para divisão: ')
if "+" in opcao:
    resultado=n1+n2
    print("Resultado da operação de soma: {} Vitor Gulicz".format(resultado))
elif "-" in opcao:
    resultado=n1-n2
    print("Resultado da operação de subtração: {} Vitor Gulicz".format(resultado))
elif "*" in opcao:
    resultado=n1*n2
    print("Resultado da operação de multiplicação: {} Vitor Gulicz".format(resultado))
elif "/" in opcao:
    resultado=n1/n2
    print("Resultado da operação de divisão: {} Vitor Gulicz".format(resultado))
else:
    print("Opção invalida Vitor Gulicz")