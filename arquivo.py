# Importações necessárias para a aplicação

import time # intervalo de tempo para o usuário poder visualizar e processar as informações
import getpass # simular a entrada de senha de uma maneira segura (neste primeiro momento)
import bcrypt # criptografar senha, a nível de garantir integridade e segurança do usuário
import openrouteservice # API para simulação de rotas 
import folium # para mostrar um mapa e não somente derivadas pro usuário
import webbrowser # abrir o mapa automaticamente para o usuário, mesmmo que nesse momento seja somente com HTML
import json # para abrir arquivos json externos da aplicação

# variáveis criadas anteriormente para inicialização do programa

usuarios = [] # utilizada na função de cadastro e login para acesso ao arquivo externo de usuários

# Funções

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

def cadastro():
    '''
        Função utilizada para simular o cadastro dentro da aplicação. Dentro dessa função, é simulado também
        a questão da integridade e segurança dos dados do usuário, ocultando a senha e criptografando em seguida.
    '''

    # abre o arquivo para manter os dados anteriormente inseridos
    with open('usuarios.json', 'r', encoding='utf-8') as arquivo: 
        usuarios = json.load(arquivo)

    email: str = input("Digite seu e-mail: ")
    usuarioExiste = False
    for usuario in usuarios:
         if usuario['email'] == email:
              usuarioExiste = True
              print("O email já está registrado em nosso sistema! Por favor, realize seu login com email e senha!")

    if not usuarioExiste:
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
    '''
        Função criada para simular o login do usuário através do arquivo JSON contendo os dados dos usuários
        e a senha criptografada, em que o próprio sistema consegue descriptografar e fazer o acesso caso os dados
        estejam corretos.
    '''

    with open('usuarios.json', 'r', encoding='utf-8') as arquivo: 
        usuarios = json.load(arquivo)
        
    global apelidoUsuario
    encontrouUsuario = False
    senhaCorreta = False
    for usuario in usuarios:
        if usuario['email'] == email:
            encontrouUsuario = True
            if bcrypt.checkpw(senha.encode("utf-8"), usuario["senha"].encode("utf-8")):
                apelidoUsuario = usuario["apelido"]
                print(f"Bem-vindo, {apelidoUsuario}!")  
                senhaCorreta = True
                return True
            
    if not encontrouUsuario:
        print("Email não cadastrado em nosso sistema. Por favor, verifique o email digitado.")
        return False
    
    if encontrouUsuario and not senhaCorreta:
        print("A senha está incorreta! Tente novamente!")
        return False
    
def rotaFavorita(emailUsuario: str, pontoOrigem: str, pontoDestino: str, tituloRotaFav: str):
    '''
        Função criada para cadastrar as rotas favoritas do usuário em um arquivo JSON externo, 
        permitindo que as rotas, mesmo após o encerramento da Tiana, fiquem salvas através do e-mail do
        usuário, que é um ID único.
    '''
    with open('testes/testeCadastroLogin/rotasFavoritas.json', 'r', encoding='utf-8') as arquivo: 
        rotasFav = json.load(arquivo)
    
    if emailUsuario not in rotasFav:
        rotasFav[emailUsuario] = {}
    
    rotasUsuario = rotasFav[emailUsuario]
    rota = {
        "Ponto Origem": pontoOrigem,
        "Ponto Destino": pontoDestino
    }
    rotasUsuario[tituloRotaFav] = rota 

    with open('testes/testeCadastroLogin/rotasFavoritas.json', 'w', encoding='utf-8') as arquivo: 
        json.dump(rotasFav, arquivo, indent=4, ensure_ascii=False)
    
    print("Rota cadastrada com sucesso!")
    
# Programa principal