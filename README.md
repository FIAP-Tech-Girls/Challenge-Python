# Tiana, a Inteligência Artificial.

## O que é?

Projeto de Python criado para a Challenge da @FIAP em parceria com a IBM para as aulas de Computational Thinking With Python.

## Quero testar no meu PC, como fazer? Preciso instalar algo?

- Ao iniciar a aplicação, no terminal, digite "pip install bcrypt" ou "py -3.11 -m pip install bcrypt" e aperte enter, aguardando a instalação;
- Depois, no terminal, digite "pip install openrouteservice" ou "py -3.11 -m pip install openrouteservice" e aperte enter, aguardando a instalação;
- E, por fim, no terminal, digite "pip install folium" ou "py -3.11 -m pip install folium" e aperte enter, aguardando a instalação.
- Feito isso, para rodar o rpojeto em sua máquina, escolha o arquivo.py, que é o programa principal!
- Com o programa rodando você poderá realizar seu cadastro que ficará salvo para acesso ao login ou escolher o email que foi utilizado de teste para a programação para testar o login direito, sendo os dados
alucard@gmail.com
1234
- Aproveite!

## Quem compõe esse projeto?

Esse projeto está sendo construído por 4 programadoras, sendo elas:

<a href="https://github.com/anny-dias">Anny Diaz</a> <br>
<a href="https://github.com/camilapadalino">Camila Padalino</a> <br>
<a href="https://github.com/letyresina">Leticia Resina</a> <br>
<a href="https://github.com/Luanacabezaolias">Luana Cabeazolias</a> <br>

## Quais são as funcionalidades?

A Inteligência artificial que busca ser o mais humanizado possível para a melhor experiência do usuário. Inicialmente, são feitas perguntas iniciais, que questionam o nome da pessoa (onde a interação será feita com o nome da pessoa), e pergunta se ela deseja participar ou não sobre a pesquisa sobre o trânsito. Caso a pessoa não deseja participar, nos sprints futuros, serão implementados:

<ul>
<li>Reportar algum problema em alguma avenida, cidade, que não foi encontrado pelo nosso sistema arduíno (citado posteriormente);</li>
<li>Perguntar sobre a situação de alguma cidade/avenida que deseja passar (se está congestionada, com acidentes, entre outros);</li>
<li>Perguntar rotas alternativas, onde o trânsito é pequeno ou inexistente para evitar o congestionamento;</li>
<li>Quando houver a integração com Login, armazenamento de rotas favoritas para fácil acesso do usuário.</li>
</ul>

## Versões 

Todas as versões serão salvas na pasta "versoes", caso seja do interesse analisar o código detalhadamente, como também para facilitar melhorias e, caso necessário, voltar alguma parte do código de uma versão antiga.
Foi também criado uma pasta de "testes", para testes a parte de alguma funcionalidade antes de jogar no arquivo final.

<ul>
<li>Versão 1.0: Último commit feito no dia 11 de abril de 2023. Essa versão conta com uma saudação padrão da IA, que logo em seguida questiona se o usuário deseja ou não participar da entrevista, trabalhando com match case, ifs e elses. E por fim, agradece o usuário por participar da entrevista e deixou espaço para mais implementações futuras. </li>

<li>Versão 2.0: Último commit feito no dia 18 de maio de 2023. Essa versão conta com uma função de menu de opções, para facilitar a execução do programa. Também foi adicionado um While de Loop infinito, para que o usuário possa utilizar das funções até que decida encerrar a execução. Foram feitas melhorias na própria entrevista, deixando numa linguagem mais compreensível para o usuário. Na parte da entrevista de caso a pessoa dirija, foi feito uma função que armazena uma lista, que a quantidade de valores é a informada pelo próprio usuário para facilitar. Nessa versão, foi feito um pontapé da opção 2, onde o usuário informa um problema em alguma avenida, rua ou rota, indicando se há acidente ou trânsito que a IA não pode captar no momento. Isso seria repassado para os usuários que buscassem determinada rota, e avisaria pro usuário que, caso ele desejasse rotas alternativas, seguisse para a opção, que viria logo em seguida, por conta do looping. A última implementação adicionada simula a adição e visualização de rotas favoritas -> essa implementação está sujeita a mudanças futuras, uma vez que, somente com o Login, o usuário poderá ter essa opção. Nesse caso, fizemos uma simulação para a entrega da Sprint 2.</li>

<li>Versão 3.0: Último commit feito no dia 15 de novembro de 2023. Essa versão, em primeiro momento, foi melhor organizado o código, separando importações, funções, e detalhando o que cada uma delas faz. Foi feito uma função para simular um cadastro, e, ainda que não armazenado em banco, foi feito uma pequena simulação com uma criptografia simples, para garantir a integridade e segurança dos dados do usuário. Diferentemente da versão anterior, nessa versão é necessário fazer o cadastro/login para continuar a utilizar a aplicação. Também foi feito um validação de erro no menu, para evitar erros por parte do usuário, além de validações das informações durante toda a usabilidade, no que se era possivel, com try/except. Nessa versão, foi colocada a nível de teste uma conexão com API de mapa, para simular o que é esperado (ou parecido) na versão final, além de uma simulação com o mapa utilizando folium (futuramente, tudo será tratado da melhor forma e intuitiva para o usuário).</li>

<li>Versão 4.0: Último commit feito no dia 10 de novembro de 2023. Essa versão foi feito uma forma de simular cadastro e login através de um acesso de um arquivo JSON externo, com a senha criptografada para simular a segurança e privacidade para com os dados dos usuários. É importante ressaltar que fora feito uma validação, em que somente realiza um cadastro caso o email não conste no nosso sistema. Foi adicionado também anotações de tipo para facilitar a aplicação para desenvolvedores no geral. Em relação às rotas favoritas cadastradas, através de uma chave única que vai incrementando a cada nova rota cadastrada, são armazenadas em um JSON externo para cada usuário através da chave única que é seu e-mail. O usuário também vai ter como listar, editar e excluir essas rotas favoritas depois de cadastradas em seu arquivo JSON. Em questão do programa principal, para respeitar as regras decididas no estudo de caso e requisitos levantados pelas Tech Girls, é necessário que o usuário esteja logado em sua conta para que possamos continuar com as funcionalidades da aplicação, e para segurança, após o cadastro, logar para então que possamos prosseguir. Foi feito uma simulação de preferência de rotas salvadas em um arquivo JSON externo, ainda simulando o banco de dados para com o usuário. Além disso, o usuário poderá editar alguns de seus dados, com exceção do email, que por hora, é a chave primária de alguns JSONS, funcionamento que será implementado futuramente. Em relação a situação atual de uma determinada rota, como não iríamos conseguir fazer com o ESP32 ligado 24 horas, simulamos um arquivo JSON que recebe uma quantidade de carros aleatória e atualiza a cada vez que o usuário decide verificar a situação de uma determinada rota que o usuário digita e assim, com a lógica de Leve, Moderado e Intenso, conseguimos simular a ideia final da aplicação.</li>

</ul>

## Copyright

ATENÇÃO: O programa deve ser utilizado EXCLUSIVAMENTE como forma de estudos para aqueles que baixarem sem serem as desenvolvedoras. <br>

Copyright ©️ Anny, Camila, Leticia e Luana.