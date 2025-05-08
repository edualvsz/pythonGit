import os
os.system ("cls")
#IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
#ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO


# NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")

#ATIVIDADE MEDIA

# n1 = float(input("digite a 1 nota: "))
# n2 = float(input("Digite a 2 nota: "))
# media = (n1+n2)/2

# if media < 5:
#     print("reprovado")
# elif media < 5 <7:
#     print("em recuperacao")
# elif media < 7:
#     print("aprovado")
# else: 
#     print("aprovado")

#ATIVIDADE PESO:

# peso = float(input("digite o seu peso: "))
# altura = float(input("Digite a sua altura: "))
# imc = peso / (altura * altura)
# print(f"seu IMC é:  , {imc :.2f}")

# if imc < 17:
#     print("muito abaixo do peso")
# elif imc >= 17 <=18.49:
#     print("abaixo do peso")
# elif imc >= 18.5 <=24.99:
#     print("peso normal")
# elif imc >= 25 <=29.99:
#     print("acima do peso")
# elif imc >= 30 <=34.99:
#     print("obesidade 1")
# elif imc  >= 35 <=39.99:
#     print("obesidade 2")
# else: 
#     print("obesidade 3")

#ATIVIDADE DO SALARIO:

# print(r"""
      
    
#                        ____________________                              
#                      //|           |        \                            
#                    //  |           |          \                          
#       ___________//____|___________|__________()\__________________      
#     /__________________|_=_________|_=___________|_________________{}    
#     [           ______ |           | .           | ==  ______      { }   
#   __[__        /##  ##\|           |             |    /##  ##\    _{# }_ 
#  {_____)______|##    ##|___________|_____________|___|##    ##|__(______}
#              /  ##__##                              /  ##__##        \   

# """)

# print("="*25 , "AUTOCAR" , "="*40)
# print(" " \
# "\nSalários até R$ 2799,99 :aumento de 20%;"
# "\nSalários entre R$ 2800,00 e R$6999,99: aumento de 15%" \
# "\nSalários entre R$ 7000,00 e R$ 14999,99: aumento de 10%;" \
# "\nSalários de R$ 15000,00 em diante: aumento de 5%")



# salario = float(input("digite o seu salario: "))

# valoraumento1= 0.20* salario
# valoraumento2= 0.15* salario 
# valoraumento3= 0.10* salario
# valoraumento4= 0.05* salario

# if salario < 2799.99:
#     print("Você recebeu um aumento: " , 0.20 * salario)

# elif salario >=2800.00 and salario <6999.99:
#     print("Você recebeu um aumento: " , 0.15 * salario)
# elif salario>=7000.00 and salario <14999.99:
#     print("Você recebeu um aumento: " , 0.10 * salario)
# elif salario>=15000.00:
#     print("Você recebeu um aumento: " , 0.05 *salario)

# print("Salario antes do reajuste: " , salario)


