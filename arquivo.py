# Imports necessários para a aplicação

import time # intervalo de tempo para o usuário poder visualizar e processar as informações
import getpass # simular a entrada de senha de uma maneira segura (neste primeiro momento)
import bcrypt # criptografar senha, a nível de garantir integridade e segurança do usuário
import openrouteservice # API para simulação de rotas 
import folium # para mostrar um mapa e não somente derivadas pro usuário
import webbrowser # abrir o mapa automaticamente para o usuário, mesmmo que nesse momento seja somente com HTML

# Criações de variáveis necessárias para início do programa.

categoriasCNH = {
    'A': 'Categoria A - Motocicletas',
    'B': 'Categoria B - Veículos de passeio',
    'C': 'Categoria C - Veículos de carga',
    'D': 'Categoria D - Ônibus',
    'E': 'Categoria E - Veículos de carga pesada com reboque'
}

chaveAPI = '5b3ce3597851110001cf62480b2433fb93fa4bf4bcda5d0487e0ee7f' # futuramente, tratar isso para ter mais segurança e não ser de fácil acesso pros usuários

client = openrouteservice.Client(key=chaveAPI) # Inicializa o cliente OpenRouteService

rotasFavoritas = []

# Funções

def cadastro():
    '''
        Função utilizada para simular o cadastro dentro da aplicação. Dentro dessa função, é simulado também
        a questão da integridade e segurança dos dados do usuário, ocultando a senha e criptografando em seguida.
    '''
    
    global apelido # deixa global para poder utilizar o apelido durante todo sistema.

    nome = input("Digite seu nome completo: ").title()
    apelido = input("Digite como deseja ser chamado durante a nossa conversa: ").title()
    email = input("Digite seu e-mail: ")
    senha = getpass.getpass("Digite sua senha (ela está ocultada pela sua segurança): ")

    salt = bcrypt.gensalt() # gera um salt aleatório

    hashSenha = bcrypt.hashpw(senha.encode("utf-8"), salt)

    cadastro = {
        "nome": nome,
        "apelido": apelido,
        "email": email,
        "senha": hashSenha
    }

    return cadastro


def menuOpcoes():
    '''
        Função utilizada para facilitar e deixar o código inteiro do sistema mais limpo para chamar 
        o menu de opções, que se repete em todo looping. Há uma validação para evitar que erros aconteçam.
    '''

    print(f"\n 1 - Participar da entrevista de qualificação do trânsito; \n 2 - Ver situação de determinada rota; \n 3 - Feedback sobre determinada rota; \n 4 - Rotas alternativas para um destino; \n 5 - Favoritar uma rota \n 6 - Visualizar rotas favoritas \n 7 - Feedback sobre aplicativo; \n 8 - Encerrar Tiana.")
    try:
        opcao = int(input("Informe a opção desejada: "))
        if (opcao < 1) or (opcao > 8):
            raise TypeError
        return opcao
    except ValueError:
        print("Por favor, informe somente números dentre as opções disponíveis!")
        time.sleep(1)
    except TypeError:
        print("Por favor, digite uma opção válida para prosseguir.")
        time.sleep(1)

# Programa principal

cadastroUsuario = cadastro()

time.sleep(1)

print(f"{apelido}, seja bem-vindo(a) à Tiana. Como podemos te ajudar hoje?")

time.sleep(1)

