import os
from random import randint
from time import sleep
from colorama import Fore, Style, init
init(convert=True)


#Variáveis
matriz= [['','',''],['','',''],['','','']]
turnos=0
jogadas=[]
totjogador=[]
Pontos_maquina=0
Pontos_jogador=0


#Funções
def leiastr():
    
    while True:
        a= str(input('Quer jogar outra vez? [S/N]')).upper().strip()[0]
        if 'S' in a or 'N' in a:
            return a   
        else:
            print('Digite S ou N')     
            
def leiaint(msg):
    while True:
        try:
            while True:
                num= int(input(msg))
                if num in (0,1,2):
                    return num
                else:
                    print('-'*20)
                    print('Por favor, coloque apenas números de 0 a 2')
                    print('-'*20)
        except:
            print('-'*20)
            print('Por favor, coloque apenas números de 0 a 2')
            print('-'*20)
            continue
            

def verificar():
    if listamaq in jogadas:
        return True
    else:
        matriz[colunamaq][linhamaq] = str ("O")
        jogadas.append(listamaq)
        return False
    
def verificarjogador():
    if listajog in jogadas:
        return True
    else:
        matriz[colunajog][linhajog] = str ("X")
        jogadas.append(listajog)
        totjogador.append(listajog)

def marcação():  
    for l in range(0,3):
        if l == 0:
            for linha in range(0,3): #Repetição do número da coluna acontece aqui
                print(f'{linha:>4}',end=' ') 
            print()
        for c in range(0,3):
            print(f'{c}: {matriz[0][c]:>3} {"|":>1}{matriz[1][c]:>3}{"|":>1}{matriz[2][c]:>3}')
            print(f'{"----------------":>18}')
        break
    
def condiçãovitória():
    #colunas_Jogador
    for c in range(0,3):
        if matriz[c][0] == 'X' and  matriz[c][1] == 'X' and matriz[c][2] == 'X':
            return True
     
    #colunas_Maquina
    for c in range(0,3):
        if matriz[c][0] == 'O' and  matriz[c][1] == 'O' and matriz[c][2] == 'O':
            return True       
            
    #linhas_jogador
    for l in range(0,3):
        if matriz[0][l] == 'X' and  matriz[1][l] == 'X' and matriz[2][l] == 'X':
            return True
        
           
    #linhasMaquina
    for l in range(0,3):
        if matriz[0][l] == 'O' and  matriz[1][l] == 'O' and matriz[2][l] == 'O':
            return True
    
    #Diagonal
    if matriz[0][0] == 'X' and  matriz[1][1] == 'X' and matriz[2][2] == 'X':
        return True
    
    #Diagonal_Maquina
    if matriz[0][0] == 'O' and  matriz[1][1] == 'O' and matriz[2][2] == 'O':
        return True
        
    #Outra Diagonal
    if matriz[0][2] == 'X' and  matriz[1][1] == 'X' and matriz[2][0] == 'X':
        return True
    
    #Outra Diagonal_Maquina
    if matriz[0][2] == 'O' and  matriz[1][1] == 'O' and matriz[2][0] == 'O':
        return True
    
    
    
#classes
class JogoMaquina:
    def __init__(self,linha=0,coluna=0):
        self.linha= linha
        self.coluna= coluna
        
    def JogarLinha(self):
        self.linha= randint(0,2)
        return self.linha
    
    def JogarColuna(self):
        self.coluna= randint(0,2)
        return self.coluna
    
class Jogador:
    def __init__(self,linha=0,coluna=0):
        self.linha= linha
        self.coluna= coluna
        
    def JogarLinha(self):
        self.linha= leiaint('Linha:')
        return self.linha
    
    def JogarColuna(self):
        self.coluna= leiaint('Coluna:')
        return self.coluna


#********INÍCIO***************
while True:
    while True:
        os.system('cls')
        marcação()
        print(Fore.CYAN)
        print(f'Turnos:{turnos}')
        print(Style.RESET_ALL)
                
        #Entrada Do Jogador
        while True:
            jogador= Jogador()
            linhajog= jogador.JogarLinha()
            colunajog= jogador.JogarColuna()
            print(Fore.YELLOW)
            print('-=-'*10)
            print(Style.RESET_ALL)
            listajog=[linhajog,colunajog]
            verificação= verificarjogador()
            if verificação == True:
                print('-'*20)
                print('A jogada já foi feita \nTente Novamente:')
                print('-'*20)
                continue
            else:
                turnos+=1
                break
        

        if condiçãovitória():
            print(Fore.BLUE)
            print('JOGO FINALIZADO!')
            print('VITÓRIA DO JOGADOR!')
            Pontos_jogador+=1
            print(Style.RESET_ALL)
            marcação()
            break
    
        
        if turnos == 9:
            print(f'Turno: {turnos}')
            print('Jogo Finalizado!!!')
            print('Resultado: EMPATE')
            marcação()
            break

        #Entrada Da Maquina
        maquina= JogoMaquina()
        while True:
            linhamaq= maquina.JogarLinha()
            colunamaq=maquina.JogarColuna()
            listamaq= [linhamaq,colunamaq]
            a = verificar()
            if a == False:
                break
        turnos+=1
        
        if condiçãovitória():
            print(Fore.RED)
            print('JOGO FINALIZADO')
            print('VIÓRIA DO COMPUTADOR!!!')
            Pontos_maquina+=1
            print(Style.RESET_ALL)
            marcação()
            break
        print('-=-'*20)
     
    print(f'-Pontos do jogador: {Pontos_jogador} \n-Pontos da maquina: {Pontos_maquina}')
    print('-'*20)   
    resposta= leiastr()
    if resposta == 'S':
        matriz= [['','',''],['','',''],['','','']]
        jogadas=[]
        totjogador=[]
        turnos=0
        continue
    else:
        print('|-------RESULTADO FINAL--------------|')
        print(f'|Pontos do computador: {Pontos_maquina}')
        print(f'|Pontos do jogador...: {Pontos_jogador}')
        print('|')
        print('|-------Obrigado por jogar! ;/-------|')
        break
    