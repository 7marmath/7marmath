# Qual é o possivel enunciado para o fluxograma apresentado a  seguir: ( inicio) ►
# Acrescentar uma estrutura de repetição para interromper quando for digitada zero para c1 e c2 
# import math sqrt

import math
while True :
    c1=int(input("c1: "))
    c2=int(input("c2: "))
    c3 = (c1*c1)+(c2*c2)
    h= math.sqrt(c3)    
    if h == 0 :        
        break
    print('Hipotenusa', h)


