import bcrypt
import getpass

import json # colocar na versão final

usuarios = [] 

def cadastro():
    '''
        Função utilizada para simular o cadastro dentro da aplicação. Dentro dessa função, é simulado também
        a questão da integridade e segurança dos dados do usuário, ocultando a senha e criptografando em seguida.
    '''

    # abre o arquivo para manter os dados anteriormente inseridos
    with open('testes/testeCadastroLogin/usuarios.json', 'r', encoding='utf-8') as arquivo: 
        usuarios = json.load(arquivo)

    nome: str = input("Digite seu nome completo: ").title()
    apelido: str = input("Digite como deseja ser chamado durante a nossa conversa: ").title()
    email: str = input("Digite seu e-mail: ")
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

    with open('testes/testeCadastroLogin/usuarios.json', 'w', encoding='utf-8') as arquivoJSON:
            json.dump(usuarios, arquivoJSON, indent=4, ensure_ascii=False)

    print("Cadastro feito com sucesso! Basta realizar seu login para acessar à Tiana!")

    return cadastro

usuario = cadastro()

