salario = float(input("digite o seu salário: "))

if salario <= 400.00:
    percentual = 15

elif salario <= 800.00:
    percentual = 12

elif salario <= 1200.00:
    percentual = 10

elif salario <= 2000.00
    percentual = 7

else 
    percentual = 4

reajuste_percentual = salario (percentual/100)
novo_salario = salario + reajuste_percentual

print (f"Novo Salario: {novo_salario:.2f}")
print (f"Reajuste ganho: {reajuste_percentual:.2f}")
print (f"Em percentual: {percentual} %")

input("Pressione Enter para sair...")

