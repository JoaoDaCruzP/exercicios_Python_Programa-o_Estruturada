# ATIVIDADE SEMANA 02 - T1 - Q1

#Um mago precisa misturar duas substancias para criar uma poção. Peça ao usuario os dois volumes(em ml) e exiba o total da poção.

volume_1 = 0
volume_2 = 0
soma = 0

#ESTA VERSÃO NÃO UTILIZA FUNÇÃO
while True:
    # RECENDO O PRIMEIRO VALOR DIGITADO PELO USUARIO
    valor1 = input('Digite o Primeiro volume: ')
    # TESTA SE O VALOR É UM FLOAT OU INTEIRO
    try:
        volume_1 = float(valor1)
        print('Primeiro volume adicionado com sucesso')
        break 
    except:
        print('Tente usar apenas numeros e não use "virgula"')

while True:
    # RECENDO O SEGUNDO VALOR DIGITADO PELO USUARIO
    valor2 = input('Digite o Segundo volume: ')
    
    try:
        volume_2 = float(valor2)
        print('Segundo volume adicionado com sucesso')
        break       
    except:
        print('Tente usar apenas numeros e não use "virgula"')
        
#MOSTRA NA TELA O QUE ESTA GUARDADO NA RESPECTIVA VARIAVEL E SEU TIPO    
print(f'O primeiro volume é {volume_1}ml e é do tipo {type(volume_1)}')    
print(f'O segundo volume é {volume_2}ml e é do tipo {type(volume_2)}\n')

#REALIZA A OPERAÇÃO
soma = volume_1 + volume_2

#MOSTRA O RESULTADO
print(f'O resultado da soma dos dois volumes é {soma:.2f}ml')