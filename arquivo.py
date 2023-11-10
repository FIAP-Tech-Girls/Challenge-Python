# Importações necessárias para a aplicação

import time # intervalo de tempo para o usuário poder visualizar e processar as informações
import getpass # simular a entrada de senha de uma maneira segura (neste primeiro momento)
import bcrypt # criptografar senha, a nível de garantir integridade e segurança do usuário
import openrouteservice # API para simulação de rotas 
import folium # para mostrar um mapa e não somente derivadas pro usuário
import webbrowser # abrir o mapa automaticamente para o usuário, mesmmo que nesse momento seja somente com HTML
import json # para abrir arquivos json externos da aplicação

# Variáveis criadas anteriormente para inicialização do programa

categoriasCNH = {
    'A': 'Categoria A - Motocicletas',
    'B': 'Categoria B - Veículos de passeio',
    'C': 'Categoria C - Veículos de carga',
    'D': 'Categoria D - Ônibus',
    'E': 'Categoria E - Veículos de carga pesada com reboque'
}

usuarios = [] # utilizada na função de cadastro e login para acesso ao arquivo externo de usuários

logado = False

chaveAPI = '5b3ce3597851110001cf62480b2433fb93fa4bf4bcda5d0487e0ee7f' # futuramente, tratar isso para ter mais segurança e não ser de fácil acesso pros usuários

client = openrouteservice.Client(key=chaveAPI) # Inicializa o cliente OpenRouteService

# Funções

def cadastro():
    """
        Função utilizada para simular o cadastro dentro da aplicação. Dentro dessa função, é simulado também
        a questão da integridade e segurança dos dados do usuário, ocultando a senha e criptografando em seguida.
    """

    # abre o arquivo para manter os dados anteriormente inseridos
    with open('usuarios.json', 'r', encoding='utf-8') as arquivo: 
        usuarios = json.load(arquivo)

    email: str = input("Digite seu e-mail: ")
    usuarioExiste = False
    for usuario in usuarios:
         if usuario['email'] == email: # Caso o usuário já tenha seu email cadastrado em nosso sistema
            usuarioExiste = True
            print("O email já está registrado em nosso sistema! Por favor, realize seu login com email e senha!")
            time.sleep(1)
              
    if not usuarioExiste: # Caso o usuário não tenha seu email cadastrado em nosso sistema
        nome: str = input("Digite seu nome completo: ").title()
        time.sleep(1)

        apelido: str = input("Digite como deseja ser chamado durante a nossa conversa: ").title()
        time.sleep(1)

        senha: str = getpass.getpass("Digite sua senha (ela está ocultada pela sua segurança): ")
        time.sleep(1)

        salt = bcrypt.gensalt() # gera um salt aleatório

        hashSenha = bcrypt.hashpw(senha.encode("utf-8"), salt)
        hashSenhaString = hashSenha.decode('utf-8')

        cadastro = {
            "nome": nome,
            "apelido": apelido,
            "email": email,
            "senha": hashSenhaString
        }

        usuarios.append(cadastro)

        with open('usuarios.json', 'w', encoding='utf-8') as arquivoJSON:
                json.dump(usuarios, arquivoJSON, indent=4, ensure_ascii=False)

        print("Cadastro feito com sucesso! Basta realizar seu login para acessar à Tiana!")
        time.sleep(1)
        return cadastro

def login(email: str, senha: str):
    """
        Função criada para simular o login do usuário através do arquivo JSON contendo os dados dos usuários
        e a senha criptografada, em que o próprio sistema consegue descriptografar e fazer o acesso caso os dados
        estejam corretos.
    """

    with open('usuarios.json', 'r', encoding='utf-8') as arquivo: 
        usuarios = json.load(arquivo)
        
    global apelidoUsuario # Para facilitar comunicação com o usuário logado
    global emailUsuario # Para facilitar pegar o email nas demais funções

    encontrouUsuario = False
    senhaCorreta = False
    
    for usuario in usuarios:
        emailUsuario = usuario['email']
        if emailUsuario == email:
            encontrouUsuario = True
            if bcrypt.checkpw(senha.encode("utf-8"), usuario["senha"].encode("utf-8")):
                apelidoUsuario = usuario["apelido"]
                time.sleep(1)
                print(f"Bem-vindo, {apelidoUsuario}!")  
                senhaCorreta = True
                return True
            
    if not encontrouUsuario: # caso não exista esse cadastro em nosso sistema
        print("Email não cadastrado em nosso sistema. Por favor, verifique o email digitado.")
        time.sleep(1)
        return False
    
    if encontrouUsuario and not senhaCorreta: # Caso exista o email mas a senha está incorreta
        print("A senha está incorreta! Tente novamente!")
        time.sleep(1)
        return False
    
