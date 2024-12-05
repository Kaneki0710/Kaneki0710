import sys
import os

def resource_path(relative_path):
    """Retorna o caminho absoluto para o recurso (útil para PyInstaller)"""
    try:
        base_path = sys._MEIPASS
        print(f"Base Path (PyInstaller): {base_path}")  # Verifique o caminho base
    except AttributeError:
        base_path = os.path.abspath(".")
        print(f"Base Path (local): {base_path}")
    return os.path.join(base_path, relative_path)

# Exemplo de como carregar o arquivo screen.kv e a imagem calcular.png
kv_file = resource_path("screen.kv")
icon_image = resource_path("icons/calcular.png")
background_image = resource_path('background/image.jpg')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock

Window.minimum_width = 400
Window.minimum_height = 600



Window.size = (400, 600)

class MyLayout(BoxLayout):
    pass

GUI = Builder.load_file(kv_file)

class PyCalculator(App):
    def build(self):
        self.result = 0
        self.background_image = background_image
        print(f"Background image path: {self.background_image}")  # Verifica o caminho gerado
        self.account = ''
        self.icon = icon_image
        return MyLayout()
    
    def on_key_pressed(self, value):
        self.account += str(value)
        show_thing = self.account.replace('*', 'X')
        show_thing = show_thing.replace('/', ':')
        self.root.ids['label_0'].text = show_thing
        
    def equals_res(self):
        try:
            if self.account:
                result = eval(self.account)
                
                if isinstance(result, int) or result.is_integer():
                    result = int(result)
                else:
                    result = float(result)
                    
                self.account = str(result)
                self.result = result
                self.root.ids['label_0'].text = self.account
            else:
                self.root.ids['label_0'].text = '0'
            
        except Exception as e:
            self.root.ids['label_0'].text = 'Error'
            self.account = ''
    
            
    def clear_acc_res(self):
        self.account = ''
        self.root.ids['label_0'].text = '0'
    
    def backspace(self):
        count = 0
        full_word = ''
        if len(self.account) <= 1:
            self.account = ''
            self.root.ids['label_0'].text = '0'
        else:
            for letter in self.account:
                if count == len(self.account)-1:
                    break
                else:
                    full_word += letter
                count += 1
            self.account = full_word
                
            self.root.ids['label_0'].text = self.account
    
    def sum_add(self):
        self.account += '+'    
        show_thing = self.account.replace('*', 'X')
        show_thing = show_thing.replace('/', ':')    
        self.root.ids['label_0'].text = show_thing

    def sum_subtract(self):
        self.account += '-'    
        show_thing = self.account.replace('*', 'X')
        show_thing = show_thing.replace('/', ':')    
        self.root.ids['label_0'].text = show_thing
    
    def sum_mult(self):
        self.account += '*'
        show_thing = self.account.replace('*', 'X')
        show_thing = show_thing.replace('/', ':')    
        self.root.ids['label_0'].text = show_thing
    
    def sum_truediv(self):
        self.account += '/'    
        show_thing = self.account.replace('*', 'X')
        show_thing = show_thing.replace('/', ':')   
        self.root.ids['label_0'].text = show_thing
        
    def switch_signal(self):
        self.equals_res()
        if self.result > 0:
            self.result = -(self.result)
        elif self.result < 0:
            self.result = -(self.result)
        elif self.result == 0:
            self.result = self.result
        self.account = str(self.result)
        self.root.ids['label_0'].text = str(self.result)
        
    def on_start(self):
        self.clear_acc_res()
    
    def kill(self):
        App.get_running_app().stop()
        Window.close()
    

PyCalculator().run()
