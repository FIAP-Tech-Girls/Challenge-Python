import json
import random
import time

def contagemAleatoriaCarros():
    """
        Função para gerar uma contagem aleatória de carros, uma vez que não iríamos conseguir deixar
        o ESP32 ligado 24 horas para nível de teste no programa em Python, então fizemos de uma forma 
        aleatória que atualiza a cada 1 segundo.
    """
    return random.randint(0, 100)  # Ajuste o intervalo conforme necessário


def estadoTrafego(carros):
    """
        Função para determinar o estado do tráfego com base na contagem de carros
    """
    if 0 <= carros <= 20:
        return "Leve"
    elif 21 <= carros <= 50:
        return "Moderado"
    else:
        return "Intenso"


def arquivoJSON():
    """
        Função para gerar um arquivo JSON simulando a contagem de carros. Esse arquivo JSON é atualizado
        a cada vez que o usuário pede para visualizar qual o estado do trafégo mostrando o último antes de
        ser atualizado.
    """
    carros = contagemAleatoriaCarros()
    estadoTrafegoAtual = estadoTrafego(carros)

    data = {
        "horário": time.strftime("%Y-%m-%d %H:%M:%S"),
        "carros": carros,
        "estadoTrafego": estadoTrafegoAtual,
        "local": "São Paulo"
    }

    with open("testes/contagem_carros.json", "w", encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

# Função para obter o estado do tráfego a partir do arquivo JSON
def obterEstadoTrafego():
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
        estadoAtual = obterEstadoTrafego()
        print(f"O estado atual do tráfego é: {estadoAtual}")
    elif opcao == "2":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
