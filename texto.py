from random import *
from time import *

consoantes=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z',' ',',','.',';','~']
vogais=['a','e','i','o','u']
letras=consoantes+vogais

while True:
    comprimento=0
    texto=''
    extensões=['.pe','.elf']
    while comprimento<randint(20,200):
        if comprimento % 2 ==0:
            texto+=consoantes[randint(0,len(consoantes)-1)]
        else:
            texto+=vogais[randint(0,len(vogais)-1)]
        comprimento+=1
    sleep(1)
    arquivo=texto+extensões[randint(0,1)]
    print(arquivo)
    comprimento=0
    senha=''
    while comprimento<randint(20,200):
        binario=randint(0,1)
        if binario==0:
            senha+=str(randint(0,9))
        else:
            senha+=str(letras[randint(0,len(letras)-1)])
        comprimento+=1
    sleep(1)
    print(f'a senha do arquivo {arquivo} é\n{senha}')
    conteudo=''
    comprimento=0
    sleep(1)
    while comprimento<randint(0,90000):
        conteudo+=str(randint(0,1))
        comprimento+=1
    print(f"e o conteúdo de {arquivo} é \n{conteudo}\n")