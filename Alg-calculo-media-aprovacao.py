#Algoritmo para cálculo de média, com base na nota do aluno, e aprovação.
aprovados = 0
reprovados = 0
alunos_cadastrados = 0

while input("Deseja cadastrar uma nota? (s/n) ").lower() == "s":
  alunos_cadastrados += 1
  aluno = input("Digite o nome do aluno: ")
  np1 = float(input("Digite nota NP1: "))
  np2 = float(input("Digite nota NP2: "))
  med = (np1 + np2)/2

  if med >= 7:
    print(f"Aluno {aluno} passou com media: {med}.\n")
    aprovados += 1

  elif med >= 4:
    print(f"Aluno {aluno} ficou de recuperação com media: {med}.")
    nr = float(input("Digite nota Nota Final: "))
    med_f = (med + nr)/2

    if med_f >= 7:
      print(f"Aluno {aluno} aprovado com media final: {med_f}.\n")
      aprovados += 1

    else:
      print(f"Aluno {aluno} reprovado com media final: {med_f}.\n")
      reprovados += 1

  else:
    print(f"Aluno {aluno} reprovado com media: {med}.\n")
    reprovados += 1
 
print("\nSistema encerrado.") 
print(f"Numero de notas lançadas: {alunos_cadastrados}.")
print(f"Numero de alunos aprovados: {aprovados}.")
print(f"Numero de alunos reprovados: {reprovados}.")

taxa_aprovacao = aprovados / alunos_cadastrados

print(f"Taxa de aprovação: {taxa_aprovacao*100}%.")