def rotaFavorita(emailUsuario: str, pontoOrigem: str, pontoDestino: str, tituloRotaFav: str):

    """ 
        Função criada para criação de rotas favoritas de cada usuário, sendo armazenada em um arquivo JSON
        para que cada usuário possua a sua e fique salva mesmo após o usuário deslogar de sua conta na Tiana,
        e que mesmo após cadastrar novas, não apaguem as anteriormente salvas.
    """

    with open('rotasFavoritas.json', 'r', encoding='utf-8') as arquivo: 
        rotasFav = json.load(arquivo)
    
    if emailUsuario not in rotasFav: # Caso o usuário não possua rotas favoritas cadastradas, já cria o dicionário
        rotasFav[emailUsuario] = {}

    rotasUsuario = rotasFav.get(emailUsuario, {})
    # chave inteira para rotas favoritas -> para facilitar a identificação de cada rota
    chave = 1
    if rotasUsuario:
        chavesInt = [int(chave) for chave in rotasUsuario.keys()] # preciso transformar em inteira para fazer a soma
        chave = str(max(chavesInt) + 1) # Depois de somar, transformo para string para cadastrar na nova rota

    rota = {
        "Titulo": tituloRotaFav,
        "Ponto Origem": pontoOrigem,
        "Ponto Destino": pontoDestino
    }

    rotasUsuario[chave] = rota # cadastro a nova rota dentro da chave
    rotasFav[emailUsuario] = rotasUsuario # adiciono no email do usuário mais rotas
    
    with open('rotasFavoritas.json', 'w', encoding='utf-8') as arquivo: 
        json.dump(rotasFav, arquivo, indent=4, ensure_ascii=False)

    print("Rota cadastrada com sucesso!")

def editarRotaFav():
    """
        Função feita para edição de rotas favoritas previamente salvas em nosso sistema.
    """

    with open('rotasFavoritas.json', 'r', encoding='utf-8') as arquivo: 
        rotasFav = json.load(arquivo)

    # Para facilitar a lógica do programa caso encontre ou não o título desejado pelo usuário
    encontrouRota = False 

    if emailUsuario not in rotasFav: # Caso o usuário não possua nenhuma rota favorita
        print("Você não possui rotas favoritas cadastradas! Que tal cadastrar algumas? ")
        time.sleep(1)

    else: # Caso possua
        titulo = input("Qual título da rota que você deseja editar? \n")
        for item in rotasFav[emailUsuario].values():
            if item["Titulo"] == titulo:
                encontrouRota = True # se encontra, passa a ser verdadeiro para prosseguir
                print(f"O que você deseja editar para {titulo}?")
                print("\n 1 - Título \n 2 - Ponto de origem \n 3 - Ponto de destino \n 4 - Ponto de origem e destino \n 5- Título, ponto de origem e destino \n")
                
                try: # Tratamento de erros para evitar opções indesejadas e paradas inesperadas
                    editarOpcao = int(input("Informe a opção desejada: "))

                    if (editarOpcao < 1) or (editarOpcao > 5):
                        raise TypeError
                    
                    if editarOpcao == 1:
                        # Para editar título
                        item["Titulo"] = input("Digite o novo título da rota favorita: ")
                        time.sleep(1)
                        print("Título atualizado com sucesso!")
                        time.sleep(1)

                    if editarOpcao == 2:
                        # Para editar o ponto de origem 
                        item["Ponto Origem"] = input("Digite o novo ponto de origem da rota favorita: ")
                        time.sleep(1)
                        print("Ponto de origem atualizado com sucesso!")
                        time.sleep(1)

                    if editarOpcao == 3:
                        # Para editar o ponto de destino 
                        item["Ponto Destino"] = input("Digite o novo ponto de origem da rota favorita: ")
                        time.sleep(1)
                        print("Ponto de destino atualizado com sucesso!")
                        time.sleep(1)

                    if editarOpcao == 4:
                        # Para editar o ponto de origem e destino 
                        item["Ponto Origem"] = input("Digite o novo ponto de origem da rota favorita: ")
                        time.sleep(1)
                        item["Ponto Destino"] = input("Digite o novo ponto de destino da rota favorita: ")
                        time.sleep(1)
                        print("Ponto de origem e destino atualizados com sucesso!")
                        time.sleep(1)

                    if editarOpcao == 5:
                        # Para editar título, ponto de origem e destino
                        item["Titulo"] = input("Digite o novo título da rota favorita: ")
                        time.sleep(1)
                        item["Ponto Origem"] = input("Digite o novo ponto de origem da rota favorita: ")
                        time.sleep(1)
                        item["Ponto Destino"] = input("Digite o novo ponto de destino da rota favorita: ")
                        time.sleep(1)
                        print("Título, ponto de origem e destino atualizados com sucesso!")
                        time.sleep(1)

                except ValueError: # caso valor diferente de inteiro
                    print("Por favor, informe somente números dentre as opções disponíveis!")
                    time.sleep(1)
                    
                except TypeError: # caso opção não existente no sistema
                    print("Por favor, digite uma opção válida para prosseguir.")
                    time.sleep(1)

        if not encontrouRota: # caso a rota chamada não exista no sistema
            print(f"A rota para o título {titulo} não existe! Tente novamente, ou cadastre em nosso sistema para editar.")
            time.sleep(1)

    with open('rotasFavoritas.json', 'w', encoding='utf-8') as arquivo: 
        json.dump(rotasFav, arquivo, indent=4, ensure_ascii=False)

