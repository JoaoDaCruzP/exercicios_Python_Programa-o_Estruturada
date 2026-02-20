# ATIVIDADE SEMANA 02 - T1 - Q4

'''Um dragão come exatamente meia ovelha por dia. Pergunte ao usuário por quantos dias o dragão está solto. Calcule
quantas ovelhas ele já comeu nesse tempo!'''

while True:
    #recebe a entrada do usuario e remove os espaços em branco
    dias = input('O dragão está solto a quantos dias?: ').strip()
    #faz uma primeira verificação, se o valor é inteiro, se o valor nao é negativo ou zero
    try:
        dias = int(dias)
        
        if dias < 0:
            print('Não da para voltar no tempo!')
            continue
        elif dias == 0:
            print(f'O dragão nao comeu ovelhas ainda!')
            continue
        else:
            if dias == 1:
                print(f'o dragão comeu meia ovelha')
                break
            
        #faz a operação para obter um numero inteiro e um resto respectivamente
        ovelha_inteira = dias //2    
        meia_ovelha = dias % 2

        #atribui singular pra 1 ovelha e plural para mais de uma ovelha inteira
        singular = "ovelha" if ovelha_inteira == 1 else "ovelhas"
        #so mostra "meia" se houver resto na operação "meia_ovelha" acima
        meia = " e meia " if meia_ovelha == 1 else ""
        
        print(f'O dragão comeu {ovelha_inteira} {singular}{meia} em {dias} dias')
        
        #verifica se o print acima é compativel com a saida da operação e sai do laço
        print(f'{ovelha_inteira}, {meia_ovelha}')
        break
    except:
        #tratamento de erro caso a entrada não seja apenas numeros inteiros e retorna pro laço
        print('Não é Permitido "letras" nem numeros com "Ponto" ou "virgula"')
        print('vamos tentar novamente\n')

