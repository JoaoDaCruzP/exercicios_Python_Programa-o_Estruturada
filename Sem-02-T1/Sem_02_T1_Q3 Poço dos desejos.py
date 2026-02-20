# ATIVIDADE SEMANA 02 - T1 - Q3

#Voce encontrou um poço dos desejos, mas ele so realiza desejos que envolvem matematica! Peça ao usuario par inserir o valor encontrando no poço. Agora calcule quantas moedas de R$0.25, somam o valor no poço sem ultrapassar o total encontrado.

valor_encontrado = 0

while True:
    valor = input('Digite o que você encontrou no poço: ')
    try:
        valor = int(valor)
        print('valor adicionado com sucesso\n')
        break
    except:
        print('Não é Permitido "letras" nem numeros com "Ponto" ou "virgula"')
        print('vamos tentar novamente\n')
        
valor_encontrado = int(valor) / 0.25

print(f'O valor encontrado pode ser trocado por {valor_encontrado} moedas de R$0.25 centavos')