def excluirRota():
    """
        Função feita para exclusão de rotas favoritas previamente cadastradas em nosso sistema.
    """

    with open('rotasFavoritas.json', 'r', encoding='utf-8') as arquivo: 
        rotasFav = json.load(arquivo)
        # Para facilitar a lógica do programa caso encontre ou não o título desejado pelo usuário
    encontrouRota = False 

    if emailUsuario not in rotasFav: # Caso o usuário não possua nenhuma rota favorita
        print("Você não possui rotas favoritas cadastradas! Que tal cadastrar algumas?")
        time.sleep(1)

    else: # Caso possua
        titulo = input("Qual título da rota que você deseja excluir? \n")
        time.sleep(1)
        chaveRemover = []
        for chave, item in rotasFav[emailUsuario].items():
            if item["Titulo"] == titulo:
                encontrouRota = True # se encontra, passa a ser verdadeiro para prosseguir
                print(f"Você tem certeza que deseja remover {titulo} de suas rotas favoritas?") 
                # Para o usuário ter certeza e não excluir nada sem desejar
                print("\n 1 - Sim \n 2 - Não \n")

                try: # tratamento de erros para evitar paradas indesejadas durante o programa
                    opcaoCerteza = int(input("Informe a opção desejada aqui: "))
                    if (opcaoCerteza < 1) or (opcaoCerteza > 2):
                        raise TypeError
                    
                    elif opcaoCerteza == 1:
                            chaveRemover.append(chave)

                    elif opcaoCerteza == 2:
                        print("Nenhuma rota foi removida!")

                except ValueError: # caso valor diferente de inteiro
                    print("Por favor, informe somente números dentre as opções disponíveis!")
                    time.sleep(1)
                    
                except TypeError: # caso opção não existente no sistema
                    print("Por favor, digite uma opção válida para prosseguir.")
                    time.sleep(1)

        for chave in chaveRemover:
            del rotasFav[emailUsuario][chave]
            print("Rota removida com sucesso!")
            time.sleep(1)

        if not rotasFav[emailUsuario]:  # Verifique se o usuário não possui mais rotas favoritas
            del rotasFav[emailUsuario] # Deleta do arquivo JSON

        if not encontrouRota: # caso a rota chamada não exista no sistema
            print(f"A rota para o título {titulo} não existe! Tente novamente, ou cadastre em nosso sistema para editar.")
            time.sleep(1)

    with open('rotasFavoritas.json', 'w', encoding='utf-8') as arquivo: 
        json.dump(rotasFav, arquivo, indent=4, ensure_ascii=False)

