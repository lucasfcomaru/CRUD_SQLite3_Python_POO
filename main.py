from classes import Produto
import funcoes as fc

# Menu principal
while True:
    print("-" * 10, "GESTÃO DE ESTOQUE", "-" * 10)
    print("1 - Cadastrar novo produto")
    print("2 - Consultar produtos")
    print("3 - Editar produto")
    print("4 - Remover produto")
    print("0 - Encerrar programa")

    op_menu = input("Escolha a opção desejada: ")

    if op_menu == "1":
        while True:
            try:
                nome = input("Informe o nome do produto: ")
                quantidade = int(input("Informe a quantidade do produto: "))
                preco = float(input("Informe o preço do produto: "))
            except:
                print("Por favor, digite um valor válido.")
            else:
                # Criando o objeto com os parâmetros.
                produto = Produto(nome, quantidade, preco)
                # Método que vai adicionar um produto ao banco de dados
                produto.add_produto()

                # Condição para permancecer dentro do cadastro
                novo_cadastro = input("Deseja realizar um novo cadastro? [Y/N] ")
                if novo_cadastro in "Yy":
                    continue
                elif novo_cadastro in "Nn":
                    print("Voltando para o menu principal.")
                    break

    elif op_menu == "2":
        try:
            fc.consultar_produto()
        except:
            print("Algo deu errado. Tente novamente.")
        else:
            continue

    elif op_menu == "3":
        while True:
            # menu
            print("CAMPOS DISPONÍVEIS")
            print("1 - Nome")
            print("2 - Quantidade")
            print("3 - Preço")
            print("0 - Voltar")

            try:
                op_editar = int(input("Informe o campo que deseja editar: "))
                valor_antigo = input("Informe o valor que deseja substituir: ")
                valor_novo = input("Informe o valor novo: ")
            except ValueError:
                print("Digite um valor válido.")
            else:
                # função para editar os campos do banco de dados
                fc.editar_produto(op_editar, valor_novo, valor_antigo)

                # Condição para permancecer dentro do menu de edição
                novo_cadastro = input("Deseja realizar um nova edição? [Y/N] ")
                if novo_cadastro in "Yy":
                    continue
                elif novo_cadastro in "Nn":
                    print("Voltando para o menu principal.")
                    break

    elif op_menu == "4":
        while True:
            nome_produto = input("Informe o nome do produto que deseja remover: ")
            fc.remove_produto(nome_produto)

            # Condição para permancecer dentro do menu de remoção
            novo_cadastro = input("Deseja realizar um nova remoção? [Y/N] ")
            if novo_cadastro in "Yy":
                continue
            elif novo_cadastro in "Nn":
                print("Voltando para o menu principal.")
                break

    elif op_menu == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Digite uma opção válida.")
