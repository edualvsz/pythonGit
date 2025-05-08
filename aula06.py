import os
os.system("cls")
#ESTRUTURAS CONDICIONAIS IF ELSE (ELIF)
#SWITCH CASE -> (MATCH CASE) escolha caso (a partir da versão 3.10)
#match valor:
#  case valor:

# linguagem = 100

# match linguagem:

#     case "python":
#         print("é facil")
#     case "java":
#         print ("muito codigo, python faz com linhas menores")
#     case "c#":
#         print("massa")
#     case "js":
#         print("sou do back")
#     case "html":
#         print("kauan nao dorme")
#     case 10:
#         ("entrou aqui !")
#     case _:
#         print("outro caso")

#ATIVIDADE SEMANA

# print("1- segunda", "\n 2- terca", "\n 3- quarta", "\n 4- quinta", "\n 5- sexta", "\n 6- sabado", "\n 7- domingo")

# semana = int(input ("Que dia da semana é ?: "))

# match semana:

#     case 1:
#         print("segunda")
#     case 2:
#         print ("terca")
#     case 3:
#         print("quarta")
#     case 4:
#         print("quinta")
#     case 5:
#         print("sexta")
#     case 6:
#         ("sabado")
#     case 7:
#         print("domingo")

#ATIVIDADE CELULAR

# valor=0
# frete=0
# print(f"VALOR CELULAR:R$ {valor:.2f}")
# print(f"VALOR FRETE R$: {frete:.2f}")
# print(f"VALOR TOTAL R$: {valor+frete:.2f}")
# print(""" 
# MUNDO CELULAR
      
# 1-IPHONE -> 5000
# 2-MOTO G -> 3000
# 3-LENOVO -> 2500

# FRETE: 
#       SP -> 10,00
#       RS -> 20,00
#       RJ -> 30,00      
# """)

# celular = int(input("Digite a opção desejada: "))
# estado = input("Digite a sigla do estado para entrega: ").lower()
# valor=0
# frete=0
# valortotal=0
# match celular:
#     case 1:
#         valor=5000
#     case 2:
#         valor=3000
#     case 3:
#         valor=2500

# match estado:
#     case "sp":
#         frete=10
#     case "rs":
#         frete=20
#     case "rj":
#         frete=30

# valortotal= valor + frete

# print(f"VALOR CELULAR:R$ {valor:.2f}")
# print(f"VALOR FRETE R$: {frete:.2f}")
# print(f"VALOR TOTAL R$: {valor+frete:.2f}")

#RANDOM
# import random

# valor = 0
# #randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")

#ATIVIDADE PEDRA PAPEL TESOURA 

import random

desenhos = {
    "pedra": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "papel": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "tesoura": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

opcoes = ["pedra", "papel", "tesoura"]
usuario = input("Escolha pedra, papel ou tesoura: ").lower()
aleatorio = random.randint(0, 2)
computador = opcoes[aleatorio]

print(f"Você escolheu: {usuario}")

match usuario:
    case "pedra" | "papel" | "tesoura":
        print(desenhos[usuario])
    case _:
        print("Escolha inválida.")

print(f"Computador escolheu: {computador}")
print(desenhos[computador])

match (usuario, computador):
    case (a, b) if a == b:
        print("Empate!")
    case ("pedra", "tesoura") , ("papel", "pedra") , ("tesoura", "papel"):
        print("Você venceu!")
    case ("pedra", "papel") , ("papel", "tesoura") , ("tesoura", "pedra"):
        print("Você perdeu!")
        