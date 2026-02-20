# ATIVIDADE SEMANA 02 - T1 - Q1

#Um mago precisa misturar duas substancias para criar uma poção. Peça ao usuario os dois volumes(em ml) e exiba o total da poção.

volume_1 = 0
volume_2 = 0

#ESTA VERSÃO UTILIZA DE FUNÇÃO
def valor_float():
    #LAÇO DE REPETIÇÃO
    while True:
        valor = input('digite aqui: ') #ENTRADA DO USUARIO
        try: #TESTA SE  O VALOR PODE SER UM FLOAT OU INTEIRO
            valor = float(valor)
            print('valor adicionado com sucesso\n')
            return valor
        except:
            print('valor so pode conter numeros, tente usar "ponto ao inves de virgula"')
            
#ATRIBUI O RESULTADO DA FUNÇÃO A VARIAVEL CORRESPONDENTE
print('Qual o primeiro volume?')
volume_1 = valor_float()
print('QUal o segundo volume?')
volume_2 = valor_float()

soma = volume_1 + volume_2 #FAZ A OPERAÇÃO 

#MOSTRA O RESULTADO
print(f'O resultado da soma dos dois volumes é {soma:.2f}ml')