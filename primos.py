#esse script é pra verificar se um numero é primo
numero=int(input("informe o numero que deseja verificar: "))
primo=False
for verifica in range(2,int((numero//2))+1):
    print(verifica)
    print(numero%verifica)
    if numero%verifica==0:
        primo=True
        break
if not primo:
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")