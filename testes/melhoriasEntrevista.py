categoriasCNH = {
    'A': 'Categoria A - Motocicletas',
    'B': 'Categoria B - Veículos de passeio',
    'C': 'Categoria C - Veículos de carga',
    'D': 'Categoria D - Ônibus',
    'E': 'Categoria E - Veículos de carga pesada com reboque'
}

print("Você dirige? \n 1 - Sim \n 2 - Não")
opcaoEntrevista = input("Digite aqui a opção escolhida: ")

match opcaoEntrevista:

    case "1":
        print("Qual a categoria da sua CNH?")
        for codigo, descricao in categoriasCNH.items():
            print(f"{codigo}: {descricao}")
    case "2":
        print("Em breve")
    case _:
        print("Opção inválida. Tente novamente!")
