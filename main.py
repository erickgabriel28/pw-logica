import random


opcoes = ['pedra', 'papel', 'tesoura']


computador = random.choice(opcoes)


jogador = input("Escolha entre pedra, papel ou tesoura: ").strip().lower()


if jogador not in opcoes:
    print("Jogada inválida! Por favor, escolha apenas 'pedra', 'papel' ou 'tesoura'.")
else:

    print("-" * 30)
    print(f"Computador escolheu: {computador}")
    print(f"Você escolheu: {jogador}")
    print("-" * 30)


    if jogador == computador:
        print("Empate! Vocês fizeram a mesma escolha.")
    elif (
        (jogador == 'pedra' and computador == 'tesoura') or
        (jogador == 'papel' and computador == 'pedra') or
        (jogador == 'tesoura' and computador == 'papel')
    ):
        print("Você ganhou!")
    else:
        print("Você perdeu!")