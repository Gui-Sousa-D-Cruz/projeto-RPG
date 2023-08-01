import PySimpleGUI as sg
import random
sg.theme('Reddit')

'''
def janela_0():
    layout = [
        [sg.Push(), sg.Text('TEXTO', pad=(27.5,27.5,3.5,3.5),size=(55,0)), sg.Push()],
        [sg.Push(),sg.Text('O que deseja fazer?',pad=(0,0,2,2),size=(0,2)), sg.Push()],
        [sg.Push(), sg.Button('OPÇÃO 1',size=(15,2)), sg.Push(),sg.Button('OPÇÃO 2',size=(15,2)), sg.Push(), sg.Button('Inventário',size=(15,2)), sg.Push()]
    ]
    return sg.Window('RPG', layout=layout, finalize=True)
'''

#CLASSE
class Classe():
    def __init__(self,pow,dex,con,int,wis,cha,hp,mana):
        self.pow = pow
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.hp = hp + con 
        self.mana = mana + int
    def atributos(self):
        print(self.pow)
        print(self.dex)
        print(self.con)
        print(self.int)
        print(self.wis)
        print(self.cha)
        

#Funções

def d20(scss, atrib):
    d20.sucesso = scss
    d20.d20 = random.randint(1, 20)
    roll = d20.d20 + atrib
    # print(scss, atrib, d20.d20, roll)

    if roll <= 5:
        # print('Fracasso crítico!')
        d20.f_crit = True
        d20.fail = True
    elif roll >= 20:
        # print('Sucesso crítico!')
        d20.s_crit = True
        d20.fail = False
    elif roll >= d20.sucesso:
        # print('Sucesso')
        d20.s_crit = False
        d20.fail = False
    else:
        # print('Fracasso')
        d20.f_crit = False
        d20.fail = True
        
def d4(crit):
    d4.n = random.randint(1, 4)
    d4.n_2 = random.randint(1, 4)
    if crit == False:
        d4.d4 = d4.n
    else:
        d4.d4 = d4.n + d4.n_2
    
def hist(jal):
    hist.hist = historico.append(jal)   
    print(historico[1:])
    
#VARIAVEIS
historico = []
leng = int(len(historico))

nome = ''
clas = ''
lvl = 0

classe = Classe(0,0,0,0,0,0,1,1)
pow = classe.pow
dex = classe.dex
con = classe.con
inT = classe.int
wis = classe.wis
cha = classe.cha
hpmax= classe.hp
hp = hpmax
manamax= classe.mana
mana = manamax
lMANA= 0
dano = 0
porcHP= int((100 * hp) / hpmax)
porcMANA= int((100 * mana) / manamax)


def porcentagem(hp, hpmax, mana, manamax):
    porcentagem.hp = hp
    porcentagem.porcHP = int((100 * hp) / hpmax)
    porcentagem.porcMANA= int((100 * mana) / manamax)
    
