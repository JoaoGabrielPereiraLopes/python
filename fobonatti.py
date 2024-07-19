def fibonatti(acess):
    conjunct=[1,1]
    executions=2
    while executions<=acess:
        fibonacci=conjunct[0]+conjunct[1]
        conjunct[0]=conjunct[1]
        conjunct[1]=fibonacci
        executions+=1
        if executions%(acess//100)==0:
            print(f"{executions/(acess//100)}%")
    return conjunct[1]
print(fibonatti(10000000))