def listarRotasFavoritas():
    """
        Função para listar as rotas favoritas de forma visual e amigável para o usuário.
    """
    with open('rotasFavoritas.json', 'r', encoding='utf-8') as arquivo: 
        rotasFav = json.load(arquivo)

    if emailUsuario not in rotasFav: # Caso o usuário não possua nenhuma rota favorita
        print("Você não possui rotas favoritas cadastradas! Que tal cadastrar algumas?")

    else: # Verifica se o usuário tem rotas favoritas
        print("Aqui estão suas rotas favoritas:")
        for chave, item in rotasFav[emailUsuario].items():
            print("-----------------------------------")
            print(f"Rota {chave}:")
            print(f"  Título: {item['Titulo']}")
            print(f"  Ponto de Origem: {item['Ponto Origem']}")
            print(f"  Ponto de Destino: {item['Ponto Destino']}")
            print("-----------------------------------")

def preferenciaRotas():
    """
        Função criada para simular preferências de rota através das respostas do usuário.
    """

    with open('preferenciaRotas.json', 'r', encoding='utf-8') as arquivo: 
        preferencia = json.load(arquivo)

    print("Vamos lá!")

    if emailUsuario not in preferencia: # Caso o usuário não possua rotas favoritas cadastradas, já cria o dicionário
        preferencia[emailUsuario] = {}

    if preferencia:
        print("Vias com Ônibus")
        try:
            print("\n 1 - Não me importo \n 2 - Não desejo \n")
            pref1 = int(input("Informe a opção desejada: "))
            if (pref1 < 1) or (pref1 > 2):
                raise TypeError

            print("Vias com comércio")
            print("\n 1 - Não me importo \n 2 - Não desejo \n")
            pref2 = int(input("Informe a opção desejada: "))
            if (pref2 < 1) or (pref2 > 2):
                raise TypeError
            
            print("Vias com postos de gasolina")
            print("\n 1 - Não me importo \n 2 - Não desejo \n")
            pref3 = int(input("Informe a opção desejada: "))
            if (pref3 < 1) or (pref3 > 2):
                raise TypeError
            
            print("Vias com muitos semafóros")
            print("\n 1 - Não me importo \n 2 - Não desejo \n")
            pref4 = int(input("Informe a opção desejada: "))
            if (pref4 < 1) or (pref4 > 2):
                raise TypeError
            
            print("Vias com pedágios")
            print("\n 1 - Não me importo \n 2 - Não desejo \n")
            pref5 = int(input("Informe a opção desejada: "))
            if (pref5 < 1) or (pref5 > 2):
                raise TypeError
            
            preferenciaRota = {
                "Vias com ônibus": pref1,
                "Vias com comércios": pref2,
                "Vias com posto de gasolinas": pref3,
                "Vias com muitos semafóros": pref4,
                "Vias com pedágios": pref5
            }

            preferencia[emailUsuario] = preferenciaRota

            with open('preferenciaRotas.json', 'w', encoding='utf-8') as arquivo: 
                json.dump(preferencia, arquivo, indent=4, ensure_ascii=False)

        except ValueError:
            print("Por favor, informe somente números dentre as opções disponíveis!")
            time.sleep(1)

        except TypeError:
            print("Por favor, digite uma opção válida para prosseguir.")
            time.sleep(1)

