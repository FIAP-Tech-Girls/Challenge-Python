import json
import random
import time

def contagemAleatoriaCarros():
    """
        Função para gerar uma contagem aleatória de carros
    """
    return random.randint(0, 100)  # Ajuste o intervalo conforme necessário

# Função para determinar o estado do tráfego com base na contagem de carros
def estadoTrafego(carros):
    if 0 <= carros <= 20:
        return "Leve"
    elif 21 <= carros <= 50:
        return "Moderado"
    else:
        return "Intenso"

# Função para gerar um arquivo JSON simulando a contagem de carros
def arquivoJSON():
    carros = contagemAleatoriaCarros()
    estado_trafego = estadoTrafego(carros)

    data = {
        "horário": time.strftime("%Y-%m-%d %H:%M:%S"),
        "carros": carros,
        "estadoTrafego": estado_trafego,
        "local": "São Paulo"
    }

    with open("testes/contagem_carros.json", "w", encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

# Função para obter o estado do tráfego a partir do arquivo JSON
def obterEstadoTragego():
    with open("testes/contagem_carros.json", "r", encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data["estadoTrafego"]

# Loop principal para interação com o usuário
while True:
    arquivoJSON()  # Gera o arquivo antes de verificar o estado

    print("1. Verificar estado atual do tráfego")
    print("2. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        estado_atual = obterEstadoTragego()
        print(f"O estado atual do tráfego é: {estado_atual}")
    elif opcao == "2":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
