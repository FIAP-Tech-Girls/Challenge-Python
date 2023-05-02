# Saudações com a IA, dando uma humanização para a experiência do usuário.
print("Seja bem-vindo(a) à Tiana, a sua Inteligência Artificial sobre o trânsito!")
nome = input("Qual o seu nome? Informe aqui: ")

# Função de menu de opções
def menuOpcoes():
    print(f"{nome}, seja bem-vindo(a) novamente! Para prosseguir nossa conversa, selecione uma opção abaixo:")
    print(f"\n 1 - Participar da entrevista sobre trânsito \n 2 - Reportar algum problema em alguma via \n 3 - Saber a situação de alguma via \n 4 - Rotas alternativas para um mesmo destino \n 5 - Ver rotas favoritas \n 6 - Encerrar a conversa \n")
    opcao = int(input("Por favor, informe uma opção: "))
    return opcao
            
while True:
    opcao = menuOpcoes()
    if opcao == 1:
        print(f"{nome}, para prosseguirmos com a entrevista, você dirige?")

        print("\n Digite 1 para sim \n Digite 2 para não \n")

        opcaoDirigir = int(input("Por favor, informe uma opção: "))

        match opcaoDirigir:

            case 1:

                print(f"Inserir aqui a entrevista caso a pessoa dirija com melhorias (estudar em casa)")

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
        print("Implementações inseridas posteriormente")
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
