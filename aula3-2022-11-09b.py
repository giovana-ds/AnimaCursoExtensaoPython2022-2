# Criação de funções

preco = 1999.90

# Calcular 5% de imposto, guardar na variável imposto e exibir na tela

imposto = preco * 0.05
print (imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

# Criar uma função calcular_imposto() para calcular o imposto de 5% e retornar ao usuário

def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

# Imposto a calcular e exibir
preco = 299
imposto = calcular_imposto(preco)
print(imposto)

