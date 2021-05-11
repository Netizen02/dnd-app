import kivy

# importing App class:

from kivy.app import App

# importing Layouts:
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

# importing Window:
from kivy.core.window import Window

# importing Screen Manager and Screen
from kivy.uix.screenmanager import ScreenManager, Screen

# importing widgets:
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown

Window.clearcolor = (1, 1, 1, 1)
Window.size = (360, 600)

class character:
    def __init__(self,race,hp,stealth,strength,charisma,home):
        self.race = race
        self.hp = hp
        self.stealth = stealth
        self.str = strength
        self.charisma = charisma
        self.home = home


h = character('fsf',23,2324,545,True,'sg')

class Level_1_intro_page(character,BoxLayout):
    _disabled_count = 0

    def __init__(self, race,hp,stealth,strength,charisma,home,**kwargs):

        character.__init__(self,race,hp,stealth,strength,charisma,home)
        BoxLayout.__init__(self, **kwargs)

        print(h.home,h.str,h.race,h.stealth,h.charisma,h.hp)

        self.orientation = "vertical"

        self.lvl1_1_intro()

    def lvl1_1_intro(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""After returning from {h.home} you thought the worst
was behind you. The war was over,
and here you were, sitting in an 
inn enjoying a pretty good ale. 
The horrors of the battlefield 
were behind you, or so you thought.
The hour is late, and you’re weary 
from your travels. All you want
is the warm embrace of a soft feather
bed and the sweet scent of lilacs 
from the grove nearby. You excuse 
yourself, but your drinking buddies
hardly seem to notice, but you can’t
blame them, it’s been a while since 
either of you have felt this free. 
You head back to your room on the 
3rd floor and call it a day…
You wake up to the sound of a loud
crash.Coughing and disoriented, you
realize the inn is on fire. No this
is no dream, you're not back in 
{h.home}. This is here, this is now 
and time is running out. The door 
flings open as a man clad in armor 
leaps at you. You doge his attack at
the last minute, quickly knocking him
out with your bedside oil lamp. 
You need to get out of here!\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Do you jump out of the window? 
Or would you rather try and 
fight your way out of this nightmare?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        jumpbutton = Button(text="JUMP")
        fightbutton = Button(text="FIGHT")
        jumpbutton.bind(on_press=self.JUMP)
        choice.add_widget(jumpbutton)
        choice.add_widget(fightbutton)
        self.add_widget(choice)

    def JUMP(self, instance):
        # game.screenmanager.current = "Level 1 JUMP"
        pass

    def FIGHT(self, instance):
        # game.screenmanager.current = "Level 1 FIGHT"
        pass


class User_input_page(character,BoxLayout):
    _disabled_count = 0
    global h
    #h = character('Human', 500, 550, 500, True, 'home')
    x1 = 0

    def __init__(self, race,hp,stealth,strength,charisma,home,**kwargs):

        character.__init__(self,race,hp,stealth,strength,charisma,home)
        BoxLayout.__init__(self, **kwargs)



        #print(x.home)

        self.orientation = "vertical"

        self.userInput()


    def userInput(self):
        self.intro()
        story_button = Button(text="Go to story")
        story_button.bind(on_press=self.story)
        self.add_widget(story_button)

    def intro(self):
        intro = GridLayout(cols=2, rows=3, padding=10)
        intro.add_widget(Label(text=f"""Welcome Player! What is your name?""", color=(0, 0, 0, 1)))
        intro.nametextinput = TextInput(multiline=False)
        intro.add_widget(intro.nametextinput)
        intro.add_widget(Label(text=f"""Alright , 
Which race do you wish to be?""", color=(0, 0, 0, 1)))
        self.Race_Input()
        #intro.add_widget(Label(text=" Enter your weapon"))
        #self.Weapon_Input()
        self.add_widget(intro)

    def Race_Input(self):
        race = GridLayout(cols=2, rows=2, padding=10, spacing=10)
        rito = Button(text="RITO")
        elf = Button(text="ELF")
        human = Button(text="HUMAN")
        dwarf = Button(text="DWARF")
        rito.bind(on_press=self.ritO)
        elf.bind(on_press=self.elF)
        human.bind(on_press=self.humaN)
        dwarf.bind(on_press=self.dwarF)
        race.add_widget(rito)
        race.add_widget(elf)
        race.add_widget(human)
        race.add_widget(dwarf)
        self.add_widget(race)

    def ritO(self, instance):
        x1 = 1


    def elF(self, instance):
        x1 =2


    def humaN(self, instance):
        x1 =3


    def dwarF(self, instance):
        x1 = 4

    h = character('Rito', 500, 550, 500, False, 'High Rock')
    if x1 == 1:
        pass
    elif x1 ==2:
        h = character('Elf', 600, 600, 450, True, 'Valenwood')
    elif x1 ==3:
        h = character('Human', 500, 500, 550, True, 'Cyrodill')
    elif x1 ==4:
        h = character("Dwarf", 600, 450, 600, False, "Moria")

    def story(self, instance):
        game.screenmanager.current = "Level 1 Intro Page"


class Home_page(BoxLayout):
    def __init__(self, **kwargs):
        super(Home_page, self).__init__(**kwargs)

        self.orientation = "vertical"

        self.homescreen()

    def homescreen(self):
        titledisplay = Label(text=f"""Choose your
own adventure""", color=(0, 0, 0, 1), font_size=32)
        self.add_widget(titledisplay)
        subtitledisplay = Label(text=f"""Press -> to start
Press Home to go to the home screen
Press Character Description to get help """, color=(0, 0, 0, 1), font_size=12)
        self.add_widget(subtitledisplay)
        self.grid()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def grid(self):
        grid = GridLayout(cols=3, rows=1, padding=10, spacing=10)
        homescreen_button = Button(text="Home")
        playGame_button = Button(text="->")
        help_button = Button(text=f"""Character 
Description""")
        grid.add_widget(help_button)
        help_button.bind(on_press=self.help_screen)
        grid.add_widget(playGame_button)
        playGame_button.bind(on_press=self.game)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        self.add_widget(grid)

    def help_screen(self, instance):
        print("Help button")

    def game(self, instance):
        game.screenmanager.current = "User Input"


class cyoaApp(App):
    def build(self):
        self.screenmanager = ScreenManager()

        self.home_page = Home_page()
        screen = Screen(name="Home")
        screen.add_widget(self.home_page)
        self.screenmanager.add_widget(screen)

        self.user_input_page = User_input_page(h.race,h.hp,h.stealth,h.str,h.charisma,h.home)
        screen = Screen(name="User Input")
        screen.add_widget(self.user_input_page)
        self.screenmanager.add_widget(screen)

        self.level_1_intro = Level_1_intro_page(h.race,h.hp,h.stealth,h.str,h.charisma,h.home)
        screen = Screen(name="Level 1 Intro Page")
        screen.add_widget(self.level_1_intro)
        self.screenmanager.add_widget(screen)
        '''
        self.level_1_1_jump = Level_1_1_jump()
        screen = Screen(name="Level 1 JUMP")
        screen.add_widget(self.level_1_1_jump)
        self.screenmanager.add_widget(screen)
        self.level_1_1_fight = Level_1_1_fight()
        screen = Screen(name="Level 1 FIGHT")
        screen.add_widget(self.level_1_1_fight)
        self.screenmanager.add_widget(screen)'''

        return self.screenmanager


if __name__ == "__main__":
    game = cyoaApp()
    game.run()