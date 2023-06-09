# Tiana, a Inteligência Artificial.
## O que é?
Projeto de Python criado para a Challenge da @FIAP em parceria com a IBM para as aulas de Computational Thinking With Python.

## Quem compõe esse projeto?

Esse projeto está sendo construído por 4 programadoras, sendo elas:

<a href="https://github.com/anny-dias">Anny Diaz</a>
<a href="https://github.com/camilapadalino">Camila Padalino</a>
<a href="https://github.com/letyresina">Leticia Resina</a>
<a href="https://github.com/Luanacabezaolias">Luana Cabeazolias</a>

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
Foi também criado uam pasta de "testes", para testes a parte de alguma funcionalidade antes de jogar no arquivo final.
<ul>
<li>Versão 1.0: Último commit feito no dia 11 de abril de 2023. Essa versão conta com uma saudação padrão da IA, que logo em seguida questiona se o usuário deseja ou não participar da entrevista, trabalhando com match case, ifs e elses. E por fim, agradece o usuário por participar da entrevista e deixou espaço para mais implementações futuras. </li>
<li>Versão 2.0: Último commit feito no dia 18 de maio de 2023. Essa versão conta com uma função de menu de opções, para facilitar a execução do programa. Também foi adicionado um While de Loop infinito, para que o usuário possa utilizar das funções até que decida encerrar a execução. Foram feitas melhorias na própria entrevista, deixando numa linguagem mais compreensível para o usuário. Na parte da entrevista de caso a pessoa dirija, foi feito uma função que armazena uma lista, que a quantidade de valores é a informada pelo próprio usuário para facilitar. Nessa versão, foi feito um pontapé da opção 2, onde o usuário informa um problema em alguma avenida, rua ou rota, indicando se há acidente ou trânsito que a IA não pode captar no momento. Isso seria repassado para os usuários que buscassem determinada rota, e avisaria pro usuário que, caso ele desejasse rotas alternativas, seguisse para a opção, que viria logo em seguida, por conta do looping. A última implementação adicionada simula a adição e visualização de rotas favoritas -> essa implementação está sujeita a mudanças futuras, uma vez que, somente com o Login, o usuário poderá ter essa opção. Nesse caso, fizemos uma simulação para a entrega da Sprint 2.</li>
</ul>