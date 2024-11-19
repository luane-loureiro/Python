codigo, quantidade = map(int, 
                        input("digite o codigo de produto e a Quantidade (separada por espaços): ").split())

precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50,
}

total = precos[codigo] * quantidade

print (f"O valor total é {total}")

input("Pressione Enter para sair...")