def edicaoCadastro():
    """
        Função criada para realizar a edição do cadastro do usuário conforme sua decisão,
        atualizando no JSON final.
    """
    global apelidoUsuario

    with open('usuarios.json', 'r', encoding='utf-8') as arquivo: 
        usuarios = json.load(arquivo)

    for usuario in usuarios:
        if usuario['email'] == emailUsuario:
            print("O que você deseja editar em seu cadastro?")
            print("\n 1 - Nome \n 2 - Apelido \n 3 - Senha \n")
            try: # Tratamento de erros para evitar opções indesejadas e paradas inesperadas
                edicaoUsuario = int(input("O que você deseja editar? "))
                if (edicaoUsuario < 1) or (edicaoUsuario > 3):
                    raise TypeError
                
                elif edicaoUsuario == 1: 
                    # Alterar o nome
                    usuario['nome'] = input("Informe o novo nome: ")
                    print("Nome atualizado com sucesso!")
                elif edicaoUsuario == 2:
                    # Alterar o apelido
                    novoApelido = input("Informe o novo apelido: ")
                    usuario['apelido'] = novoApelido
                    apelidoUsuario = novoApelido
                    print(f"Apelido atualizado com sucesso!")
                elif edicaoUsuario == 3:
                    # Alterar a senha
                    novaSenha: str = getpass.getpass("Digite sua senha (ela está ocultada pela sua segurança): ")

                    salt = bcrypt.gensalt() # gera um salt aleatório

                    hashSenha = bcrypt.hashpw(novaSenha.encode("utf-8"), salt)
                    hashSenhaString = hashSenha.decode('utf-8')

                    usuario['senha'] = hashSenhaString

                    print("Senha atualizada com sucesso!")           

            except ValueError: # caso valor diferente de inteiro
                print("Por favor, informe somente números dentre as opções disponíveis!")
                
            except TypeError: # caso opção não existente no sistema
                print("Por favor, digite uma opção válida para prosseguir.")

    with open('usuarios.json', 'w', encoding='utf-8') as arquivo: 
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

def menuOpcoes():
    """
        Função criada para o menu de opções, para facilitar o tratamento de erros e deixar o código mais
        limpo na parte da programação principal.
    """
    print("\n 1 - Participar da entrevista sobre qualificação do trânsito; \n 2 - Configurar preferências de rotas \n 3 - Visualizar rotas alternativas de destino \n 4 - Situação de determinada rota \n 5 - Feedback sobre determinada rota \n 6 - Favoritar uma rota \n 7 - Listar rotas favoritas \n 8 - Editar rotas favoritas \n 9 - Excluir rotas favoritas \n 10 - Feedback sobre a Tiana \n 11 - Configurar perfil \n 12 - Encerrar Tiana \n")
    try: # Tratamento de erros para evitar paradas indesejadas 
        opcao = int(input("Informe a opção desejada: "))
        if (opcao < 1) or (opcao > 12):
            raise TypeError
        return opcao
    except ValueError:
        print("Por favor, informe somente números dentre as opções disponíveis!")
        time.sleep(1)
    except TypeError:
        print("Por favor, digite uma opção válida para prosseguir.")
        time.sleep(1)

# Programa principal

'''
    Enquanto o usuário não tiver logado, o usuário não poderá acessar as demais funcionalidades da aplicação
    segundo o estudo de caso e requisitos da aplicação definido pela Tech Girls.
'''
while logado == False:
    print("Olá! Seja bem vindo(a) à Tiana! Para prosseguir, é necessário que você esteja logado em nosso sistema!")
    print("Escolha a opção abaixo para continuar")
    print("\n 1 - Login \n 2 - Cadastro \n 3 - Encerrar à Tiana \n")
    try: # Tratamento de erros para evitar paradas inesperadas durante o programa
        opcaoInicial = int(input("Escolha uma das opções acima: "))

        if (opcaoInicial < 1) or (opcaoInicial > 3):
            raise TypeError
        
        elif opcaoInicial == 1:
            # Opção de login
            emailLogin: str = input("Digite seu email: ")
            senhaLogin: str = getpass.getpass("Digite sua senha (ela está ocultada para sua segurança): ")
            time.sleep(1)
            loginUsuario = login(emailLogin, senhaLogin)
            time.sleep(1)
            if loginUsuario == True: # caso deu tudo certo no login (não houve nenhum dado errado!)
                logado = True

        elif opcaoInicial == 2:
            # Opção de cadastro
            cadastro()
            time.sleep(1)
            print("Faça seu login, para sua segurança, para prosseguir com à Tiana")
            time.sleep(1)
            emailLogin: str = input("Digite seu email: ")
            senhaLogin: str = getpass.getpass("Digite sua senha (ela está ocultada para sua segurança): ")
            time.sleep(1)
            loginUsuario = login(emailLogin, senhaLogin)
            time.sleep(1)
            if loginUsuario == True: # caso deu tudo certo no login (não houve nenhum dado errado!)
                logado = True        
            
        elif opcaoInicial == 3:
            # Encerra a Tiana sem continuar com as funcionalidades
            print("Agradecemos por utilizar à Tiana!")
            break

    except ValueError:
        print("Por favor, informe somente números dentre as opções disponíveis!")
        time.sleep(1)

    except TypeError:
        print("Por favor, digite uma opção válida para prosseguir.")
        time.sleep(1)

