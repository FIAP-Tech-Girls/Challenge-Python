# Saudações com a IA, dando uma humanização para a experiência do usuário.
print("Seja bem-vindo(a) à Tiana, a sua Inteligência Artificial sobre o trânsito!")
nome = input("Qual o seu nome? Informe aqui: ")

# Função de menu de opções
def menuOpcoes():
    print(f"{nome}, seja bem-vindo(a) novamente! Para prosseguir nossa conversa, selecione uma opção abaixo:")
    print(f"\n 1 - Participar da entrevista sobre trânsito \n 2 - Reportar trânsito ou acidente em uma rota \n 3 - Saber a situação de alguma via \n 4 - Rotas alternativas para um mesmo destino \n 5 - Ver rotas favoritas \n 6 - Encerrar a conversa \n")
    opcao = int(input("Por favor, informe uma opção: "))
    return opcao


# Função que pegaria a quantidade de veiculos do usuário e jogaria numa lista
def veiculosDirige(veiculos):
    listaVeiculos = []
    for i in range (veiculos):
        print("Exemplo de tipo de veículo: carro, moto, caminhonete...")
        print("Por favor, digite um por vez!")
        veiculo = input("Digite o tipo de veículo: ")
        listaVeiculos.append(veiculo)
        i += 1
    print(f"Os tipos digitados foram: {listaVeiculos}")

    
while True:
    opcao = menuOpcoes()
    if opcao == 1:
        print(f"{nome}, para prosseguirmos com a entrevista, você dirige?")

        print("\n Digite 1 para sim \n Digite 2 para não \n")

        opcaoDirigir = int(input("Por favor, informe uma opção: "))

        match opcaoDirigir:

            case 1:

                print("Qual a quantidade de tipo de veículos que você dirige?")
                print("Como exemplo: digite 1, caso dirija somente um tipo, digite 2, caso dirija somente dois tipos. Digite apenas o número!")

                veiculos = int(input("Informe a quantidade de veículos aqui: "))
                veiculosDirige(veiculos)

                print("Qual a categoria da sua CNH?")
                categoriaCNH = input("Digite aqui a categoria: ")

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

            case 2:

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

            case _:
                print(f"Opção inserida inválida. Por favor, reinicie e tente novamente!")

    elif opcao == 2:

        print(f"{nome}, qual é a rua, avenida ou rota que você gostaria de reportar um problema?")
        print("Informe o nome por extenso, como exemplo: Avenida Paulista")
        rotaProblema = input("Informe aqui: ")
        print("Qual é o problema? Um acidente ou trânsito?")
        problema = input("Informe aqui: ")

        # Quando informado esse problema, iria repassar para todos os usuários que estariam nessa rota ou procurassem sobre

        print(f"{nome}, a IA Tiana agradece sua contribuição! Será repassado para os demais usuários!")
        print("Caso esteja nessa rota, para rotas alternativas, veja o menu de opções!")

    elif opcao == 3:
        print("Implementações inseridas posteriormente")
    elif opcao == 4:
        print("Implementações inseridas posteriormente")
    elif opcao == 5:
        print("Implementações inseridas posteriormente")
    elif opcao == 6:
        print(f"{nome}, obrigada por utilizar a Tiana!")
        break
    else:
        print("Desculpe... Não entendi. Acredito que você inseriu uma opção inválida. Por favor, tente novamente!")
