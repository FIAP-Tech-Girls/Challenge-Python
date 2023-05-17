# Função que pegaria a quantidade de veiculos do usuário e jogaria numa lista
def veiculosDirige(veiculos):
    listaVeiculos = []
    for i in range (veiculos):
        print("Exemplo de tipo de veículo: carro, moto, caminhonete...")
        print("Por favor, digite um por vez!")
        veiculo = input("Digite o tipo de veículo: ")
        listaVeiculos.append(veiculo)
        i += 1
    print(f"Os tipos digitados foram: {listaVeiculos}")

veiculos = int(input("Informe a quantidade de veículos aqui: "))

veiculosDirige(veiculos)