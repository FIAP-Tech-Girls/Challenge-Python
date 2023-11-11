import json
import random
import time

def contagemAleatoriaCarros():
    return random.randint(0, 100)

def estadoTrafego(carros):
    if 0 <= carros <= 20:
        return "Leve"
    elif 21 <= carros <= 50:
        return "Moderado"
    else:
        return "Intenso"

def arquivoJSON(local):
    carros = contagemAleatoriaCarros()
    estadoTrafegoAtual = estadoTrafego(carros)

    data = {
        "horário": time.strftime("%Y-%m-%d %H:%M:%S"),
        "carros": carros,
        "estadoTrafego": estadoTrafegoAtual,
        "local": local
    }

    with open("testes/contagem_carros.json", "w", encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

def obterEstadoTrafego():
    with open("testes/contagem_carros.json", "r", encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data["estadoTrafego"]

# Loop principal para interação com o usuário
while True:

    print("1. Verificar estado atual do tráfego")
    print("2. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        local = input("Digite o local que deseja verificar a situação do tráfego: ")
        arquivoJSON(local)  # Gera o arquivo antes de verificar o estado
        estadoAtual = obterEstadoTrafego()
        print(f"A situação do tráfego em {local} é: {estadoAtual}")
    elif opcao == "2":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
