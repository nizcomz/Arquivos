#Conhecimento básico de bancos de dados e SQL
#Descrição:
#Saber como conectar seu código Python a bancos de dados, executar comandos SQL básicos para inserir, consultar, atualizar e deletar informações.
#Exemplo prático:

import sqlite3
conexao = sqlite3.connect("meubanco.db")
cursor = conexao.cursor()
cursor.execute("CREATE TABLE usuario (id INTEGER, nome TEXT)")
conexao.commit()
conexao.closet() 