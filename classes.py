import sqlite3 as sql # Biblioteca para conectar com banco de dados

class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    # criar
    def add_produto(self):
        try:
            # Criando o banco de dados e se conectando
            banco = sql.connect("banco_dados.db")
            # criando o cursor para executar comandos no banco de dados
            cursor = banco.cursor()
            # criar uma tabela se ela não existir
            cursor.execute("CREATE TABLE IF NOT EXISTS produtos (nome VARCHAR(100) NOT NULL, quantidade INT, preco FLOAT NOT NULL)")
            # inserir valores na tabela
            # deixar os valores fora para evitar vulnerabilidade de injeção de SQL
            cursor.execute("INSERT INTO produtos (nome, quantidade, preco) VALUES('{}', {}, {})" .format(self.nome, self.quantidade, self.preco))
            # commit para salvar as informações no banco de dados
            banco.commit()
            # fechar conexão com o banco
            banco.close()

        except sql.Error as erro:
            print(f"Erro ao cadastrar: {erro}.")
        else:
            print("Produto cadastrado com sucesso.")

