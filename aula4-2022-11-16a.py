import sqlite3

# estabelecer conexão com banco de dados
conexao = sqlite3.connect("dc_universe.db")

# criar um objeto do tipo cursor
cursor = conexao.cursor()

# comando sql do banco
sql = 'SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas'

# executar o comando sql no sqlite (no cursor)
cursor.execute(sql)

# exibir a consulta com todos os nomes de heróis e vilões do bc
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print (pessoa)

for pessoa in pessoas:
  print(f'Nome: {pessoa[1]} ({pessoa[3]})')
