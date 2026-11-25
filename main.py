operacao = input(
    "Escolha a conversao:\n"
    "1 - Celsius para Fahrenheit:\n"
    "2 - Quilometros para Milhas:\n"
    "3 - Reais para Dolar:\n"
    "4 - Quilogramas para libras:\n")
valor = float(input("Digite o valor que deseja converter: "))
if operacao == "1":
    resultado = (valor * 9 / 5) + 32
    print(f"Resultado: {resultado:.1f} °F")

    if operacao == "2":
    resultado = valor / 1.600
    print(f"Resultado: {resultado:.2f} °F")

    if operacao == "3":
    resultado = valor / 5.93
    print(f"Resultado: {resultado:.2f} °F")

    if operacao == "1":
    resultado = (valor * 9 / 5) + 32
    print(f"Resultado: {resultado:.2f} °F")