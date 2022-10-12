# O jogador vai digitar o numero da sorte e o valor a depositar
# Ao iniciar o jogo, a maquina ira ficar sorteando automaticamente ate o jogador acertar ou acabar o saldo
# Caso o jogador acerte o numero ira ganhar um premio de 50% do valor do saldo
# A cada jogada o sistema ira tirar do saldo 10% do valor apostado

import random as rd

numeros_sorteado = []
count = 0
num_sorte = int(input("Digite o seu numero da sorte: "))
valor_deposito = int(input("Digite o valor do credito: "))

saldo = valor_deposito
aposta = valor_deposito*0.1
cont = True
premio = 1.5

while cont:
  if saldo < aposta:
    print("Saldo insuficiente!")
    break

  saldo -= aposta
  sorteio = rd.randint(0, 10)
  numeros_sorteado.append(sorteio)
  #print("Numero sorteado", sorteio)
  count += 1

  if sorteio == num_sorte:
    #Olhar para o lucro atual
    saldo *= premio
    print("Voce ganhou, seu saldo e R$", saldo)
    if input("Deseja continuar? Seu premio sera aumentado em 10% (s/n): ").lower() == 'n':
      cont = False
    else:
      num_sorte = int(input("Digite o seu numero da sorte: "))
      premio += 0.1
    
print("")
print("-"*50)
print("Valor do credito inicial: R$", valor_deposito)
print("Valor da aposta: R$ {:.2f}".format(aposta))
print("Quantidade de sorteios:", count)
print("Numeros sorteados:", numeros_sorteado)
print("Saldo final: R$", saldo)
