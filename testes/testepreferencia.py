usuarios = []

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
            #time.sleep(1)

        except TypeError:
            print("Por favor, digite uma opção válida para prosseguir.")
            #time.sleep(1)

emailUsuario = input()

senhaUsuario = input()

login(emailUsuario, senhaUsuario)

preferenciaRotas()