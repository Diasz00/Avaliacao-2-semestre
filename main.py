import csv
import os

NOME_ARQUIVO = "livros.csv"

def carregar_livros():
    # Lê o arquivo CSV e retorna uma lista de dicionários com os livros.
    if not os.path.exists(NOME_ARQUIVO):
        return []

    with open(NOME_ARQUIVO, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)

def salvar_livros(livros):
    # Sobrescreve o arquivo CSV com a lista atualizada de livros.
    campos = ["Titulo", "Autor", "Ano", "Isbn", "Status"]
    with open(NOME_ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(livros)

def cadastrar_livro():
    print("\n===== CADASTRO DE LIVRO =====")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    ano = input("Ano de publicação: ").strip()
    isbn = input("ISBN: ").strip()

    if not titulo or not isbn:
        print("Erro: Título e ISBN são obrigatórios.")
        return

    livros = carregar_livros()
    novo_livro = {
        "Titulo": titulo,
        "Autor": autor,
        "Ano": ano,
        "Isbn": isbn,
        "Status": "Disponível"
    }
    
    livros.append(novo_livro)
    salvar_livros(livros)
    print(f"\nLivro '{titulo}' cadastrado com sucesso!")

def listar_livros():
    print("\n===== LISTA DE LIVROS =====")
    livros = carregar_livros()

    if not livros:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros:
        print(f"Título: {livro['Titulo']} | Autor: {livro['Autor']} | Ano: {livro['Ano']} | ISBN: {livro['Isbn']} | Status: {livro['Status']}")

def buscar_livros():
    print("\n===== BUSCAR LIVRO =====")
    termo = input("Digite o título ou autor: ").lower().strip()
    
    if not termo:
        return

    livros = carregar_livros()
    resultados = [
        l for l in livros 
        if termo in l["Titulo"].lower() or termo in l["Autor"].lower()
    ]

    if resultados:
        print(f"\nEncontrado(s) {len(resultados)} livro(s):")
        for l in resultados:
            print(f"- {l['Titulo']} (Autor: {l['Autor']}) [{l['Status']}]")
    else:
        print("Nenhum livro encontrado.")

def alterar_status(novo_status):
    print(f"\n===== REGISTRAR {novo_status.upper()} =====")
    termo = input("Digite o ISBN ou Título do livro: ").lower().strip()
    
    if not termo:
        return

    livros = carregar_livros()
    encontrado = False

    for livro in livros:
        if termo == livro["Isbn"].lower() or termo in livro["Titulo"].lower():
            encontrado = True
            if livro["Status"] == novo_status:
                print(f"O livro '{livro['Titulo']}' já consta como '{novo_status}'.")
            else:
                livro["Status"] = novo_status
                salvar_livros(livros)
                print(f"Sucesso! O status de '{livro['Titulo']}' foi alterado para '{novo_status}'.")
            break

    if not encontrado:
        print("Livro não encontrado.")

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
        cadastrar_livro()
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        buscar_livros()
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