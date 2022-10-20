# Primeiro projeto Python :)
#
# comentário em linha
'''
comentário em bloco
'''
# print() = comando de saída
print("Hello world!")

# para guardar String (frase):
nome = "Giovana da Silveira"
# para guardar número inteiro:
quantidade = 28

# exibindo:
print(nome)
print(quantidade)

# quando quiser exibir a frase "A quantidade é " completando com o conteúdo da variável "quantidade":
print("A quantidade é "+str(quantidade))
print(f"A quantidade é {quantidade}")
print("A quantidade é {}".format(quantidade))

# quando quiser exibir uma frase com duas variáveis usando o ".format":
print("Meu nome é {} e tenho {} maçãs".format(nome, quantidade))