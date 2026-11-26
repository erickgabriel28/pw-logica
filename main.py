opcao = 0 
while opcao != 4:
    print("\n===== Menu de Operações =====")
    print("1 - Mostrar mensagem de Boas-Vindas!")
    print("2 - Mostrar a tabuada de um numero")
    print("3 - informar se um numero e par ou impar")
    print("4 - Sair")
    opcao = int(input("Escolher uma opção: "))

    if opcao == 1:
        print("\nSeja bem vindo ao programa!")

    elif opcao == 2:
        numero = int(input("Digite um numero para ver a tabuada: "))

        for contador in range(1, 11):
            print(f"{numero} x {contador} = {numero * contador}")

    elif opcao == 3:
        numero =int(input("Digite um numero: "))
        if numero %2 == 0:
            print(f"O numero {numero} é Par! ")
        else:
            print(f"O numero {numero} é IMPAR!")

    elif opcao == 4:
        print("\n Encerramento o programa... Até mais.")
    else:
        print("Opção invalida!")