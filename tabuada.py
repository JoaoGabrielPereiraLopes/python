fator=0
numero_de_tentativas=0
acertos=0
tabuada=int(input("qual a tabuada desejada: "))
limite=int(input("informe o limite: "))
while True:
    fator=0
    numero_de_tentativas=0
    while True:
        fator=fator+1
        numero_de_tentativas=numero_de_tentativas+1
        resposta=int(input(f"informe quanto : é {fator} x {tabuada}: "))
        if resposta == fator * tabuada:
            print("acertou continue nesse ritimo")
            acertos=acertos+1
        else:
            print(f"incorreto {fator}x {tabuada} = {tabuada * fator}")
        if numero_de_tentativas == limite:
            break
    escolha=input("desja continuar: ")
    if escolha.upper()=="SIM":
        tabuada=int(input("qual a tabuada desejada: "))
        limite=int(input("informe o limite: "))
    else:
        break