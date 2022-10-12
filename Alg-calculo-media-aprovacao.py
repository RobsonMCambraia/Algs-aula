#Algoritmo para cálculo de média, com base na nota do aluno, e aprovação.
while True:
  np1 = float(input("Digite nota NP1: "))
  np2 = float(input("Digite nota NP2: "))
  med = (np1 + np2)/2

  if med >= 7:
    print(f"Aluno passou com media: {med}.\n")
  elif med >= 4:
    print(f"Aluno de recuperação com media: {med}.")
    nr = float(input("Digite nota Nota Final: "))
    med_f = (med + nr)/2
    if med_f >= 7:
      print(f"Aluno aprovado com media final: {med_f}.\n")
    else:
      print(f"Aluno reprovado com media final: {med_f}.\n")
  else:
    print(f"Aluno reprovado com media: {med}.\n")

  cont = input("Deseja cadastrar outra nota? (s/n) ").lower()
  if cont == "n":
    print("Encerrando sistema")
    break
  
print("\nSistema encerrado.") 
