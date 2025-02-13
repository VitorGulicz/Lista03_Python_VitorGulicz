#Escreva um programa que faça o cálculo do imposto de renda 2025. Consulte a tabela no site da Receita federal.
salario=float(input("Digite o seu salario: "))
if 2826.66>=salario>=2259.21:#7.5%
    imposto=salario-(salario*0.075)
    print("Salario com imposto de renda de 7.5% R$: {} Vitor Gulicz".format (imposto))
elif 3751.05>=salario>=2826.66:#15%
    imposto=salario-(salario*0.15)
    print("Salario com imposto de renda de 15% R$: {} Vitor Gulicz".format (imposto))
elif 4664.68>=salario>=3751.05:#25.5%
    imposto=salario-(salario*0.225)
    print("Salario com imposto de renda de 25.5% R$: {} Vitor Gulicz".format (imposto))
elif salario>=4664.68:#27.5%
    imposto=salario-(salario*0.275)
    print("Salario com imposto de renda de 27.5% R$: {} Vitor Gulicz".format (imposto))
else:
       print("Seu salario não possui imposto de renda Vitor Gulicz")