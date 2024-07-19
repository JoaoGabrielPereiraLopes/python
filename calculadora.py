numero=float(input('Me respoda um numero: '))
numero2=float(input("me responda outro numero: "))
operacao=input("me diga qual operacao quer fazer: ")

if operacao=='*':
    print(f'o resiultado e {numero*numero2}')
elif operacao=='+':
    print(f'o resiultado e {numero+numero2}')
elif operacao=='-':
    print(f'o resiultado e {numero-numero2}')
elif operacao=='/':
    print(f'o resiultado e {numero/numero2}')
elif operacao=='**':
    print(f'o resiultado e {numero**numero2}')
elif operacao=='//':
    print(f'o resiultado e {numero//numero2}')
elif operacao=='%':
    print(f'o resiultado e {numero%numero2}')
elif operacao=='///':
    print(f'o resiultado e {numero**(1/numero2)}')