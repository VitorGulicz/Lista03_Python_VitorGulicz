#Pergunte a idade do usuário. Se tiver 16 anos ou mais, exiba a mensagem "Você pode votar", se tiver 18 anos, exiba a mensagem "Você pode aprender a dirigir", se tiver 14 anos,
#exiba a mensagem "Você pode comprar um bilhete de loteria", se tiver menos de 14 anos, exiba a mensagem "Você pode fazer doces ou travessuras".
idade=int(input("Quantos anos voce tem? "))
if idade>=18:
    print("Você pode aprender a dirigir Vitor Gulicz")
else:
    if 18>idade>=16:
        print("Você pode votar Vitor Gulicz")
    else:
        if 16>idade>=14:
            print("Você pode comprar um bilhete de loteria Vitor Gulicz")
        else:
            print("Você pode fazer doces ou travessuras Vitor Gulicz")