nome1 = input("Nome do jogador1: ")
nome2 = input("Nome do jogador2: ")
escolha = input(f"{nome1}. você escolhe (par/impar): ").lower()

n1 = int(input(f"{nome1}. seu numero: "))
n2 = int(input(f"{nome2}. seu numero: "))

soma = n1 + n2
resultado = "par" if soma % 2 == 0 else "impar" 

print(f"\n{n1} + {n2} = {soma} ({resultado})")
 
if escolha == resultado:
    print(f"{nome} ganhou!")
    
else:
    print(f"{nome2} ganhou!")