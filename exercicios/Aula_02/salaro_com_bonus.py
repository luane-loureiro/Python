nome = input ("Digite no Nome do Vendedor: ")
salario = float (input("Digite o salário do colaborador: "))
vendas_total = float (input("Digite o Total de Vendas no mês: "))
comicao = float (input("Digite o valor da comiçao: "))

total = salario + (vendas_total * (comicao/100))


print (f"O valor a receber do colaborador {nome} é de {total:.2f}")
input("Pressione Enter para sair...")