# comando input(): entrada, permite que o usuário digite algo
nome = input("Digite o seu nome: ")

# comando print(): saída, permite que o programa devolva algo, exibe
print(f"Boa noite, seu nome é {nome}")

# exercício
idade = int(input("\nDigite a sua idade: "))
print(f"{nome}, a sua idade é {idade}")

# para mostrar o dobro da idade informada
dobro = idade*2
print("\nO dobro da idade informada é {}".format(dobro))