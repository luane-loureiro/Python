numero = round (float(input("Digite um número, comm nomaximo 2 casas decimais: ")),2)
intervalo1, intervalo2, intervalo3, intervalo4 = "0,25", "25,50", "50,75", "75,100"

if 0 <= numero <=25:
    print(intervalo1)

elif 25 < numero <= 50:
    print(intervalo2)

elif 50 < numero <= 75:
    print(intervalo3)

elif 75 < numero <= 100:
    print(intervalo4)

else :
    print("fora do intervalo!")

input("Pressione Enter para sair...")
