num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
operacao = input("Digite a operação desejada (+, -, * ou /): ")

if operacao == "+":
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")

elif operacao == "-":
resultado = num1 - num2
print(f"O resultado da subtração é: {resultado}")

elif operacao == "":
resultado = num1 * num2
print(f"O resultado da multiplicação é: {resultado}")

elif operacao == "/":
if num2 != 0:
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado:.2f}")

else:
    print("Erro! Não pode dividir por zero!")

else:
 print("Operação inválida!")