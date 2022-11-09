# pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "Você é bixão, mesmo..."
nome = input("Qual o seu nome? ")
nota = float(input("Qual foi a sua nota? "))

if (nota == 10):
  print(f"\nParabéns, {nome}! Você é o bixão mesmo.")
elif(nota > 7 and nota < 10):
  print(f"\n{nome}, bom trabalho! Você passou.")
elif(nota == 7):
  print(f"\n{nome}, você passou na média.")
elif(nota < 7 and nota >= 0):
  print(f"\n{nome}, você reprovou.")
else:
  print("Insira um valor entre 0 e 10.")
  