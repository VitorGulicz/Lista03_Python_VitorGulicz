#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento
#  de 10%. Para os inferiores ou iguais, de 15%.
Salario=float(input("Qual é seu salario: "))
if Salario>1250.00:
    bonus=Salario*0.10+Salario
    print("Salario com bonus R$: {} Vitor Gulicz".format(bonus))
else:
    bonus=Salario*0.15+Salario
    print("Salario com bonus R$: {} Vitor Gulicz".format(bonus))