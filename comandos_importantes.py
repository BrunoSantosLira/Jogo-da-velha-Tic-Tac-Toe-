'''for l in range(0,3):
    if l == 0:
        for linha in range(0,3): #Repetição do número da coluna acontece aqui
            print(f'{linha:>7}',end=' ') 
    for c in range(0,3):
        print()
        print(f'{c}: {"|":>8}{"|":>8}')
        print(f'{"----------------------":>26}')
    break


#Saida  minha   
for l in range(0,3):
    if l == 0:
        for linha in range(0,3): #Repetição do número da coluna acontece aqui
            print(f'{linha:>7}',end=' ') 
    for c in range(0,3):
        print()
        print(f'{c}: {matriz[0][c]:>4} {"|":>6}{matriz[1][c]:>4}{"|":>6}{matriz[2][c]:>4}')
        print(f'{"-------------------------------":>25}')
    break

for c in range(0,3):
        for i in matriz[c][2]:
            if i == 'X':
                print(f'Tem x')
                totalx +=1
                

 
    for c in range(0,3):
        x=0
        if matriz[2][c] == "X":
            x+=1
            totalx+=x'''


'''def leiastr():
    try:
        while True
            a= str(input('Quer jogar outra vez? [S/N]')).upper().strip()[0]
            if 'SN' not in a:
                continue
            else:
                break
    except:
        print('Digite apenas S ou N')'''
        
from ast import Num

def leiaint(msg):
    while True:
        try:
            while True:
                num= int(input(msg))
                if num in (0,1,2):
                    print('é igual')
                    return num
                else:
                    print('é diferente')
        except:
            continue
        

salve= leiaint('Digite um valor')
print(salve)

        