#LAYOUT DAS JANELAS
def inventario():
    
    layout = [
        [sg.Text(f'Nome:   {nome}',size=(18,0),k='nome'),sg.T(f'Classe:    {clas}', size=(18,0),k='classe'),sg.T(f'Lvl:  {lvl}', k='lvl')],
        [sg.Push(),sg.Text('HP :',size=(4,0)),sg.ProgressBar(100, orientation='h', s=(30, 20), k='hp', ), sg.Push(), sg.Text(f'{hp}/{hpmax}',k='hpt')],
        [sg.Push(),sg.Text('MANA :'),sg.ProgressBar(100, orientation='h', s=(30, 20), k='mana'),sg.Push(), sg.Text(f'{mana}/{manamax}', k='manat')],
        [
        sg.Push(),
        sg.Listbox(['','Atributos','',f'        Força: {pow} ','',f'        Agilidade: {dex}','',f'        Constituição: {con}','',f'        Inteligência: {inT}','',f'        Sabedoria: {wis}','',f'        Carisma: {cha}',''], no_scrollbar=True, s=(20, 15),k='atri'),
        sg.Push(),
         sg.Listbox([''], no_scrollbar=True, s=(20, 15)),
         sg.Push(),
         sg.Listbox([''], no_scrollbar=True, s=(20, 15)),
         sg.Push(),
         ],
        [sg.Push(), sg.Button('Voltar',size=(15,2)), sg.Push()]
    ]   
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_1():
    layout=[
        [],
        [sg.Push(), sg.Text('Preparado para sua aventura?'),sg.Push()],
        [],
        [sg.Push(), sg.Button('Sim',size=(15,2)),sg.Push(), sg.Button('Não',size=(15,2)), sg.Push()],
        [],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_2():
    layout=[
        [],
        [sg.Push(), sg.Text('Qual seu nome?'), sg.Push()],
        [sg.Input('',size=(50,7), key='nome')],
        [],
        [sg.Push(), sg.Button('Continuar',size=(15,2)), sg.Push()],
        [],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_3():
    layout = [
        [],
        [sg.Push(), sg.Text('Escolha uma classe:'), sg.Push()],
        [],
        [sg.Button('Guerreiro',size=(20,2)),sg.Button('Mago',size=(20,2))],
        [sg.Button('Ladino',size=(20,2)),sg.Button('Clérigo',size=(20,2))],
        [],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)


def janela_4():
    layout=[

        [sg.Text(f'A guerra entre os viashinos e os homens durava décadas, o rei Lorestes prometeu rios de ouro pra quem trouxesse a cabeça do rei viashiano, inúmeros mercenários tentaram se aproximar da pirâmide, porém todos falharam. Você e seu grupo de aventureiros planejava uma invasão à pirâmide mas foram emboscados, e agora só você {nome} o grande {clas}, pode salvá-los de um destino miserável.',size=(55,7))],
        [],
        [sg.Push(), sg.Button('Continuar',size=(15,2)), sg.Push()],
        [],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_5():
    layout=[
        
        [sg.Push(), sg.Text('Após a emboscada, você e seu grupo foram separados, você acorda numa pequena câmara dentro da pirâmide, há um alçapão no teto e apenas uma saída que da para um corredor, você nota na parade diversos hierógrifos.', pad=(27.5,27.5,3.5,3.5),size=(55,0)), sg.Push()],
        [sg.Push(),sg.Text('O que deseja fazer?',pad=(0,0,2,2),size=(0,2)), sg.Push()],
        [sg.Push(), sg.Button('Investigar a parede',size=(20,2)), sg.Push(),sg.Button('Ir pro corredor',size=(20,2)), sg.Push()],
        [],
        [sg.Push(), sg.Button('Habilidades',size=(20,2)),sg.Push(),sg.Button('Inventário',size=(20,2)),sg.Push()],
        [],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_6():
    layout = [
        [sg.Push(), sg.Text('Você anda até a saída e observa que além de ser um corredor extenso está cheio de ossos humanos, porém há uma pilha que se destaca.', pad=(27.5,27.5,3.5,3.5),size=(55,0)), sg.Push()],
        [sg.Push(),sg.Text('O que deseja fazer?',pad=(0,0,2,2),size=(0,2)), sg.Push()],
        [sg.Push(), sg.Button('Olhar a pilha',size=(15,2)), sg.Push(),sg.Button('Continuar andando',size=(15,2)), sg.Push(), sg.Button('Inventário',size=(15,2)), sg.Push()],
        [],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_7_1():
    layout = [
        [sg.Push(), sg.Text('Você anda pelo corredor, esbarrando em todas as plihas de ossos, até que ouve um barulho de engrenagem, porém a armadilha trava e não ativa!', pad=(27.5,27.5,3.5,3.5),size=(55,0)), sg.Push()],
        [sg.Push(),sg.Text('O que deseja fazer?',pad=(0,0,2,2),size=(0,2)), sg.Push()],
        [sg.Push(), sg.Button('OPÇÃO 1',size=(15,2)), sg.Push(),sg.Button('OPÇÃO 2',size=(15,2)), sg.Push(), sg.Button('Inventário',size=(15,2)), sg.Push()],
        [],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_7_2():
    layout = [
        [sg.Push(), sg.Text('Você anda pelo corredor, esbarrando em todas as plihas de ossos, até que você ouve um barulho de engrenagem, então são disparados diversos dardos ao longo do corredor!', pad=(27.5,27.5,3.5,3.5),size=(55,0)), sg.Push()],
        [sg.Push(),sg.Text(f'Você recebeu {dano} de dano',pad=(0,0,2,2),size=(0,2)), sg.Push()],
        [sg.Push(),sg.Text('O que deseja fazer?',pad=(0,0,2,2),size=(0,2)), sg.Push()],
        [sg.Push(), sg.Button('OPÇÃO 1',size=(15,2)), sg.Push(),sg.Button('OPÇÃO 2',size=(15,2)), sg.Push(), sg.Button('Inventário',size=(15,2)), sg.Push()],
        [],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)


#CRIAÇÃO DE JANELAS
invent = inventario()
janela1 = janela_1()
janela2 = None
janela3 = None
janela4 = None
janela5 = None
janela6 = None
janela7 = None

invent.hide()


#LOOP DE LEITURA DOS EVENTOS
historico.append(janela1)
while True:
    
    janela,evento,valor = sg.read_all_windows()
    
    # FECHAR O JOGO
    
    if evento == sg.WIN_CLOSED:
        janela.close()
        break
    
    #INVENTARIO
    
    if evento == 'Inventário':
        invent['hp'].update(porcHP)
        invent['mana'].update(porcMANA)
        invent['hpt'].update(f'{hp}/{hpmax}')
        invent['manat'].update(f'{mana}/{manamax}')
        invent['nome'].update(f'Nome:   {nome.capitalize()}')
        invent['classe'].update(f'Classe:    {clas.capitalize()}')
        invent['lvl'].update(f'Lvl:  {lvl}')
        invent['atri'].update(['','        ATRIBUTOS:','',f'        Força: {pow} ','',f'        Agilidade: {dex}','',f'        Constituição: {con}','',f'        Inteligência: {inT}','',f'        Sabedoria: {wis}','',f'        Carisma: {cha}',''])
        
        invent.un_hide()
        
        if historico[leng-1] == 'janela5':
            janela5.hide()
        if historico[leng-1] == 'janela6':
            janela6.hide()
        if historico[leng-1] == 'janela7':
            janela7.hide()

        
    if janela == invent:
        if evento == 'Voltar':
            if historico[leng-1] == 'janela5':
               invent.hide()
               janela5.un_hide()
            if historico[leng-1] == 'janela6':
                invent.hide()
                janela6.un_hide()
            if historico[leng-1] == 'janela7':
                invent.hide()
                janela7.un_hide()
    
    #PRÉ MENU
    
    if janela == janela1 and evento == 'Sim':
        janela2 = janela_2()
        janela2.un_hide()
        janela1.hide()
        hist('janela2')
    elif janela == janela1 and evento == 'Não':
        sg.popup('Volte quando estiver pronto')
        janela.close()
        break
    
    #TELA DE REGISTRO DE NOME
    
    if janela == janela2 and evento == 'Continuar':
        nome = janela2['nome'].get()
        if nome == '':
            popup = sg.Window('RPG', [[sg.T('Escolha um nome válido!')], [sg.Push(),sg.Yes(s=10, button_text='OK' ),sg.Push()]], disable_close=True).read(close=True)
        else:
            janela3 =janela_3()
            janela2.hide()
            hist('janela3')
        
    #TELA DE REGISTRO DE CLASSE
    
    if janela == janela3 and evento == 'Guerreiro':
        classe = Classe(0,0,0,0,0,0,1,1)
        pow = classe.pow
        dex = classe.dex
        con = classe.con
        inT = classe.int
        wis = classe.wis
        cha = classe.cha
        hpmax= classe.hp
        hp = hpmax
        manamax= classe.mana
        mana = manamax
        clas = 'guerreiro'
        janela4 = janela_4()
        janela3.hide()
        historico.append('janela4')
        
    if janela == janela3 and evento == 'Mago':
        classe = Classe(0,0,0,0,0,0,1,1)
        pow = classe.pow
        dex = classe.dex
        con = classe.con
        inT = classe.int
        wis = classe.wis
        cha = classe.cha
        hpmax= classe.hp
        hp = hpmax
        manamax= classe.mana
        mana = manamax
        clas = 'mago'
        janela4 = janela_4()
        janela3.hide()
        historico.append('janela4')
        
    if janela == janela3 and evento == 'Ladino':
        classe = Classe(0,0,0,0,0,0,1,1)
        pow = classe.pow
        dex = classe.dex
        con = classe.con
        inT = classe.int
        wis = classe.wis
        cha = classe.cha
        hpmax= classe.hp
        hp = hpmax
        manamax= classe.mana
        mana = manamax
        clas = 'ladino'
        janela4 = janela_4()
        janela3.hide()
        hist('janela4')
        
    if janela == janela3 and evento == 'Clérigo':
        classe = Classe(0,0,0,0,0,0,1,1)
        pow = classe.pow
        dex = classe.dex
        con = classe.con
        inT = classe.int
        wis = classe.wis
        cha = classe.cha
        hpmax= classe.hp
        hp = hpmax
        manamax= classe.mana
        mana = manamax
        clas = 'clérigo'
        janela4 = janela_4()
        janela3.hide()
        hist('janela4')
        
    #INTRODUÇÃO 

    if janela == janela4 and evento == 'Continuar':
        janela5 = janela_5()
        janela4.hide()
        hist('janela5')
    
    #
    
    if janela == janela5:
        
        if evento == 'Investigar a parede':
            popup = sg.Window('RPG', [[sg.T('Os hierógrifos te mostram: Viashinos devorando humanos ainda vivos!')], [sg.Push(),sg.Yes(s=10, button_text='OK' ),sg.Push()]], disable_close=True).read(close=True)
        
        if evento == 'Ir pro corredor':
            janela6 = janela_6()
            janela5.hide()
            hist('janela6')

            
    #
    
    if janela == janela6:
        
        if evento == 'Olhar a pilha':
            d20(20, wis)
            if d20.fail == False:
                pista = True
                popup = sg.Window('RPG', [[sg.T('Você analisa a pilha de ossos e descobre uma armadilha logo à frente!')], [sg.Push(),sg.Yes(s=10, button_text='OK' ),sg.Push()]], disable_close=True).read(close=True)
                janela7 = janela_7_1()
                janela6.hide()
                hist('janela7')
    
            else:
                pista = False
                popup = sg.Window('RPG', [[sg.T('A pilha de ossos não diz nada a você.')], [sg.Push(),sg.Yes(s=10, button_text='OK' ),sg.Push()]], disable_close=True).read(close=True)
                fcrit = d20.f_crit
                d4(fcrit)
                dano = d4.d4
                hp -= dano
                porcentagem(hp,hpmax,mana,manamax)
                hp = porcentagem.hp
                porcHP = porcentagem.porcHP
                porcMANA = porcentagem.porcMANA
                janela7 = janela_7_2()
                janela6.hide()
                hist('janela7')
    

                                  
        if evento == 'Continuar andando':
            d4(True)
            dano = d4.d4
            hp -= dano
            if dano > hp:
                sg.popup(f'''Você anda pelo corredor, esbarrando em todas as plihas de ossos, até que você ouve um barulho de engrenagem, então são disparados diversos dardos ao longo do corredor! 
                         Recebeu {dano} de dano
                         Você Morreu!''')
                janela.close()
            else:
                porcentagem(hp,hpmax,mana,manamax)
                hp = porcentagem.hp
                porcHP = porcentagem.porcHP
                porcMANA = porcentagem.porcMANA
                janela7 = janela_7_2()
                janela6.hide()
                hist('janela7')
                print(hp)


    #
    
    if janela == janela7:
        
        pass
    
    
            
               
           