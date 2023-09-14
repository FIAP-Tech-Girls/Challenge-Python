import getpass
import bcrypt


nome = input("Digite seu nome completo: ")
apelido = input("Digite como deseja ser chamado durante a nossa conversa: ")
email = input("Digite seu e-mail: ")
senha = getpass.getpass("Digite sua senha (ela está ocultada pela sua segurança: )")

# a nível de simular a privacidade e segurança dos dados do usuário

salt = bcrypt.gensalt() #gera um salt aleatório

hashSenha = bcrypt.hashpw(senha.encode("utf-8"), salt)

cadastro = {
    "nome": nome,
    "apelido": apelido,
    "email": email,
    "senha": hashSenha
}

print(hashSenha)

print(cadastro)