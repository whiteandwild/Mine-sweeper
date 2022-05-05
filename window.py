

from kivy.clock import Clock
from kivy.uix.button import Button
import main , math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.graphics import Rectangle, Color
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


mouse = None
diff = 0
class Board(GridLayout):
    
    def build(self):
        pass


class Menu(Screen):
    def DisableOthers(self , obj , txt):      
        for x in obj.children: 
            x.disabled = False 
            x.background_color = [1,1,1,1]
        global diff
        match txt:
            case "Łatwy":
                diff = 0
            case "Średni":
                diff = 1
            case "Trudny":
                diff = 2
            case _:
                return False
            

    

class gameWindow(Screen):
    
    def createBoard(self, size):
        
        diff_mult = 0
        size = int(size)

        match diff:

            case 0:
                diff_mult = 0.10
            case 1:
                diff_mult = 0.20
            case 2:
                diff_mult = 0.33
        
            case _:
                return

     
        bombs = math.ceil(size**2 * diff_mult)
        

        b = self.ids['board']
        self.removeFields()
       
        print(len(b.children))
        b.rows = size
        b.cols = size
        self.buttons = createFields(size)
        

        for elem in self.buttons:
        
            b.add_widget(elem)
        main.start(size,bombs,b,self)
        

    def removeFields(self ):
        try:
            b = self.buttons
        except : return
        for elem in b:
            
            self.ids['board'].remove_widget(elem)
    def show(self,cords,value):
        self.buttons[cords].disabled = True
        self.buttons[cords].background_disabled_down = ''
        self.buttons[cords].background_color = [1, 1, 1, 1] 
        self.buttons[cords].color = [0,0,0,1]
        self.buttons[cords].text = str(value) 
    def show_flag(self,cords,value):
        b = self.buttons[cords]
        
        if value == "":
        
            
            
            b.background_color = [1, 1, 1, 1]
        else:
            
            b.background_color = [255/255, 0/255, 255/255, 1]
        b.text = str(value)

    def get_val(self , cords):
        return self.buttons[cords].text 
    def show_bomb(self ,cords):

        

        self.buttons[cords].disabled = True
        self.buttons[cords].background_disabled_normal = ''
        self.buttons[cords].background_disabled_down = ''
        self.buttons[cords].background_color = [255/255, 0/255, 0/255, 1]
        self.buttons[cords].color = [0,0,0,1]
        self.buttons[cords].text = "X"
        
    def disable_all(self):
        for but in self.buttons:
            if but.disabled:
                continue
            but.disabled = True
            but.background_disabled_normal= but.background_normal

  
        
       
   
   
class WindowManager(ScreenManager):
    
    pass




class MinesweeperApp(App):
    pass
   
def mouseclick(instance ,touch):
    global mouse
  
    mouse = touch.button

def createFields(size):
    
    output = []
    id = 0
    global mouse

    for i in range(size**2):
        b = Button()
        b.cords = id
        b.background_down = ''
        
        b.background_disabled_normal = ''
        b.bind(on_touch_down = mouseclick)
        b.bind(on_press = lambda x : main.press(x.cords , mouse))
        
        id +=1
        output.append(b)
    return output

MinesweeperApp().run()
