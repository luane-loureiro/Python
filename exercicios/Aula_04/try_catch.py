try:
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
    resultado = numero1/numero2
    print (f"resultado {resultado}")

except ZeroDivisionError:
    print(f"Ta errado! Não pode dividir por 0!")
except ValueError:
    print(f"Pessoa Maluca! Operação não permitida.")