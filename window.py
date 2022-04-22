
from kivy.clock import Clock
from kivy.uix.button import Button
import main
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.graphics import Rectangle, Color
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class Board(GridLayout):
    
    def build(self):
        pass
class TouchInput(Widget):

  def on_touch_down(self, touch):
    global mouse
    mouse = touch.button
    print(mouse)
    
      
class Menu(Screen):
    pass
      
class gameWindow(Screen):
    
    def createBoard(self, size , bombs):
        
        print(f"Creating board of size {size} with {bombs} bombs")
        
        size , bombs = int(size) , int(bombs)

        b = self.ids['board']
        self.removeFields()
        #Clock.schedule_once(self.removeFields) 
        print(len(b.children))
        b.rows = size
        b.cols = size
        self.buttons = createFields(size)
        

        for elem in self.buttons:
        
            b.add_widget(elem)
        main.start(size,bombs,b,self)
        print(main.board)

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
    def show_bomb(self ,cords):

        

        self.buttons[cords].disabled = True
        self.buttons[cords].background_disabled_normal = ''
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


#class Option(GridLayout):
#   pass


class MinesweeperApp(App):
    pass
   


def createFields(size):
    print(size)
    output = []
    id = 0

    for i in range(size**2):
        b = Button()
        b.cords = id
        b.background_down = ''
        
        b.background_disabled_normal = ''
        b.bind(on_press = lambda x : main.press(x.cords , "L"))
        id +=1
        output.append(b)
    return output

MinesweeperApp().run()
