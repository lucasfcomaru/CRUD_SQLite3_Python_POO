import sqlite3 as sql # Biblioteca para conectar com banco de dados

# Deletar
def remove_produto(nome_produto):
    try:
        # Criando o banco de dados e se conectando
        banco = sql.connect("banco_dados.db")
        # criando o cursor para executar comandos no banco de dados
        cursor = banco.cursor()
        # deletando dados na tabela
        cursor.execute("DELETE FROM produtos WHERE nome = '{}'".format(nome_produto))

        # Verificando o número de linhas afetadas
        if cursor.rowcount == 0:
            print("Nenhuma linha foi deletada. O nome não foi encontrado na tabela.")

        # commit para salvar as informações no banco de dados
        banco.commit()

    except sql.Error as erro:
        print(f"Erro ao excluir: {erro}.")
    else:
        print("Produto deletado com sucesso.")
    finally:
        # fechando cursor e conexão
        cursor.close()
        banco.close()

# Atualizar
def editar_produto(opcao, valor_novo, valor_antigo):
    try:
        # Criando o banco de dados e se conectando
        banco = sql.connect("banco_dados.db")
        # criando o cursor para executar comandos no banco de dados
        cursor = banco.cursor()

        while opcao <= 3:
            # para saber qual campo da tabela será alterado
            if opcao == 1:
                # atualizando dados no nome
                cursor.execute("UPDATE produtos SET nome = '{}' WHERE nome = '{}'" .format(valor_novo, valor_antigo))
                # Verificando o número de linhas afetadas
                if cursor.rowcount == 0:
                    print("Nenhuma linha foi alterada. O valor não foi encontrado na tabela.")
                else:
                    print("Produto alterado com sucesso.")
                break
            elif opcao == 2:
                # atualizando dados na quantidade
                cursor.execute("UPDATE produtos SET quantidade = {} WHERE quantidade = {}".format(valor_novo, valor_antigo))
                # Verificando o número de linhas afetadas
                if cursor.rowcount == 0:
                    print("Nenhuma linha foi alterada. O valor não foi encontrado na tabela.")
                else:
                    print("Produto alterado com sucesso.")
                break
            elif opcao == 3:
                # atualizando dados no preco
                cursor.execute("UPDATE produtos SET preco = {} WHERE preco = {}".format(valor_novo, valor_antigo))
                # Verificando o número de linhas afetadas
                if cursor.rowcount == 0:
                    print("Nenhuma linha foi alterada. O valor não foi encontrado na tabela.")
                else:
                    print("Produto alterado com sucesso.")
                break
            else:
                break

        # commit para salvar as informações no banco de dados
        banco.commit()

    except sql.Error as erro:
        print(f"Erro ao excluir: {erro}.")

    finally:
        # fechando cursor e conexão
        cursor.close()
        banco.close()

# Consultar
def consultar_produto():
    try:
        # Criando o banco de dados e se conectando
        banco = sql.connect("banco_dados.db")
        # criando o cursor para executar comandos no banco de dados
        cursor = banco.cursor()
        # executa uma consulta na tabela produtos
        cursor.execute("SELECT * FROM produtos")
        # Obtendo todos os resultados
        resultados = cursor.fetchall()
        # Loop para trazer o resultado da consulta
        for linha in resultados:
            print(f"\nNome: {linha[0]} \nQuantidade: {linha[1]} \nPreço: {linha[2]}")
            print("-" * 10)

    except sql.Error as erro:
        print(f"Erro ao consultar tabela: {erro}.")
    else:
        print("Consulta feita com sucesso.")
    finally:
        # fechando cursor e conexão
        cursor.close()
        banco.close()