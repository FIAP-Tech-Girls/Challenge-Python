# Criações de variáveis necessárias para início do programa.



# Imports necessários para a aplicação

import time # intervalo de tempo para o usuário poder visualizar e processar as informações
import getpass # simular a entrada de senha de uma maneira segura (neste primeiro momento)
import bcrypt # criptografar senha, a nível de garantir integridade e segurança do usuário

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

    print(f"\n 1 - Participar da entrevista de qualificação do trânsito; \n 2 - Ver situação de determinada rota; \n 3 - Feedback sobre determinada rota; \n 4 - Rotas alternativas para um destino; \n 5 - Favoritar uma rota \n 6 - Feedback sobre aplicativo; \n 7 - Encerrar Tiana.")
    try:
        opcao = int(input("Informe a opção desejada: "))
        if (opcao < 1) or (opcao > 7):
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
        opcaoEntrevista = int(input("Digite aqui a opção escolhida: "))

        match opcaoEntrevista:

            case 1:
                print("Em breve")
            case 2:
                print("Em breve")
            case _:
                print("Em breve")

    elif opcao == 2:
        # Opção para ver situação sobre determinada rota
        print("Em breve")
    elif opcao == 3:
        # Opção para dar feedback sobre um determinado caminho
        print("Em breve")
    elif opcao == 4:
        # Opção para ver caminhos alternativos para determinado destino
        print("Em breve")
    elif opcao == 5:
        # Opção para favoritar uma rota
        print("Em breve")
    elif opcao == 6:
        # Opção para feedback sobre a Tiana
        print("Em breve")
    elif opcao == 7:
        # Opção para encerrar a Tiana
        print(f"{apelido}, agradecemos por utilizar a Tiana!")
        break
