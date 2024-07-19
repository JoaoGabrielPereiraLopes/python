print('legal')
from random import *
from time import *
print('legal')
def gerador():
    inicio=int(input())
    fim=int(input())
    tentativas=[]
    objetivo=str(fim)*(fim-inicio)
    print('legal')
    while True:
        senha=''
        senha+=str(randint(inicio+1,fim))+str(randint(inicio+1,fim))+str(randint(inicio+1,fim))+str(randint(inicio+1,fim))
        if senha not in tentativas:
            tentativas+=[senha]
        if senha==objetivo:
            break
    input(f'forma nessessario {len(tentativas)} execucoes')
gerador()
