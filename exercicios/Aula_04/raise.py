try:
    idade = int(input("Digite sua idade: "))
    if idade < 0:
        raise ValueError("Idade não pode ser Negativa, a não ser que você viaje no tempo.")
    print(f"Sua idade é {idade}")
except ValueError:
    print(f"Erro: {e}")