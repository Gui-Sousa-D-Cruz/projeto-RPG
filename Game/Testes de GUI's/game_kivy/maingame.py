
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class Gerenciador(ScreenManager):
    pass

class Tela1(Screen):
    pass

class Tela2_1(Screen):
    pass
    
class Tela2_2(Screen):
    pass

class Inventario(Screen):
    pass

class Status(Screen):
    pass




class Game(App):
    def build(self):
        return Gerenciador()
        
   

Game().run()


