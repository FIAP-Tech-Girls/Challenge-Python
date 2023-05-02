# Saudações com a IA, dando uma humanização para a experiência do usuário.
print("Seja bem-vindo(a) à Tiana, a sua Inteligência Artificial sobre o trânsito!")
nome = input("Qual o seu nome? Informe aqui: ")

# Função de menu de opções
def menuOpcoes():
    print(f"{nome}, seja bem-vindo(a) novamente! Para prosseguir nossa conversa, selecione uma opção abaixo:")
    print(f"\n 1 - Participar da entrevista sobre trânsito \n 2 - Reportar algum problema em alguma via \n 3 - Saber a situação de alguma via \n 4 - Rotas alternativas para um mesmo destino \n 5 - Encerrar a IA")
    opcao = int(input("Por favor, informe uma opção: "))
    return opcao

while True:
    opcao = menuOpcoes()
    if opcao == 1:
        print(f"{nome}, para prosseguirmos com a entrevista, você dirige?")

        print("Digite 1 para sim \n Digite 2 para não")

        opcaoDirigir = int(input("Digite a opção escolhida: "))
        
    elif opcao == 2:
        print("Implementações inseridas posteriormente")
    elif opcao == 3:
        print("Implementações inseridas posteriormente")
    elif opcao == 4:
        print("Implementações inseridas posteriormente")
    elif opcao == 5:
        print(f"{nome}, obrigada por utilizar a Tiana!")
        break
    else:
        print("Desculpe... Não entendi. Acredito que você inseriu uma opção inválida. Por favor, tente novamente!")
