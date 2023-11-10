import json
import bcrypt
import getpass

def login(email: str, senha: str):
    '''
        Função criada para simular o login do usuário através do arquivo JSON contendo os dados dos usuários
        e a senha criptografada, em que o próprio sistema consegue descriptografar e fazer o acesso caso os dados
        estejam corretos.
    '''
    with open('testes/testeCadastroLogin/usuarios.json', 'r', encoding='utf-8') as arquivo: 
        usuarios = json.load(arquivo)
        
    global apelidoUsuario
    global emailUsuario
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
            
    if not encontrouUsuario:
        print("Email não cadastrado em nosso sistema. Por favor, verifique o email digitado.")
        return False
    
    if encontrouUsuario and not senhaCorreta:
        print("A senha está incorreta! Tente novamente!")
        return False
    
def edicaoCadastro():
    with open('testes/testeCadastroLogin/usuarios.json', 'r', encoding='utf-8') as arquivo: 
        usuarios = json.load(arquivo)

    for usuario in usuarios:
        if usuario['email'] == emailUsuario:
            print("O que você deseja editar em seu cadastro?")
            print("\n 1 - Nome \n 2 - Apelido \n 3 - Email \n 4 - Senha \n")
            try: # Tratamento de erros para evitar opções indesejadas e paradas inesperadas
                edicaoUsuario = int(input("O que você deseja editar? "))
                if (edicaoUsuario < 1) or (edicaoUsuario > 4):
                    raise TypeError
                
                elif edicaoUsuario == 1: 
                    # Alterar o nome
                    usuario['nome'] = input("Informe o novo nome: ")
                    print("Nome atualizado com sucesso!")
                elif edicaoUsuario == 2:
                    # Alterar o apelido
                    usuario['apelido'] = input("Informe o novo apelido: ")
                    print("Apelido atualizado com sucesso!")
                elif edicaoUsuario == 3:
                    # Alterar o email
                    usuario['email'] = input("Informe o novo email: ")
                    print("Email atualizado com sucesso!")
                elif edicaoUsuario == 4:
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

    with open('testes/testeCadastroLogin/usuarios.json', 'w', encoding='utf-8') as arquivo: 
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

email = input("Email: ")
senha = input("Senha: ")

login(email, senha)
edicaoCadastro()