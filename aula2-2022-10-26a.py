# comando input(): entrada, permite que o usuário digite algo
nome = input("Digite o seu nome: ")

# comando print(): saída, permite que o programa devolva algo, exibe
print(f"Boa noite, seu nome é {nome}.")

# exercício
idade = int(input("\nDigite a sua idade: "))
print(f"{nome}, a sua idade é {idade}.")

# para mostrar o dobro da idade informada
dobro = idade*2
print("\nO dobro da idade informada é {}.".format(dobro))

# estrutura condicional: "se" (if)
if (idade >= 18):
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir.")
else:
  print("Você é menor de idade.")

# perguntar gênero (M = masculino, F = feminino) e se precisou prestar o serviço militar obrigatório

genero = input("\nInforme o seu gênero, sendo M = Masculino, F = Feminino, O = Outros: ")
if (idade >= 18 and genero == "M"):
  print("Você deve prestar ou já prestou o serviço militar obrigatório.")
# o else não é obrigatório para o "if"
else:
  print("Você não precisa/precisou prestar o serviço militar obrigatório (ainda rs).")