while True:
    opcao = menuOpcoes()
    if opcao == 1:
        # Opção para entrevista para levantamento de dados sobre o trânsito.
        print(f"{apelido}, para prosseguirmos com a sua entrevista, por favor, informe-nos")
        print("Você dirige? \n 1 - Sim \n 2 - Não")
        opcaoEntrevista = input("Digite aqui a opção escolhida: ")

        match opcaoEntrevista:

            case "1":
                print("Qual a categoria da sua CNH? Para auxiliar, veja a lista abaixo!")
                for codigo, descricao in categoriasCNH.items():
                    print(f"{codigo}: {descricao}")
                categoriaCNH = input("Informe aqui a sua categoria presente na carteira de motorista: ")

                try:
                        print("Você dirige com mais frequência a trabalho ou a diversão (sozinho, com sua família, amigos, entre outros?) Veja no menu de opções:")

                        print("1 - Dirijo mais a trabalho.")
                        print("2 - Dirijo mais a diversão.")

                        opcaoDirige = int(input("Digite aqui a opção escolhida: "))

                        # Para saber mais sobre o que a pessoa trabalha 
                        if opcaoDirige == 1:
                            print("Para qual trabalho você mais utiliza seu veículo?")

                            print("1 - Uber/Táxi")
                            print("2 - Entregador")
                            print("3 - Outro.")

                            opcaoTrabalho = int(input("Digite aqui a opção escolhida: "))

                            if opcaoTrabalho == 3:
                                outroTrabalho = input("Informe qual o trabalho que você utiliza seu automóvel: ")
                        
                        print("Você dirige com mais frequência sozinho ou acompanhado?")

                        print("1 - Dirijo mais sozinho.")
                        print("2 - Dirijo mais acompanhado.")

                        sozinhoouacompanhado = int(input("Digite aqui a opção escolhida: "))

                        print("Em qual período você costuma dirigir com mais frequência?")

                        print("\n 1 - Manhã \n 2 - Tarde \n 3 - Noite \n ")

                        periodo = int(input("Digite aqui a opção escolhida: "))

                        print("Nesse período, você pega muito trânsito?")

                        print("\n 1 - Sim \n 2 - Não \n")

                        transito = int(input("Digite aqui a opção escolhida: "))

                        if transito == 2:
                            print("Em qual período você costuma pegar mais trânsito?")

                            print("\n 1 - Manhã \n 2 - Tarde \n 3 - Noite \n ")

                            periodoTransito = int(input("Digite aqui a opção escolhida: "))

                        print("Como você costuma reagir ao trânsito?")

                        reacaoTransito = input("Sinta-se livre para escrever como se sente, num limite de até 1000 caracteres: ")
                except ValueError:
                    print("Por favor, informe somente números dentre as opções disponíveis!")
                    time.sleep(1)
                except TypeError:
                    print("Por favor, digite uma opção válida para prosseguir.")
                    time.sleep(1)

            case "2":
                try:
                    print("Qual meio de transporte você utiliza com mais frequência? Veja no menu de opções:")

                    print("\n 1 - Uber/Táxi \n 2 - Carona (amigos(as), marido/esposa, entre outros) \n 3 - Transporte Público \n")

                    opcaoTransporte = int(input("Digite aqui apenas uma opção: "))

                    print("Em qual período você costuma sair com mais frequência?")

                    print("\n 1 - Manhã \n 2 - Tarde \n 3 - Noite \n ")

                    periodoSair = int(input("Digite aqui apenas uma opção: "))

                    print("Nesse período, você costuma pegar muito trânsito?")

                    print("\n 1 - Sim \n 2 - Não \n")
                        
                    transitoPeriodo = int(input("Digite aqui apenas uma opção: "))

                    if transitoPeriodo == 2:
                        print("Então, em qual dos períodos abaixo você costuma pegar muito trânsito?")

                        print("\n 1 - Manhã \n 2 - Tarde \n 3 - Noite \n ")
                        
                    print("Como você costuma reagir ao trânsito?")

                    reacaoTransito = input("Sinta-se livre para escrever como se sente, num limite de até 1000 caracteres: ")
                
                except ValueError:
                    print("Por favor, informe somente números dentre as opções disponíveis!")
                    time.sleep(1)
                except TypeError:
                    print("Por favor, digite uma opção válida para prosseguir.")
                    time.sleep(1)
                    
            case _:
                print("Opção inválida. Tente novamente!")

        print(f"Agradecemos por suas respostas {apelido}!")
    
    elif opcao == 2:
        # Opção para ver situação sobre determinada rota
        print("Em breve")

    elif opcao == 3:
        # Opção para dar feedback sobre um determinado caminho
        print(f"Qual é o caminho que você deseja dar feedback, {apelido}?")
        caminho = input("Digite aqui: ")
        print(f"Qual o problema com o {caminho}? Selecione uma opção abaixo:")
        print(f"\n 1 - Reportar acidente; \n 2 - Reportar congestionamento \n 3 - Outro")

        try:
            feedbackCaminho = int(input("Informe a opção desejada: "))
            if (feedbackCaminho < 1) or (feedbackCaminho > 3):
                raise TypeError
            
            if feedbackCaminho == 1:
                print(f"{apelido}, agradecemos pelo seu aviso! Iremos avisar os demais usuários!")
                time.sleep(1)
            elif feedbackCaminho == 2:
                print(f"{apelido}, agradecemos pelo seu aviso! Iremos avisar os demais usuários!")
                time.sleep(1)
            elif feedbackCaminho == 3:
                feedbackOutro = input("Conte-nos com detalhe sobre o que aconteceu: ")
                time.sleep(1)
                print(f"{apelido}, agradecemos pelo seu feedback! Iremos avisar os demais usuários!")
                time.sleep(1)

        except ValueError:
            print("Por favor, informe somente números dentre as opções disponíveis!")
            time.sleep(1)
        except TypeError:
            ("Por favor, digite uma opção válida para prosseguir.")
            time.sleep(1)

    elif opcao == 4:
        # Opção para ver caminhos alternativos para determinado destino
        pontoPartida = input("Informe o local de partida, informe, por favor, como exemplo 'Avenida Paulista, São Paulo, Brasil': ") 
        destino = input("Informe o local de destino, informe, por favor, como exemplo 'Avenida Paulista, São Paulo, Brasil': ")

        coordenadas_partida = client.pelias_search(pontoPartida)['features'][0]['geometry']['coordinates']
        coordenadas_destino = client.pelias_search(destino)['features'][0]['geometry']['coordinates']

        rota = client.directions(
            coordinates=[coordenadas_partida, coordenadas_destino],
            profile='driving-car',  # Você pode usar 'foot-walking' para rota a pé -> futuramente pensar em algo
            format='geojson',
        )

        if 'features' in rota:
            # Crie um mapa com o folium
            mapa = folium.Map(location=[coordenadas_partida[1], coordenadas_partida[0]], zoom_start=15)

            # Adicione a rota ao mapa
            folium.GeoJson(rota).add_to(mapa)

            # Abra o mapa em um navegador
            mapa.save('rota.html')
            webbrowser.open_new_tab('rota.html') # abre o mapa automaticamente

            print("Mapa da rota foi salvo como 'rota.html'.")
        else:
            print("Não foi possível encontrar uma rota.")

    elif opcao == 5:
        # Opção para favoritar uma rota -> aprimorar futuramente
        rotaFavorita = input("Informe a rota/ponto de partida/origem favorito: ")
        rotasFavoritas.append(rotaFavorita)
        time.sleep(1)
        print("Para visualizar suas rotas favoritas, utilize a opção 6, no menu!")
        time.sleep(1)

    elif opcao == 6:
        # Opção para visualizar rotas favoritas -> aprimorar futuramente
        if rotasFavoritas == []:
            print("Não há rotas favoritas! Que tal adicionar? Informe-nos na opção 5!")
            time.sleep(1)
        else:
            print(f"Suas rotas favoritas são {rotasFavoritas}")
            time.sleep(1)

    elif opcao == 7:
        # Opção para feedback sobre a Tiana
        print(f"{apelido} sua opinião é muito importante para nós! Escreva sua avaliação que iremos receber, ler e aprimorar.")
        feedbackTiana = input("Digite seu feedback \n")
        time.sleep(1)
        print("Agradecemos a sua avaliação e preferência! Conte sempre com a gente!")

    elif opcao == 8:
        # Opção para encerrar a Tiana
        print(f"{apelido}, agradecemos por utilizar a Tiana!")
        break
