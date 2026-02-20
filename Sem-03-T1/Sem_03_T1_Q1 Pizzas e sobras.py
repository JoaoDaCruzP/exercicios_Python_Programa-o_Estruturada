# ATIVIDADE SEMANA 03 - T1 - Q1

'''01. Faça um programa que pergunte ao usuário quantas fatias de pizza tem e quantos amigos vão dividir a pizza. Mostre
quantas fatias cada um recebe e quantas sobram.'''

while True:
    # RECENDO O PRIMEIRO VALOR DIGITADO PELO USUARIO
    n1 = input('Digite quantas fatias a pizza tem: ')
    # TESTA SE O VALOR É UM FLOAT OU INTEIRO
    try:
        valor1 = int(n1)
        break 
    except:
        print('Tente usar apenas numeros e não use "virgula"')

while True:
    # RECENDO O SEGUNDO VALOR DIGITADO PELO USUARIO
    n2 = input('Digite quantas pessoas vão comer a pizza: ')
    
    try:
        valor2 = int(n2)
    
        break       
    except:
        print('Tente usar apenas numeros e não use "virgula"')
        

#REALIZA A OPERAÇÃO
div_sem_resto = valor1 // valor2
resto = valor1 % valor2

singular_pizza = 'pedaço de pizza' if div_sem_resto <= 1 else 'pedaços de pizzas'
singular_resto = 'sobrará ' + str(resto) + ' pedaço' if resto <= 1 else 'sobrarão ' + str(resto) + ' pedaços'


#MOSTRA O RESULTADO
print(f'Dará {div_sem_resto} {singular_pizza} e {singular_resto}')