# 1.	Faça um código que leia 3 valores inteiros e positivos, 
# encontre o maior e o menor valor lidos, calcule a média dos números lidos e mostre os resultados

while True:
    
    a = float(input('A:'))
    b = float(input('B:'))
    c = float(input('C:'))

    maior = max(a,b,c)
    menor = min(a,b,c)
    media = (a+b+c) / 3 

    print('Maior valor = ', maior)
    print('Menor valor = ', menor)
    print('Média = ', media)

    exit=str(input('para sair digite exit'))
    if exit == 'exit' :
        break

