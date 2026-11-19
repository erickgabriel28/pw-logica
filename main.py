preco = 40.0

idade = int(input("Digite a idade do cliente: "))
dia = input("Digite o dia da semana (seg, ter, qua, qui, sex, sab, dom): ").strip().lower()

if idade <= 12:
    preco = preco * 0.5
    print("Meia-entrada: criança")
elif idade <= 21:
    preco = preco * 0.5
    print("Meia-entrada: estudante")
elif idade >= 60:
    preco = preco * 0.5
    print("Meia-entrada: idoso")
else:
    print("Ingresso inteiro")

if dia == "qua":
    preco = preco * 0.5
    print("Promoção de quarta")

print(f"Valor final do ingresso: R$ {preco:.2f}")