# ATIVIDADE SEMANA 02 - T1 - Q2
# Um robô coleta 12 peças por hora. Quantas peças ele terá coletado após certo número de horas?

horas = 0

while True:
    horas = input('Quantas horas você da para o Robô: ')
    #verifica se o primeiro valor é numero inteiro
    try:
        horas = int(horas)
        print('valor foi adicionado com sucesso\n')
        break
    except:
        print('o valor nao pode conter "letras"')
    
while True:
    minutos = input('Quantos minutos você da para o Robô: ')
    #verifica se o segundo valor é numero inteiro
    try:
        if len(minutos) < 2:
            print('precisa ter 2 digitos')  
        else:
            minutos = float(minutos)
            print('valor foi adicionado com sucesso\n')
            break
    except:
        print('o valor nao pode conter "letras"')
        
#executa as operações
coleta_p_hora = 12 * horas
coleta_p_minutos = 12 * (minutos / 60)
result_coleta = coleta_p_hora + coleta_p_minutos

print(f'em {horas}h:{minutos}min o Robô irá coletar {result_coleta:.0f} peças')
