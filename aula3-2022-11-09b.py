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
  imposto = preco_produto * 0.07
  return imposto

# Imposto a calcular e exibir
preco = 299
imposto = calcular_imposto(preco)
print(f"Esse aqui é com a função (7%): {imposto}")

# Explicação de variável local x global
print(preco)
preco_produto = 100
print(preco_produto)

# Agora calcular imposto, a alíquota agora é 7%
valores = [1.99, 24.50, 78.27, 1515.5]

# Se quiser calcular o imposto destes quatro valores e exibir na tela: "O imposto de .... é ...." (1o. preço, 2o. imposto)
print(f"O imposto de {valores} é {calcular_imposto(valores)}")