# Caso o usuário esteja logado, podemos prosseguir com o looping infinito do programa principal
if logado == True:
    print(f"Olá {apelidoUsuario}! Seja bem vindo(a)!")
    time.sleep(1)
    print(f"Como podemos te auxiliar hoje?")
    time.sleep(1)
    while True:
        opcao = menuOpcoes()
        if opcao == 1:
            # Entrevista sobre qualificação do trânsito
            print(f"{apelidoUsuario}, para prosseguirmos com a sua entrevista, por favor, informe-nos")
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

            print(f"Agradecemos por suas respostas {apelidoUsuario}!")

        elif opcao == 2:
            # Configurar preferência de rotas
            preferenciaRotas()
            time.sleep(1)

        elif opcao == 3:
            # Visualizar rotas alternativas
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
                time.sleep(1)
            else:
                print("Não foi possível encontrar uma rota.")
                time.sleep(1)

        elif opcao == 4:
            # Situação de determinada rota 
            print("Em breve...")
            time.sleep(1)

        elif opcao == 5:
            # Feedback sobre determinada rota pelos usuários
            print(f"Qual é o caminho que você deseja dar feedback, {apelidoUsuario}?")
            caminho = input("Digite aqui: ")
            print(f"Qual o problema com o {caminho}? Selecione uma opção abaixo:")
            print(f"\n 1 - Reportar acidente; \n 2 - Reportar congestionamento \n 3 - Outro")

            try:
                feedbackCaminho = int(input("Informe a opção desejada: "))
                if (feedbackCaminho < 1) or (feedbackCaminho > 3):
                    raise TypeError
                
                if feedbackCaminho == 1:
                    print(f"{apelidoUsuario}, agradecemos pelo seu aviso! Iremos avisar os demais usuários!")
                    time.sleep(1)
                elif feedbackCaminho == 2:
                    print(f"{apelidoUsuario}, agradecemos pelo seu aviso! Iremos avisar os demais usuários!")
                    time.sleep(1)
                elif feedbackCaminho == 3:
                    feedbackOutro = input("Conte-nos com detalhe sobre o que aconteceu: ")
                    time.sleep(1)
                    print(f"{apelidoUsuario}, agradecemos pelo seu feedback! Iremos avisar os demais usuários!")
                    time.sleep(1)

            except ValueError:
                print("Por favor, informe somente números dentre as opções disponíveis!")
                time.sleep(1)
            except TypeError:
                ("Por favor, digite uma opção válida para prosseguir.")
                time.sleep(1)
            time.sleep(1)

        elif opcao == 6:
            # Favoritar uma rota
            pontoOrigem: str = input("Digite o ponto de origem: ")
            pontoDestino: str = input("Digite o ponto de destino: ")
            tituloRota: str = input("Digite o título da rota: ")
            rotaFavorita(emailUsuario, pontoOrigem, pontoDestino, tituloRota)
            time.sleep(1)

        elif opcao == 7:
            # Listar todas as rotas favoritas do usuário
            listarRotasFavoritas()
            time.sleep(1)

        elif opcao == 8:
            # Editar rota favorita do usuário
            editarRotaFav()
            time.sleep(1)

        elif opcao == 9:
            # Excluir rota favorita do usuário
            excluirRota()
            time.sleep(1)

        elif opcao == 10:
            # Feedback sobre Tiana
            print(f"{apelidoUsuario} sua opinião é muito importante para nós! Escreva sua avaliação que iremos receber, ler e aprimorar.")
            feedbackTiana = input("Digite seu feedback \n")
            time.sleep(1)
            print("Agradecemos a sua avaliação e preferência! Conte sempre com a gente!")
            time.sleep(1)

        elif opcao == 11:
            # Configurar perfil
            edicaoCadastro()
            time.sleep(1)

        elif opcao == 12:
            # Encerrar a Tiana
            print("Obrigada por utilizar a Tiana!")
            print("Deslogando...")
            time.sleep(1)
            break