#Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso,
#  exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
velcar=int(input("Insira a velocidade do carro em km/h: "))
if velcar>80:
    print("Usuario foi multado")
    multa=(velcar-80)*5
    print("Multa do carro R$: {} Vitor Gulicz".format (multa))
else:
    print("Não multado Vitor Gulicz")