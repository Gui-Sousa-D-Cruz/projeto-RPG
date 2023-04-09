import random
from time import sleep
import keyboard 


pow = 0
dex = 0
con = 0
int = 0
sab = 0
car = 0
lbase = 10
hp = lbase + con


lista = [pow, dex, con , int, sab, car, lbase, hp]

class Item:
    def __init__(self,nome, pow, dex, con, int, sab, car, life):
        self.nome = nome
        self.pow = pow
        self.dex = dex
        self.con = con
        self.int = int
        self.sab = sab
        self.car = car
        self.life = life

item1 = Item('Poção de cura',0,0,0,0,0,
0,1)
item2 = Item('Escudo',5,5,5,5,5,5,5)
item3 = Item('nome3',0,0,0,0,0,0,0)
item4 = Item('nome4',0,0,0,0,0,0,0)
item5 = Item('nome5',0,0,0,0,0,0,0)
item6 = Item('nome6',0,0,0,0,0,0,0)

bau1 = [item1, item2]

ItemBau1 = random.choice(bau1)



def linha():
    print('-='*50)


def classes():
    
    while True:
        if keyboard.is_pressed('1'):
            classes.classe = 'guerreiro'
            break
        elif keyboard.is_pressed('2'):
            classes.classe = 'mago'
            break
        elif keyboard.is_pressed('3'):
            classes .classe = 'ladino'
            break       
        elif keyboard.is_pressed('4'):
            classes.classe = 'clérigo'
            break


def escolha(): #escolha de ação
    escolha.act = 0

    while True:
        if keyboard.is_pressed('1'):
            escolha.act = 1
            break
        elif keyboard.is_pressed('2'):
            escolha.act = 2
            break
        
           
                
                
      
def d20(scss, atrib):
    d20.sucesso = scss
    d20.d20 = random.randint(1, 20)
    roll = d20.d20 + atrib
    #print(scss, atrib, d20.d20, roll)
      

    if roll <= 5:
        #print('Fracasso crítico!')
        d20.f_crit = True
        d20.fail = True
    elif roll >= 20:
        #print('Sucesso crítico!')
        d20.s_crit = True
        d20.fail = False
    elif roll >= d20.sucesso:
        #print('Sucesso')
        d20.s_crit = False
        d20.fail = False
    else:
        #print('Fracasso')
        d20.f_crit = False
        d20.fail = True


      
def d4(crit):
    d4.d4 = random.randint(1, 4)
    d4.d4_2 = random.randint(1, 4)
    d4.life = hp
    if crit == False:
        d4.life -= d4.d4
        d4.dano = d4.d4 + d4.d4_2
    else:
        d4.life -= d4.d4 + d4.d4_2
        d4.dano = d4.d4 + d4.d4_2


def op(t1, t2):
   op.dec = '| 1-'+ t1 + ' | 2-'+ t2 +' |'
   print(op.dec)

linha()
nome = input('Qual é seu nome, viajante? ').strip()
linha()

print(f'Escolha uma classe: | 1-Guerreiro | 2-Mago | 3-Ladino | 4-Clérigo | ')
linha()

classes()
                
print(f'É um prazer te conhecer {nome}!')
linha()

sleep(1)

if classes.classe.upper() == 'MAGO':
    print('Você escolheu a classe: Mago!')
    pow = 0
    dex = 3
    con = 2
    int = 4
    sab = 4
    car = 1
    hp = lbase + con
if classes.classe.upper() == 'GUERREIRO':
    print('Você escolheu a classe: Guerreiro!')
    pow = 4
    dex = 0
    con = 4
    int = 3
    sab = 1
    car = 2
    hp = lbase + con
if classes.classe.upper() == 'LADINO':
    print('Você escolheu a classe: Ladino!')
    pow = 1
    dex = 4
    con = 0
    int = 3
    sab = 2
    car = 4
    hp = lbase + con
if classes.classe.upper() == 'CLERIGO' or classes.classe.upper() == 'CLÉRIGO':
    print('Você escolheu a classe: Clérigo')
    pow = 0
    dex = 1
    con = 2
    int = 3
    sab = 4
    car = 4
    hp = lbase + con
linha()

sleep(1)

print('Ao adentrar a pirâmide, você nota diversos hierógrifos na parede, o que deseja fazer?')
op('Investigar.', 'Passar direto.')
linha()

escolha()

sleep(1)

if escolha.act == 1:
    print('Os hierógrifos te mostram: Viashinos devorando humanos ainda vivos!')
else:
    print('Você anda até a entrada do corredor.')

linha()

sleep(1)

print('Você vê um longo corredor na sua frente, o que deseja fazer?')
op('Continuar seguindo.', 'Voltar.')
linha()

escolha()

sleep(1)

if escolha.act == 1:
    print('Você segue, vendo ossos humanos espalhados por todo o corredor.')
else:
    print('Game Over!')
linha()

sleep(1)

print('No meio corredor, você avista uma pilha de ossos! o que deseja fazer?')
op('Investigar.', 'Passar direto.')
linha()

escolha()

sleep(1)

