import random

# Lista para armazenar números já sorteados
lista_de_sorteados = []
numero_limite = 10
tentativas = 1

# Função para exibir mensagens no terminal
def exibir_texto_na_tela(texto):
    print(texto)

# Função para gerar um número secreto
def gerar_numero():
    global lista_de_sorteados
    numero_escolhido = random.randint(1, numero_limite)

    # Reinicia a lista se já tiver sorteado todos os números possíveis
    if len(lista_de_sorteados) == numero_limite:
        lista_de_sorteados = []

    # Garante que o número ainda não foi sorteado
    if numero_escolhido in lista_de_sorteados:
        return gerar_numero()
    else:
        lista_de_sorteados.append(numero_escolhido)
        return numero_escolhido

# Função de mensagem inicial
def mensagem_inicial():
    exibir_texto_na_tela("Jogo do Número Secreto")
    exibir_texto_na_tela("Escolha um número entre 1 e 10")

# Função para verificar o chute do usuário
def verificar_chute(chute):
    global tentativas, numero_secreto

    if chute == numero_secreto:
        exibir_texto_na_tela("Acertou!")
        palavra_tentativa = 'tentativas' if tentativas > 1 else 'tentativa'
        msg_tentativas = f"Você descobriu o número secreto com {tentativas} {palavra_tentativa}."
        exibir_texto_na_tela(msg_tentativas)
        return True
    else:
        if chute > numero_secreto:
            exibir_texto_na_tela("Número Errado!")
            exibir_texto_na_tela(f"O número secreto é menor que {chute}.")
        else:
            exibir_texto_na_tela("Número Errado!")
            exibir_texto_na_tela(f"O número secreto é maior que {chute}.")

        tentativas += 1
        return False

# Função para reiniciar o jogo
def reiniciar_jogo():
    global numero_secreto, tentativas
    numero_secreto = gerar_numero()
    tentativas = 1
    mensagem_inicial()

# Inicializa o jogo
numero_secreto = gerar_numero()
mensagem_inicial()

# Loop principal do jogo
while True:
    try:
        chute = int(input("Digite seu chute: "))
        if verificar_chute(chute):
            jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
            if jogar_novamente == 's':
                reiniciar_jogo()
            else:
                exibir_texto_na_tela("Obrigado por jogar!")
                break
    except ValueError:
        print("Por favor, digite um número válido.")
