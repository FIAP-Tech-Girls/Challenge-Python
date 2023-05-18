# Função que simula roda favorita do usuário (isso mudará posteriormente)
def rotasFavoritas(rotas):
    listaRotas = []
    for i in range(rotas):
        print("Digite qual rota você deseja inserir em sua favorita!")
        print("Por favor, digite um por vez!")
        rotaFav = input("Digite a rota favorita aqui: ")
        listaRotas.append(rotaFav)
        i += 1
    return listaRotas

rotas = int(input("Informe a quantidade de rotas favoritas que deseja inserir aqui (somente o número por favor) aqui: "))
rotasFav = rotasFavoritas(rotas)

print("Deseja ver quais rotas são suas favoritas? Digite 1 para sim e 2 para não")
verRota = int(input("Digite aqui a opção escolhida: "))

if verRota == 1:
    print(f"As suas rotas favoritas foram: {rotasFav}")
else:
    print("Continua com o menu!")