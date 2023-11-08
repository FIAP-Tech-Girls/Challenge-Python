# Importações necessárias para a aplicação

import time # intervalo de tempo para o usuário poder visualizar e processar as informações
import getpass # simular a entrada de senha de uma maneira segura (neste primeiro momento)
import bcrypt # criptografar senha, a nível de garantir integridade e segurança do usuário
import openrouteservice # API para simulação de rotas 
import folium # para mostrar um mapa e não somente derivadas pro usuário
import webbrowser # abrir o mapa automaticamente para o usuário, mesmmo que nesse momento seja somente com HTML
import json # para abrir arquivos json externos da aplicação

# Variáveis criadas anteriormente para inicialização do programa

usuarios = [] # utilizada na função de cadastro e login para acesso ao arquivo externo de usuários

logado = False

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

    if not usuarioExiste: # Caso o usuário não tenha seu email cadastrado em nosso sistema
        nome: str = input("Digite seu nome completo: ").title()
        apelido: str = input("Digite como deseja ser chamado durante a nossa conversa: ").title()
    
        senha: str = getpass.getpass("Digite sua senha (ela está ocultada pela sua segurança): ")

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
                print(f"Bem-vindo, {apelidoUsuario}!")  
                senhaCorreta = True
                return True
            
    if not encontrouUsuario: # caso não exista esse cadastro em nosso sistema
        print("Email não cadastrado em nosso sistema. Por favor, verifique o email digitado.")
        return False
    
    if encontrouUsuario and not senhaCorreta: # Caso exista o email mas a senha está incorreta
        print("A senha está incorreta! Tente novamente!")
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
                        print("Título atualizado com sucesso!")

                    if editarOpcao == 2:
                        # Para editar o ponto de origem 
                        item["Ponto Origem"] = input("Digite o novo ponto de origem da rota favorita: ")
                        print("Ponto de origem atualizado com sucesso!")

                    if editarOpcao == 3:
                        # Para editar o ponto de destino 
                        item["Ponto Destino"] = input("Digite o novo ponto de origem da rota favorita: ")
                        print("Ponto de destino atualizado com sucesso!")

                    if editarOpcao == 4:
                        # Para editar o ponto de origem e destino 
                        item["Ponto Origem"] = input("Digite o novo ponto de origem da rota favorita: ")
                        item["Ponto Destino"] = input("Digite o novo ponto de destino da rota favorita: ")
                        print("Ponto de origem e destino atualizados com sucesso!")

                    if editarOpcao == 5:
                        # Para editar título, ponto de origem e destino
                        item["Titulo"] = input("Digite o novo título da rota favorita: ")
                        item["Ponto Origem"] = input("Digite o novo ponto de origem da rota favorita: ")
                        item["Ponto Destino"] = input("Digite o novo ponto de destino da rota favorita: ")
                        print("Título, ponto de origem e destino atualizados com sucesso!")

                except ValueError: # caso valor diferente de inteiro
                    print("Por favor, informe somente números dentre as opções disponíveis!")
                    
                except TypeError: # caso opção não existente no sistema
                    print("Por favor, digite uma opção válida para prosseguir.")

        if not encontrouRota: # caso a rota chamada não exista no sistema
            print(f"A rota para o título {titulo} não existe! Tente novamente, ou cadastre em nosso sistema para editar.")

    with open('rotasFavoritas.json', 'w', encoding='utf-8') as arquivo: 
        json.dump(rotasFav, arquivo, indent=4, ensure_ascii=False)

def excluirRota():
    """
        Função feita para exclusão de rotas favoritas previamente cadastradas em nosso sistema.
    """

    with open('testes/testeCadastroLogin/rotasFavoritas.json', 'r', encoding='utf-8') as arquivo: 
        rotasFav = json.load(arquivo)
        # Para facilitar a lógica do programa caso encontre ou não o título desejado pelo usuário
    encontrouRota = False 

    if emailUsuario not in rotasFav: # Caso o usuário não possua nenhuma rota favorita
        print("Você não possui rotas favoritas cadastradas! Que tal cadastrar algumas?")

    else: # Caso possua
        titulo = input("Qual título da rota que você deseja excluir? \n")
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
                    
                except TypeError: # caso opção não existente no sistema
                    print("Por favor, digite uma opção válida para prosseguir.")

        for chave in chaveRemover:
            del rotasFav[emailUsuario][chave]
            print("Rota removida com sucesso!")

        if not rotasFav[emailUsuario]:  # Verifique se o usuário não possui mais rotas favoritas
            del rotasFav[emailUsuario] # Deleta do arquivo JSON

        if not encontrouRota: # caso a rota chamada não exista no sistema
            print(f"A rota para o título {titulo} não existe! Tente novamente, ou cadastre em nosso sistema para editar.")

    with open('testes/testeCadastroLogin/rotasFavoritas.json', 'w', encoding='utf-8') as arquivo: 
        json.dump(rotasFav, arquivo, indent=4, ensure_ascii=False)

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
            print("Em breve...")
            logado = True

        elif opcaoInicial == 2:
            # Opção de cadastro
            print("Em breve...")
            
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
