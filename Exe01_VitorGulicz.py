#Peça dois números. Se o primeiro for maior que o segundo, exiba primeiro o segundo número e depois o primeiro número, caso contrário, mostre primeiro o 
# primeiro número e depois o segundo.
num=int(input("Digite o primeiro numero: "))
num2=int(input("Digite o segundo numero: "))
if num>num2:
    print("Numero 2: {}, Numero 1: {} Vitor Gulicz".format(num2,num))
else:
    print("Numero 1: {}, Numero 2: {} Vitor Gulicz".format(num,num2))