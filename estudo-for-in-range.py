# Questão 01:
# Escreva um código que receba uma senha de usuário e caso este erre a senha 3x o programa irá entrar em bloqueio onde só será desbloqueado com a senha de administrador, retornando para a solicitação de senha de usuário.
# Caso a senha de usuária seja digitada corretamente o sistema encerra com mensagem de seja bem-vindo.
# Informações:
# senha de usuário cadastrada = "12a3b"
# senha de admin cadastrada = "9876"

user = input("Digite seu nome: ")

pass_user = '12a3b'
pass_adm = '9876'
acess = False


while True:
  for i in range(1,4):
    if pass_user == input("Digite a senha de usuário: "):
      print("Acesso liberado.")
      acess = True
      break
    else:
      tentativas = 3 - i 
      print(f"Senha errada. Você possui {tentativas} tentativas.")
      if tentativas == 0:
        print("Sem novas tentativas.")

  if acess == True:
        print(f"Seja bem vindo de volta, {user} !")
        break
  
  print("Você digitou a senha de usuário errada muitas vezes.")

  while True:
    if pass_adm == input("Por favor, digite a senha de administrador: "):
      print("Acesso verificado. Tente a senha de usuário novamente.")
      break
    else: 
      print("Acesso negado. Tente novamente.")