if escolha.act == 1:
    d20(10, sab)
    if d20.fail == False:
        investigar_ossos = True
        print('Você analisa a pilha de ossos e descobre uma armadilha logo à frente!')
    else:
        investigar_ossos = False
        print('A pilha de ossos não diz nada a você.')
else:
    print('Você passa direto pela pilha de ossos!')
    investigar_ossos = False
linha() 

sleep(1)
    
print('O que deseja fazer?')
op('Continuar pelo corredor.','Voltar.')     
linha() 

escolha()

if escolha.act == 1:
    if investigar_ossos == True:
        print('Você segue o corredor e não ativa a armadilha!')
    else:
        print('Ao seguir o corredor, você ouve um barulho de pedra se movendo e repentinamente são dispardos dardos das paredes!')
        d20(12, dex)
        if d20.fail == False:
            print('Você consegue desviar de todos os dardos e não sofre nenhum dano!')
        elif d20.f_crit == True:
            d4(d20.f_crit)
            print(f'Você tomou {(d4.d4 + d4.d4_2)} de dano e está agora com {d4.life} de vida')
            hp -= d4.dano
        else:
            d4(d20.f_crit)
            print(f'Você tomou {d4.d4} de dano e está agora com {d4.life} de vida')
            hp -= d4.dano                                               
else:
    print('Game Over!')            
linha()

sleep(1)

print('Você entra em uma nova câmara da pirâmide, à frente está um corredor e à esquerda tem uma porta. O que deseja fazer?')

op('Seguir em frente.', 'Verificar a porta.')

linha()

escolha()

sleep(1)


if escolha.act == 1:
    pass
else:
    print('Você verificou a porta e descobre uma pequena câmara. O que deseja fazer?')
    op('Seguir em frente.','Entrar na pequena câmara.')
    linha()
    escolha()
    sleep(1)
    if escolha.act == 1:
        pass
    else:
        print('Ao entrar, você se depara com um báu. O que deseja fazer?')
        op('Sair.', 'Abrir o báu.')
        linha()
        escolha()
        sleep(1)
        if escolha.act == 1:
            print('Você retornou à câmara principal, mas ao sair a pequena câmara desmorona. O que deseja fazer?')
            op('Seguir em frente', 'Voltar')
            linha()
            escolha()
            sleep(1)
            if escolha.act == 1:
                pass
            else:
                print(f'Game Over!')
                linha()
                exit()
        else:
            print(f'Você abriu o báu e achou: {ItemBau1.nome}!')
            linha()
            sleep(1)
            if ItemBau1.nome == bau1[0].nome: 
                print(f'Você guardou: {ItemBau1.nome}')
                linha()
                print('O que deseja fazer?')
                op('Sair da pequena câmara', 'Ficar na pequena câmara')
                linha()
                escolha()
                sleep(1)
                if escolha.act == 1:
                    print('Você retornou à câmara principal, mas ao sair a pequena câmara desmorona. O que deseja fazer?')
                    op('Seguir em frente', 'Voltar')
                    linha()
                    escolha()
                    sleep(1)
                    if escolha.act == 1:
                        pass
                    else:
                        print(f'Game Over!')
                        linha()
                        exit()

                else:
                    print('A pequena câmara desmorona em cima de você!')
                    linha()
                    print(f'Game over!')
                    linha()
                    exit()
            
            else:
                print('Deseja equipar agora?')
                op('Sim','Não')  
                linha()
                escolha()
                sleep(1)
                if escolha.act == 1:
                    print(f'Você equipou: {ItemBau1.nome}!')
                    print(lista)
                    pow += ItemBau1.pow
                    dex += ItemBau1.dex
                    con += ItemBau1.con
                    int += ItemBau1.int
                    sab += ItemBau1.sab
                    car += ItemBau1.car
                    hp += ItemBau1.life
                    print(lista)
                    
                    linha()
                    print('O que deseja fazer?')
                    op('Sair da pequena câmara', 'Ficar na pequena câmara')
                    linha()
                    escolha()
                    sleep(1)
                    if escolha.act == 1:
                        print('Você retornou à câmara principal, mas ao sair a pequena câmara desmorona. O que deseja fazer?')
                        op('Seguir em frente', 'Voltar')
                        linha()
                        escolha()
                        sleep(1)
                        if escolha.act == 1:
                            pass
                        else:
                            print(f'Game Over!')
                            linha()
                            exit()
                    else:
                        print('A pequena câmara desmorona em cima de você!')
                        linha()
                        print(f'Game Over!')
                        linha()
                        exit()
                else:
                    print('O que deseja fazer?')
                    op('Sair da pequena câmara', 'Ficar na pequena câmara')
                    linha()
                    escolha()
                    sleep(1)
                    if escolha.act == 1:
                        print('Você retornou à câmara principal, mas ao sair a pequena câmara desmorona. O que deseja fazer?')
                        op('Seguir em frente', 'Voltar')
                        linha()
                        escolha()
                        sleep(1)
                        if escolha.act == 1:
                            pass
                        else:
                            print(f'Game Over!')
                            linha()
                            exit()
                    else:
                        print('A pequena câmara desmorona em cima de você!')
                        linha()
                        print(f'Game Over!')
                        linha()
                        exit()
                    
            


print('Você chegou à mais uma câmara!')
linha()













input('Gostou do game? ')

