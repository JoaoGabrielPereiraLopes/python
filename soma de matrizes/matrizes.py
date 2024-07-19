def soma_de_matriz(matriz1,matriz2):
    limite=len(matriz1)
    y=0
    resultado=[]
    while y<limite:
        limite2=len(matriz2[y])
        x=0
        linha=[]
        while x<limite2:
            linha+=[matriz1[y][x]+matriz2[y][x]]
            x+=1
        resultado+=[linha]
        y+=1
    return resultado
entrada1=[]
escolha=''
while escolha!='sair':
    linha=[]
    for x in input('numeros separados por espaço: ').split():
        linha+=[int(x)]
    entrada1+=[linha]
    escolha=input()
entrada2=[]
escolha=''
while escolha!='sair':
    linha=[]
    for x in input('numeros separados por espaço').split():
        linha+=[int(x)]
    entrada2+=[linha]
    escolha=input('quer sair ("sair" para sair): ')
texto=''
print('o resultado será:')
for x in soma_de_matriz(entrada1,entrada2):
    for y in x:
        texto+=str(y)+' '
    print(texto)
    texto=''