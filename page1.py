import kivy

#importing App class:

from kivy.app import App

#importing Layouts:
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

#importing Window:
from kivy.core.window import Window

#importing widgets:
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown

Window.clearcolor = (1,1,1,1)


class cyoaGame(BoxLayout):
    def __init__(self, **kwargs):
        super(cyoaGame, self).__init__(**kwargs)

        self.orientation = "vertical"

        self.homescreen()

    def homescreen(self):
        titledisplay = Label(text= "Choose your own adventure", color = (0, 0, 0, 1), font_size = 32)
        self.add_widget(titledisplay)
        subtitledisplay = Label(text = f"""Press -> to start
Press Home to go to the home screen
Press Character Description to get help """, color = (0,0,0, 1), font_size = 12)
        self.add_widget(subtitledisplay)
        textdisplay = Label(text = "Nirav",color = (0,0,0,1))
        self.add_widget(textdisplay)
        self.grid()

    def grid(self):
        grid = GridLayout(cols = 3, rows = 1)

        grid.add_widget(Button(text = "Character Description"))
        grid.add_widget(Button(text = "->"))
        grid.add_widget(Button(text = "|^|"))
        self.add_widget(grid)


class cyoaApp(App):
    def build(self):
        return cyoaGame()

if __name__ == "__main__":
    cyoaApp().run()