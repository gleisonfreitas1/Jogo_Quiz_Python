import requests
from tkinter import *

armazenamento = ["","","",0]

def jogo_quiz():
   print("================== ANIME QUIZ ==================\n")

   armazenamento[0] = input("Antes de começarmos por fazor informe o seu nome: \n")
   print("Seja bem vindo,",armazenamento[0], "ao nosso Anime Quiz.")
   armazenamento[1] = input("Vamos começar ? [S/N] ")

   if armazenamento[1] != "S" and armazenamento[1] != "s":
    quit()

   print("\nComeçando...\n")
   print("pergunta 1: ")
   print("Quem criou o golpe chamado Rasengan?: \n")
   print("A) Naruto Uzumaki")
   print("B) Kakashi Hatake")
   print("C) Sakura Haruno")
   print("D)    Minato Namikaze \n")
   armazenamento[2] = input("R:")

   if armazenamento[2] != "D" and armazenamento[2] != "d":
       print("\n Resposta incoreta")
       print(" A resposta correta é D) Minato Namikaze")
       print(" Proxima pergunta... \n")
   else:
       print("\n Resposta Correta")
       print(" Proxima perginta... \n")
       armazenamento[3] += int(10)

   print("pergunta    2: ")
   print("Quem criou o golpe chamado Chidory?: \n")
   print("A) Sasuke Uchiha")
   print("B) Madara Uchiha")
   print("C) Kakachi Hatake")
   print("D) Minato Namikaze \n")
   armazenamento[2] = input("R:")

   if armazenamento[2] != "C" and armazenamento[2] != "c":
      print("\n Resposta incoreta")
      print(" A resposta correta é C) Kakachi Hatake")
      print(" Proxima pergunta...")
   else:
      print("\n Resposta Correta")
      print(" Proxima perginta... \n")
      armazenamento[3] += int(10)

   print(armazenamento[3])

   print("pergunta 3: ")
   print("Quem criou o golpe chamado MultiClones das Sombras?: \n")
   print("A) Sasuke Uchiha")
   print("B)    Naruto Uzumaki")
   print("C) Tobirama Senju")
   print("D) Minato Namikaze \n")
   armazenamento[2] = input("R:")


   if armazenamento[2] != "C" and armazenamento[2] != "c":
      print("\n Resposta incoreta")
      print(" A resposta correta é C) Tobirama ")
      print(" Proxima pergunta... \n")
   else:
      print("\n Resposta Correta")
      print("Proxima perginta... \n")
      armazenamento[3] += int(10)

   print("pergunta 4: ")
   print("de que Cla vem o Sharinga?: \n")
   print("A) Cla Uchiha")
   print("B)    Cla Uzumaki")
   print("C) Cla Senju")
   print("D) Cla hyuga \n")
   armazenamento[2] = input("R:")

   if armazenamento[2] != "A" and armazenamento[2] != "a":
      print("\n Resposta incoreta")
      print(" A resposta correta é A) Cla Uchiha")
      print(" Proxima pergunta... \n")
   else:
     print("\n Resposta Correta")
     print("Proxima perginta... \n")
     armazenamento[3] += int(10)

   print("pergunta 5:")
   print("De que cla éra o primeiro Hokage?: \n")
   print("A) Cla Senju")
   print("B)    Cla Uchiha")
   print("C) Cla Nara")
   print("D) Cla Uzumaki \n")
   armazenamento[2] = input("R:")

   if armazenamento[2] != "A" and armazenamento[2] != "a":
       print("\n Resposta incoreta")
       print(" A resposta correta é A) Cla Senju")
       print(" Proxima pergunta...")
   else:
        print("\n Resposta Correta")
        print("Proxima perginta... \n")
        armazenamento[3] += int(10)

   print("Fim de Jogo.")
   print("A sua pontuação final é")

   if armazenamento[3] == 50:
       print("Pontuação: ",armazenamento[3],"/ 50")
       print("Parabéns você atingio uma pontuação perfeita.")
   elif armazenamento[3] < 50:
       print("Pontuação: ", armazenamento[3], "/50")
       print("quase la da proxima vez você consegue.")
   elif armazenamento[3] == 20:
       print("Pontuação: ", armazenamento[3], "/50")
       print("você acertou metade das questões")
   elif armazenamento[3] < 20:
       print("Pontuação: ", armazenamento[3], "/50")
       print("Sua Pontução foi muito baixa assista um pouco mais do anime.")

jogo_quiz()






