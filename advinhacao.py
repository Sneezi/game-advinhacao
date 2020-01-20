import random

def jogar():
  #imprimindo cabeçalho bonito no jogo
  print("\n")
  print("          P  /_\\  P                              ")
  print("         /_\\_|_|_/_\\                            ")
  print("     n_n | ||. .|| | n_n         Bem vindo ao     ")
  print("     |_|_|nnnn nnnn|_|_|     Jogo de Adivinhação! ")
  print("    |\" \"  |  |_|  |\"  \" |                     ")
  print("    |_____| ' _ ' |_____|                         ")
  print("          \\__|_|__/                              ")
  print("\n")

  numero_secreto = random.randrange(1,101) #definindo o número random para nosso número secreto
  total_de_tentativas = 0
  pontos = 1000 #inicializando nossos pontos

  print("Qual o nível de dificuldade? {}".format(numero_secreto))
  print("(1) Fácil (2) Médio (3) Difícil")

  nivel = int(input("\nDefine o nível: ") )
  #definindo a quantidade de tentativas de acordo com o nível
  if(nivel == 1):
    total_de_tentativas = 20
  elif(nivel == 2):
    total_de_tentativas = 10
  else:
    total_de_tentativas = 5
  # um laço de repetição que repete de acordo com o total de tentativas
  for rodada in range(1, total_de_tentativas + 1):
    print("\n-> Tentativa de {} de {}".format(rodada,total_de_tentativas) )
    chute = int(input("Chute um número entre 1 e 100: ") )

    if(chute < 1 or chute > 100): # um alerta caso digite um número menor que 1 ou maior que 100!
      print("Você deve digitar um número entre 1 e 100!")
      continue
    #guardando as expressões booleanas dentro da varíavel para que o if fique mais enxuto
    acertou = chute == numero_secreto
    maior   = chute >  numero_secreto
    menor   = chute <  numero_secreto 

    if(acertou): #condição para verificar se o usuário acertou o número secreto
      break
    elif(maior):
      print("\nSeu chute foi maior que o número secrero")
    elif(menor):
      print("\nSeu chute foi menor que o número secrero")
    
    #cálculo dos pontos    
    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos

  if(acertou):
      print("\n\n             OOOOOOOOOOO               ") #imprimindo uma imagem para o jogador vencedor
      print("         OOOOOOOOOOOOOOOOOOO           ")
      print("      OOOOOO  OOOOOOOOO  OOOOOO        ")
      print("    OOOOOO      OOOOO      OOOOOO      ")
      print("  OOOOOOOO  #   OOOOO  #   OOOOOOOO    ")
      print(" OOOOOOOOOO    OOOOOOO    OOOOOOOOOO   ")
      print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  ")
      print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  ")
      print("OOOO  OOOOOOOOOOOOOOOOOOOOOOOOO  OOOO  ")
      print(" OOOO  OOOOOOOOOOOOOOOOOOOOOOO  OOOO   ")
      print("  OOOO   OOOOOOOOOOOOOOOOOOOO  OOOO    ")
      print("    OOOOO   OOOOOOOOOOOOOOO   OOOO     ")
      print("      OOOOOO   OOOOOOOOO   OOOOOO      ")
      print("         OOOOOO         OOOOOO         ")
      print("             OOOOOOOOOOOO              \n")
      print("Parabéns! Você acertou!")
      print("Você fez {} pontos. Até a próxima!\n".format(pontos) )
  else: 
    print("\n\n       \\|/ ____ \\|/    ")  #imprimindo uma imagem para o jogador perdedor
    print("        @~/ ,. \\~@      ")   
    print("       /_( \\__/ )_\\    ")   
    print("          \\__U_/        \n")
    print("Você perdeu! Tente novamente!\n")  
  
  print("\n*** FIM DE JOGO ***\n")

if(__name__ == "__main__"): #executando o jogo toda vez que for acessado diretamente
  jogar()