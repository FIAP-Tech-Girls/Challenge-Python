# Saudações com a IA, dando uma humanização para a experiência do usuário.

print("Seja bem-vindo(a) à Tiana, a sua Inteligência Artificial sobre o trânsito!")

nome = input("Qual o seu nome?")

# Perguntas iniciais, que determinam a primeira interação da IA com o usuário

print(f"{nome}, nessa primeira parte, é uma entrevista sobre trânsito. Você gostaria de participar?")
print("Para participar da entrevista, digite Sim. \n Para não participar da entrevista digite Não")

opcaoEntrevista = input("Informe a opção, conforme o menu: ")

if (opcaoEntrevista == "Sim") or (opcaoEntrevista == "sim"):
    print("Fazer entrevista. ")

elif (opcaoEntrevista == "Não") or (opcaoEntrevista == "não"):
    print("Agradecemos a atenção!")
    print("{nome}, você deseja explorar outro menu de opções?")
    # Em construção.
    
else:
    print("Opção inválida.")
    # Em construção.