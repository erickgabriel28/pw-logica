alunos = {
    "joao": 8,
    "maria": 9,
    "Pedro": 5,
    "roberto": 6,
}
for nota, nota in alunos.items():
    if nota >= 7:
        print(f"{nome}Esta aprovado: ")
    else:
        print(f"{nome}Esta reprovado: ")