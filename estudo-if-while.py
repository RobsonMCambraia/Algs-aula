# Escreva um código em que o correntista digite um valor para empréstimo e o sistema decida se foi aprovado ou não.
# Regras:
# O número de parcelas permitidas deve variar de 10 a 24x
# O valor máximo de cada parcela não pode ultrapassar 30% da aposentaria do correntista
# O débito ao contratar o empréstimo será 60% a mais do valor solicitado
# Informações:
# Valor da aposentadoria do correntista: R$ 1.832,50

valor_aposentadoria = 1832.50


while True:

    valor_emprestimo = float(input("Digite o valor do emprestimo desejado: "))

    total_emprestimo = valor_emprestimo*1.6

    

    print("Você pode parcelar seu empréstimo de, no mínimo, 10 vezes, sendo parcelado máximo de 24 vezes.")

    print(f"O valor total do seu empréstimo contém um juros de 60% sobre o valor, totalizando R$ {valor_emprestimo*1.6}.")

    

    print("")

    print("-"*50)

    print(f"Você deve escolher uma parcela maior que {valor_aposentadoria*0.3} ")

    print("As parcelas do seu empréstimo podem ser de:")

    print(f"10 vezes de R$ {total_emprestimo/10}")

    print(f"11 vezes de R$ {total_emprestimo/11}")

    print(f"12 vezes de R$ {total_emprestimo/12}")

    print(f"13 vezes de R$ {total_emprestimo/13}")

    print(f"14 vezes de R$ {total_emprestimo/14}")

    print(f"15 vezes de R$ {total_emprestimo/15}")

    print(f"16 vezes de R$ {total_emprestimo/16}")

    print(f"17 vezes de R$ {total_emprestimo/17}")

    print(f"18 vezes de R$ {total_emprestimo/18}")

    print(f"19 vezes de R$ {total_emprestimo/19}")

    print(f"20 vezes de R$ {total_emprestimo/20}")

    print(f"21 vezes de R$ {total_emprestimo/21}")

    print(f"22 vezes de R$ {total_emprestimo/22}")

    print(f"23 vezes de R$ {total_emprestimo/23}")

    print(f"24 vezes de R$ {total_emprestimo/24}")

    

    while True:

        parcelas = int(input("Em quantas parcelas você deseja que seja dividido o seu empréstimo? "))

        if parcelas >= 10 and parcelas <= 24 and (total_emprestimo/parcelas) > valor_aposentadoria*0.3:

            print(f"o empréstimo no valor de R$ {total_emprestimo} será parcelado em {parcelas} vezes, de R$ {total_emprestimo/parcelas} .")

            if input("Confirmar operação? (S/N)").lower() == "s":

                print("Operação realizada com sucesso!")

                break

        else:

            print("Número de parcelas não permitido.")

            break

    novo_emprestimo = input("Deseja continuar? (S/N)").lower()

    if novo_emprestimo == "n":

        print("Encerrando aplicação.")

        break
