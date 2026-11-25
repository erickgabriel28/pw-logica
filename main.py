import random

numero_secreto = random.randint(1, 20)
tentativas = 0
palpite = int(input(
    "Tente adivinhar um numeri entre 1 e 20:"))

while palpite != numero_secreto:
    tentativas += 1
    if palpite < numero_secreto:
        print("O numero secreto e maior!")
    else:
        print("O numero secreto e menor!")
    palpite = int(input("Tente novamente: "))

tentativas += 1
print("Parabens! Você acertou!")
print(f"O numero secreto era:{numero_secreto}")
print(f"Você utilizou {tentativas} tentativas.")