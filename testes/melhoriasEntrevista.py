categoriasCNH = {
    'A': 'Categoria A - Motocicletas',
    'B': 'Categoria B - Veículos de passeio',
    'C': 'Categoria C - Veículos de carga',
    'D': 'Categoria D - Ônibus',
    'E': 'Categoria E - Veículos de carga pesada com reboque'
}

print("Você dirige? \n 1 - Sim \n 2 - Não")
opcaoEntrevista = input("Digite aqui a opção escolhida: ")

match opcaoEntrevista:

    case "1":
        print("Qual a categoria da sua CNH? Para auxiliar, veja a lista abaixo!")
        for codigo, descricao in categoriasCNH.items():
            print(f"{codigo}: {descricao}")
        categoriaCNH = input("Informe aqui a sua categoria presente na carteira de motorista: ")

        try:
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
        except ValueError:
            print("Por favor, informe somente números dentre as opções disponíveis!")
            #time.sleep(1)
        except TypeError:
            print("Por favor, digite uma opção válida para prosseguir.")
            #time.sleep(1)

    case "2":
        try:
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
        
        except ValueError:
            print("Por favor, informe somente números dentre as opções disponíveis!")
            #time.sleep(1)
        except TypeError:
            print("Por favor, digite uma opção válida para prosseguir.")
            #time.sleep(1)
            
    case _:
        print("Opção inválida. Tente novamente!")
