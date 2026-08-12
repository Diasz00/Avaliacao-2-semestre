#Sistema de Gerenciamento de Biblioteca
Projeto em Python desenvolvido para gerenciar o acervo de uma biblioteca, permitindo realizar cadastro, consultas, ordenação e controle de empréstimos e devoluções de livros.

Como Executar o Programa
Certifique-se de ter o Python 3 instalado em sua máquina.

Clone este repositório ou baixe os arquivos para o seu computador.

Abra o terminal ou prompt de comando no diretório do projeto.

Execute o comando: python main.py

O arquivo livros.csv será criado automaticamente na pasta do projeto assim que o primeiro livro for cadastrado.

Principais Funcionalidades
Cadastro de Livros
Permite inserir novos livros no acervo solicitando título, autor, ano de publicação e código ISBN. Todos os novos registros iniciam com o status "Disponível".

Listagem de Livros
Exibe no console a lista completa dos livros armazenados com suas respectivas informações e status atual.

Busca de Livros
Realiza pesquisas por palavras-chave, filtrando os registros do acervo pelo título ou pelo nome do autor.

Registro de Empréstimos e Devoluções
Permite alterar o status de um livro específico para "Emprestado" ou "Disponível", validando a alteração para evitar duplicidades.

Ordenação da Listagem
Organiza os registros do acervo com base na escolha do usuário (por título, autor, ano de publicação ou ISBN) e atualiza o arquivo de dados.

Requisitos Técnicos Aplicados
Manipulação de Arquivos CSV
Aplicado nas funções carregar_livros() e salvar_livros(), utilizando o módulo nativo csv (DictReader e DictWriter) para salvar e ler os dados no arquivo livros.csv.

Verificação de Arquivos e Sistema
Aplicado com a função os.path.exists() na função carregar_livros() para verificar se o arquivo livros.csv já existe no computador antes de tentar abri-lo.

Estruturas de Dados (Dicionários e Listas)
Aplicado no armazenamento dos dados em memória, onde cada livro é representado por um dicionário com suas chaves (Titulo, Autor, Ano, Isbn, Status) e guardado em uma lista principal de livros.

Modularização com Funções
Aplicado na organização do código dividindo as responsabilidades em funções específicas (cadastrar_livro, listar_livros, buscar_livros, alterar_status e ordenar_listagem).

Controle de Fluxo e Validações
Aplicado no menu principal com o laço while True, na busca com estruturas condicionais (if/elif/else) e no percorrimento do acervo com o laço for.