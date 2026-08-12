# Sistema de Gerenciamento de Biblioteca

Projeto em Python desenvolvido para gerenciar o acervo de uma biblioteca, permitindo realizar cadastro, consultas, ordenação e controle de empréstimos e devoluções de livros.

## Como Executar o Programa

1. Certifique-se de ter o Python 3 instalado em sua máquina.
2. Clone este repositório ou baixe os arquivos para o seu computador.
3. Abra o terminal ou prompt de comando no diretório do projeto.
4. Execute o comando:

```bash
python main.py

Principais Funcionalidades
Cadastro de Livros: Permite inserir novos livros no acervo solicitando título, autor, ano de publicação e código ISBN. Todos os novos registros iniciam com o status "Disponível".

Listagem de Livros: Exibe no console a lista completa dos livros armazenados com suas respectivas informações e status atual.

Busca de Livros: Realiza pesquisas por palavras-chave, filtrando os registros do acervo pelo título ou pelo nome do autor.

Registro de Empréstimos e Devoluções: Permite alterar o status de um livro específico para "Emprestado" ou "Disponível", validando se a alteração é cabível para evitar duplicidades.

Ordenação da Listagem: Organiza os registros do acervo com base na preferência do usuário (por título, autor, ano de publicação ou ISBN) e atualiza o arquivo de dados com a nova ordem.

Requisitos Técnicos Aplicados
Manipulação de Arquivos CSV: Aplicado nas funções de leitura e gravação de dados utilizando o módulo nativo csv (DictReader e DictWriter), garantindo a persistência dos registros no arquivo livros.csv.

Verificação de Arquivos e Sistema: Aplicado através do módulo os com a função os.path.exists(), utilizada para verificar a existência do arquivo de banco de dados antes de executar rotinas de leitura ou edição.

Estruturas de Dados: Aplicado no armazenamento dos dados em memória, utilizando dicionários para representar os campos de cada livro e listas para agrupar o acervo completo.

Modularização com Funções: Aplicado na divisão da regra de negócio em blocos reutilizáveis e organizados, como carregar_livros(), salvar_livros(), cadastrar_livro() e alterar_status().

Controle de Fluxo e Validações: Aplicado através de laços de repetição (while e for) para o menu interativo e percorrimentos de dados, além de estruturas condicionais (if, elif, else) para validação de entradas do usuário.