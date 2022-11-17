import sqlite3

# função conectar()
def conectar():
  # estabelecer uma conexão com o banco de dados
  conexao = sqlite3.connect("dc_universe.db")

  # criar um objeto do tipo cursor
  cursor = conexao.cursor()

  return conexao, cursor 
