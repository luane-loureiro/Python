cod1, qtd1, valor1 = input ("Digite o codigo, quantidade e valor da primeira item: ").split()
cod2, qtd2, valor2 = input ("Digite o codigo, quantidade e valor da Sefundo item: ").split()

qtd1, valor1 = int(qtd1), float(valor1)
qtd2, valor2 = int(qtd2), float(valor2)

valor_total = (valor1 * qtd1) + (valor2 * qtd2)

print(f"VALOR TOTAL A PAGAR: {valor_total}")

input("Pressione Enter para sair...")