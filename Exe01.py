#Peça dois números. Se o primeiro for maior que o segundo, exiba primeiro o segundo número e depois o primeiro número, caso contrário, mostre primeiro o primeiro número e depois o segundo.
num=int(input("Digite um numero: "))
num2=int(input("Digite o segundo numero: "))
if num>num2:
    print("{}, {} Vitor Gulicz".format(num2,num))
else:
    print("{}, {} Vitor Gulicz".format(num,num2))