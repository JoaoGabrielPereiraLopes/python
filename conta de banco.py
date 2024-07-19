from arquivos import *

erro=False
nome = input("informe o seu nome: ")
agencia=input(f"{nome} informe a sua agencia: ")
try:
    agencia=int(agencia)
except:
    while True:
        try:
            agencia=int(agencia)
            break
        except:
            print('erro')
            agencia=input(f"{nome} informe a agencia: ")
conta=input(f'{nome} informe o numero da conta')
try:
    conta=int(conta)
except:
    while True:
        try:
            conta=int(conta)
            break
        except:
            print('erro')
            conta=input(f'{nome} informe o numero da conta: ')
try:
    nome_do_arquiv=str(nome)+".txt"
    linhas=carregaLinhaALinha(nome_do_arquiv)
    print(nome_do_arquiv)
    print(linhas)
    print(int(linhas[0]))
    if int(linhas[0])==agencia:
        print(int(linhas[1]))
        if int(linhas[1])==conta:
            print(float(linhas[2]))
            saldo=float(linhas[2])
        else:
            erro=True
    else:
        erro=True
except:
    saldo=0.0
finally:
    if erro==True:
        raise ValueError('informações erradas')
    while True:
        menu=input(f"""{nome}informe a sua ação:
            1. saque
            2. deposito
            3.transferencia""")
        if menu=='1':
            valor=input(f'{nome} seu saldo é igual a {saldo}\ninforme o valor da operação: ')
            try:
                valor=float(valor)
            except:
                while True:
                    try:
                        valor=float(valor)
                        break
                    except:
                        print('erro')
                        valor=input(f"{nome} informe o valor do saque")
            if valor <= saldo:
                print(f'saldo atual {saldo-valor}')
                save=open(f'{nome}.txt',"w")
                saldo=saldo-valor
                save.write((f'{agencia}\n{conta}\n{saldo}'))
                save.close
            else:
                print('erro')
        elif menu=="2":
            valor=input(f'{nome} seu saldo é igual a {saldo}\ninforme o valor da operação: ')
            try:
                valor=float(valor)
            except:
                while True:
                    try:
                        valor=float(valor)
                        break
                    except:
                        print('erro')
                        valor=input(f"{nome} informe o valor do saque")
            print(f'saldo atual {saldo + valor}')
            save=open(f'{nome}.txt',"w")
            saldo=saldo+valor
            save.write((f'{agencia}\n{conta}\n{saldo}'))
            save.close()
        elif menu=="3":
            nome2=input("informe o nome da conta que ira sofrer transferencia: ")
            agencia2=input('informe o numero de agencia: ')
            if agencia2.isdecimal:
                agencia2=int(agencia2)
            else:
                while True:
                    print("erro")
                    agencia2=input("informe o numero de agencia")
                    if agencia2.isdigit():
                        agencia2=int(agencia2)
                        break
            conta2=input('informe o numero da conta')
            if conta2.isdecimal:
                conta2=int(conta2)
            else:
                while True:
                    print("erro")
                    conta2=input("informe o numero de agencia")
                    if conta2.isdigit():
                        conta2=int(conta2)
                        break
            try:
                save2=open(f'{nome2}.txt',"r")
                if int(save2.readline())==agencia2:
                    if int(save2.readline())==conta2:
                        saldo1=float(save2.readline())
                    else:
                        raise ValueError("informação errrada")
                else:
                    raise ValueError("informação errrada")
            except:
                raise ValueError("informação errrada")
            valor=input('informe o numero: ')
            try:
                valor=int(valor)
            except:
                while True:
                    try:
                        valor=int(valor)
                    except:
                        print(erro)
                        valor=input('informe o valor da transação: ')
            if valor<=saldo:
                print(f"a conta de {nome} possui {saldo-valor}")
                print(f"a conta de {nome2} possui {saldo1+valor}")
            else:
                raise ValueError('você não possui esse saldo ')
            save=open('nome.txt',"w")
            save.write(f"{agencia}\n{conta}\n{saldo-valor}")
            save.close()
            save2=open(f"{nome2}.txt",'w')
            save2.write(f"{agencia2}\n{conta2}\n{saldo1+valor}")
            save2.close()
        elif menu=="sair":
            break
        else:
            print('erro')
