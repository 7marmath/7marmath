# Faça um algoritmo (fluxograma e codifique em Python) auxiliar no controle de qualidade de uma fábrica de pisos,
# Imprimindo os números das peças reprovadas, bem como o total de peças aprovadas e reprovadas no final do dia. 
# Considere que a fábrica tem uma linha de produção capaz de produzir 800 peças por dia e para controlar a 
# qualidade deve-se cadastrar o número da peça e o seu estado (aprovado ou reprovado).

print('contagem de peças')
aprovado=0
reprovado=0
while True:
    status= input('Para aprovado 1 , Para reprovado 2:  , 3 para sair')
    if status == '1' :
        aprovado +=1
    elif status == '2' :
        reprovado +=1
    elif status  == 3 :
        break
    elif (aprovado+reprovado) > 800 :
        print('Limite de 800 peças atingido.')
        break
    print('Peças aprovadas : ', aprovado)
    print('Peças reprovadas : ', reprovado)
            