matricula = int(input("Digite a matricula do colaborador: "))
horas = int (input("Digite quantas horas trabalhadas: "))
valor_hora = int (input ("Digite o recebido pago por hora: "))

salario = horas * valor_hora

print (f"MATRICULA: {matricula}")
print (f"SALARY = U$ {salario:.2f}")

input("Pressione Enter para sair...")