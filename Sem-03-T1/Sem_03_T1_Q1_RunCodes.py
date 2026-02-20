# ATIVIDADE SEMANA 03 - T1 - Q1

'''01. Faça um programa que pergunte ao usuário quantas fatias de pizza tem e quantos amigos vão dividir a pizza. Mostre
quantas fatias cada um recebe e quantas sobram.'''

while True:
    # RECENDO O PRIMEIRO VALOR DIGITADO PELO USUARIO
    n1 = input()
    # TESTA SE O VALOR É UM FLOAT OU INTEIRO
    try:
        valor1 = int(n1)
        break 
    except:
        print('Tente usar apenas numeros e não use "virgula"')

while True:
    # RECENDO O SEGUNDO VALOR DIGITADO PELO USUARIO
    n2 = input()
    
    try:
        valor2 = int(n2)
    
        break       
    except:
        print('Tente usar apenas numeros e não use "virgula"')
        

#REALIZA A OPERAÇÃO
div_sem_resto = valor1 // valor2
resto = valor1 % valor2

print(div_sem_resto)
print(resto)
