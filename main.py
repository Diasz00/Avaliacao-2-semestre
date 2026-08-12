import csv
import os

NOME_ARQUIVO = "livros.csv"

def carregar_livros():
    """Lê o arquivo CSV e retorna uma lista de dicionários com os livros."""
    if not os.path.exists(NOME_ARQUIVO):
        return []

    with open(NOME_ARQUIVO, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)

def salvar_livros(livros):
    """Sobrescreve o arquivo CSV com a lista atualizada de livros."""
    campos = ["Titulo", "Autor", "Ano", "Isbn", "Status"]
    with open(NOME_ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(livros)


# Menu Principal
while True:
    print("\n===== MENU BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Empréstimo")
    print("5 - Devolução")
    print("6 - Ordenar lista")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        print("Cadastrando livro...")
    elif opcao == "2":
        print("Listando livros...")
    elif opcao == "3":
        print("Buscando livro...")
    elif opcao == "4":
        print("Realizando empréstimo...")
    elif opcao == "5":
        print("Realizando devolução...")
    elif opcao == "6":
        print("Ordenando lista...")
    elif opcao == "7":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")