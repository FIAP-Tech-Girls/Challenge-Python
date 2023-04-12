# Saudações com a IA, dando uma humanização para a experiência do usuário.

print("Seja bem-vindo(a) à Tiana, a sua Inteligência Artificial sobre o trânsito!")

nome = input("Qual o seu nome? Informe aqui: ")

# Perguntas iniciais, que determinam a primeira interação da IA com o usuário

print(f"{nome}, nessa primeira parte, é uma entrevista sobre trânsito. Você gostaria de participar?")
print("Para participar da entrevista, digite Sim. \n Para não participar da entrevista digite Não")

opcaoEntrevista = input("Informe a opção, conforme o menu: ")

# Caso a opção seja sim para participar da entrevista.
if (opcaoEntrevista == "Sim") or (opcaoEntrevista == "sim"):
    print(f"{nome}, para prosseguirmos com a entrevista, você dirige?")
    print("Digite 1 para sim \n Digite 2 para não")

    opcaoDirigir = int(input("Digite a opção escolhida: "))

    match opcaoDirigir:
        # Caso a opção seja sim para dirigir.
        case 1:

            print("Quantos tipos de veículos você dirige? Veja no menu de opções:")

            print("1 - para opção de somente um veículo.")
            print("2 - para a opção de dois veículos.")
            print("3 - para a opção de três veículos.")
            print("4 - para a opção de quatro ou mais.")

            veiculos = int(input("Digite a opção escolhida: "))

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

            print("1 - Manhã.")
            print("2 - Tarde.")
            print("3 - Noite.")

            periodo = int(input("Digite aqui a opção escolhida: "))

            print("Nesse período, você pega muito trânsito?")

            print("1 - Sim")
            print("2 - Não")

            transito = int(input("Digite aqui a opção escolhida: "))

            if transito == 2:
                print("Em qual período você costuma pegar mais trânsito?")

                print("1 - Manhã.")
                print("2 - Tarde.")
                print("3 - Noite.")

                periodoTransito = int(input("Digite aqui a opção escolhida: "))

            print("Como você costuma reagir ao trânsito?")

            reacaoTransito = input("Digite aqui como você costuma reagir ao trânsito. Sinta-se livre: ")

        # Caso a opção seja de não dirigir
        case 2: 
            print("Perguntas aqui")

        case _:
            print("Opção inválida. Por favor, tente novamente.")

elif (opcaoEntrevista == "Não") or (opcaoEntrevista == "não"):
    print("Agradecemos a atenção!")
    print(f"{nome}, você deseja explorar outro menu de opções?")
    # Em construção.

else:
    print("Opção inválida. Por favor, tente novamente.")