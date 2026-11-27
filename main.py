numeros = []

for contador in range(10):
    numero = int(input(f"Digite o {contador + 1}ª número: "))
    numeros.append(numeros)
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print("Lista original", numero)
print("Numeros pares", pares)
print("Numeros impares", impares)
print("quantidade de pares", len(pares))
print("quantidade de impares", len(pares))
