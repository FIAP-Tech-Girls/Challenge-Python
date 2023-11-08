'''
    A rota precisa ter 
    1. Ponto de origem
    2. Ponto de destino
    3. Qual nome deseja salvar para a rota
'''

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

def rotaFavorita(emailUsuario: str, pontoOrigem: str, pontoDestino: str, tituloRotaFav: str):

    with open('testes/testeCadastroLogin/rotasFavoritas.json', 'r', encoding='utf-8') as arquivo: 
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
    
    with open('testes/testeCadastroLogin/rotasFavoritas.json', 'w', encoding='utf-8') as arquivo: 
        json.dump(rotasFav, arquivo, indent=4, ensure_ascii=False)

    print("Rota cadastrada com sucesso!")

def editarRotaFav():
    '''
        Função feita para edição de rotas favoritas.
    '''
    with open('testes/testeCadastroLogin/rotasFavoritas.json', 'r', encoding='utf-8') as arquivo: 
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

    with open('testes/testeCadastroLogin/rotasFavoritas.json', 'w', encoding='utf-8') as arquivo: 
        json.dump(rotasFav, arquivo, indent=4, ensure_ascii=False)

def excluirRota():
    '''
        Função feita para exclusão de rotas favoritas.
    '''
    with open('testes/testeCadastroLogin/rotasFavoritas.json', 'r', encoding='utf-8') as arquivo: 
        rotasFav = json.load(arquivo)
        # Para facilitar a lógica do programa caso encontre ou não o título desejado pelo usuário
    encontrouRota = False 

    if emailUsuario not in rotasFav: # Caso o usuário não possua nenhuma rota favorita
        print("Você não possui rotas favoritas cadastradas! Que tal cadastrar algumas?")

    else: # Caso possua
        titulo = input("Qual título da rota que você deseja excluir? \n")
        removerChaves = []
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
                        removerChaves.append(chave)
                        print(f"O {titulo} foi removido com sucesso!")

                    elif opcaoCerteza == 2:
                        print("Nenhuma rota foi removida!")

                except ValueError: # caso valor diferente de inteiro
                    print("Por favor, informe somente números dentre as opções disponíveis!")
                    
                except TypeError: # caso opção não existente no sistema
                    print("Por favor, digite uma opção válida para prosseguir.")

            if not encontrouRota: # caso a rota chamada não exista no sistema
                print(f"A rota para o título {titulo} não existe! Tente novamente, ou cadastre em nosso sistema para editar.")

    # Remover as chaves marcadas para remoção -> exclui tudo de uma vez
    for chave in removerChaves:
        del rotasFav[emailUsuario]

    with open('testes/testeCadastroLogin/rotasFavoritas.json', 'w', encoding='utf-8') as arquivo: 
        json.dump(rotasFav, arquivo, indent=4, ensure_ascii=False)

emailLogin: str = input("Digite seu email: ")
senhaLogin: str = getpass.getpass("Digite sua senha: ")

login(emailLogin, senhaLogin)

print(f"Olá {apelidoUsuario}")

#editarRotaFav()
excluirRota()

#pontoOrigem = input("Digite o ponto de origem: ")
#pontoDestino = input("Digite o ponto de destino: ")
#tituloRota = input("Digite o título da rota: ")
#rotaFavorita(emailLogin, pontoOrigem, pontoDestino, tituloRota)
