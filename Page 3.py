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
# importing clock:
from kivy.clock import Clock
# importing music and audio
from kivy.core.audio import SoundLoader

Window.clearcolor = (1, 1, 1, 1)
Window.size = (360, 600)


class character:
    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense):
        self.race = race
        self.hp = hp
        self.stealth = stealth
        self.strength = strength
        self.charisma = charisma
        self.home = home
        self.name = name
        self.weapon = weapon
        self.artifact = artifact
        self.defense = defense


h = character("race", 0.00, 0.00, 0.00, True, "home", "player", "sword", False, 0)


class Level_6_intro_page(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):

        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_6_intro_page()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_6_intro_page(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""Mt.Lynaru, one of the tallest mountains in
the realm. You had never been this
close to it before. After taking a
few moments to admire the view around,
you snap out of it and remember why you
are here.It’s time to get to Revan
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=1, rows=1)
        nextbutton = Button(text="Next")
        nextbutton.bind(on_press=self.proceed_1)
        choice.add_widget(nextbutton)
        self.add_widget(choice)

    def proceed_1(self, instance):
        if h.race == 'Rito':
            game.screenmanager.current = "Level 6 Rito"
        else:
            game.screenmanager.current = "Level 6 climb"


class Level_6_Rito(character, BoxLayout):
    _disabled_count = 0


    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_6_Rito()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 6 Intro"

    def level_6_Rito(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""You immediately fly to the top of
the mountain.The feeling of wind on
your wings brings back memories of 
a time when you were safe. 
You feel better and your resolve is stronger.
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp += 150
        self.add_widget(Label(text=f"""""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=1, rows=1)
        nextbutton = Button(text="Next")
        nextbutton.bind(on_press=self.proceed_1)
        choice.add_widget(nextbutton)
        self.add_widget(choice)

    def proceed_1(self, instance):
        game.lvl7courtyard()
        game.screenmanager.current = "Level 7 courtyard"


class Level_6_climb(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_6_climb()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 6 Intro"

    def level_6_climb(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)), scroll_distance = 100)
        texta = Label(text=f""" It’s a long, hard climb.But that
will not stop you, for you are
filled with determination.
You begin your journey up the
great mountain. Good thing you
already had some mountain climbing
experience from the war, so it did
not prove too challenging.

A few hours later, while you were 
resting in a small cave, you noticed 
a rather odd shape on a cliffside near
you.You decide to investigate it.As you 
got closer you see that it is a small 
rock-cut statue with a few stone bowls 
near it.\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Do you want to make an offering?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        yesbutton = Button(text="Yes")
        nobutton = Button(text="No")
        yesbutton.bind(on_press=self.yes)
        nobutton.bind(on_press=self.no)
        choice.add_widget(yesbutton)
        choice.add_widget(nobutton)
        self.add_widget(choice)

    def yes(self, instance):
        game.lvl6offering()
        game.screenmanager.current = "Level 6 offering"

    def no(self, instance):
        game.screenmanager.current = "Level 6 no offering"


class Level_6_yes(character, BoxLayout):
    _disabled_count = 0
    h.hp += 150
    h.strength += 50

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_6_yes()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=4, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)
        
    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 6 climb"

    def level_6_yes(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""Nothing happens at first.You aren’t
surprised and begin to leave,when you
notice the shrine begins to glow.
It’s dim initially, but it’s intensity
increases.You touch the statue and find
it’s warm.You start feeling stronger and your
injuries begin healing.After a while it stops
and everything goes back to normal.

Was it a blessing?You’re not sure.All you 
know is that you feel a lot better.
With your rejuvenated confidence,you 
proceed up the mountain.
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=1, rows=1)
        nextbutton = Button(text="Next")
        nextbutton.bind(on_press=self.proceed_1)
        choice.add_widget(nextbutton)
        self.add_widget(choice)

    def proceed_1(self, instance):
        game.screenmanager.current = "Level 7 Intro"


class Level_6_no(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_6_no()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=4, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 6 climb"

    def level_6_no(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""‘But nothing more than a rock sculpture’

You turn back and rest in the cave.
After a while, you continue up the
mountain.One way or another,
you know your journey will end soon.
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=1, rows=1)
        nextbutton = Button(text="Next")
        nextbutton.bind(on_press=self.proceed_1)
        choice.add_widget(nextbutton)
        self.add_widget(choice)

    def proceed_1(self, instance):
        game.screenmanager.current = "Level 7 Intro"


class Level_7_intro_page(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_7_intro_page()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=4, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_7_intro_page(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f""" 
You arrive at Revan’s camp. It’s pretty 
impressive he was able to set it
all up in just a few days. After
scouting from a rock above the camp
you find a path that leads to Revan’s tent.
As you’re leaving you find a bottle with
something in it.
\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Do you drink it?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        yesbutton = Button(text="Yes")
        nobutton = Button(text="No")
        yesbutton.bind(on_press=self.yes)
        nobutton.bind(on_press=self.no)
        choice.add_widget(yesbutton)
        choice.add_widget(nobutton)
        self.add_widget(choice)

    def yes(self, instance):
        game.screenmanager.current = "Level 7 yes drink"

    def no(self, instance):
        game.screenmanager.current = "Level 7 no drink"


class Level_7_yes_drink(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_7_yes_drink()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 7 Intro"

    def level_7_yes_drink(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""It tastes like one of the skill
enhancement potions handed out during the war.
It’s not very effective but it still helps.
\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.stealth += 50
        print(h.stealth)
        self.add_widget(Label(text=f"""Do you want to attack the camp?Or sneak in?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        attackbutton = Button(text="Attack")
        sneakbutton = Button(text="Sneak")
        attackbutton.bind(on_press=self.attack)
        sneakbutton.bind(on_press=self.sneak)
        choice.add_widget(attackbutton)
        choice.add_widget(sneakbutton)
        self.add_widget(choice)

    def attack(self, instance):
        if h.strength >= 500:
            game. lvl7attack()
            game.screenmanager.current = "Level 7 attack"
        else:
            game.screenmanager.current = "Level 7 no attack"

    def sneak(self, instance):
        if h.stealth >= 600:
            game.screenmanager.current = "Level 7 sneak"
        else:
            game.screenmanager.current = "Level 7 no sneak"


class Level_7_no_drink(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_7_no_drink()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 7 Intro"

    def level_7_no_drink(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Do you want to attack the camp?Or sneak in?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        attackbutton = Button(text="Attack")
        sneakbutton = Button(text="Sneak")
        attackbutton.bind(on_press=self.attack)
        sneakbutton.bind(on_press=self.sneak)
        choice.add_widget(attackbutton)
        choice.add_widget(sneakbutton)
        self.add_widget(choice)

    def attack(self, instance):
        if h.strength >= 500:
            game. lvl7attack()
            game.screenmanager.current = "Level 7 attack"
        else:
            game.screenmanager.current = "Level 7 no attack"

    def sneak(self, instance):
        if h.stealth >= 600:
            game.screenmanager.current = "Level 7 sneak"
        else:
            game.screenmanager.current = "Level 7 no sneak"


class Level_7_attack(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_7_attack()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_7_attack(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""You drop down on a guard below, neutralizing him.
This attracts the attention of the entire 
camp, but you don’t care. You’re here for 
Revan, and nothing is going to stop you.

An unmatched fury takes over you as you take 
out the entire camp in combat.Seeing your rage
and strength terrorizes your enemies, moments
before they fall to your {h.weapon}. When the 
dust settles, you stand victorious on a pile
of mercenary corpses. But there’s no sign of Revan.
You head to his tent to investigate.
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        if h.strength <= 600:
            h.hp -= 200
        self.add_widget(Label(text=f"""""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=1, rows=1)
        nextbutton = Button(text="Next")
        nextbutton.bind(on_press=self.proceed_1)
        choice.add_widget(nextbutton)
        self.add_widget(choice)

    def proceed_1(self, instance):
        game.lvl7courtyard()
        game.screenmanager.current = "Level 7 courtyard"


class Level_7_attack_no(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_7_attack_no()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_7_attack_no(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""You drop down on a guard below,
neutralizing him.This attracts the attention of
the entire camp,and soon you find yourself facing
an overwhelming force. You put up a good fight but
the numbers are not in your favour, and you soon
perish


""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Game Over""", color=(0, 0, 0, 1)))


class Level_7_sneak(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_7_sneak()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_7_sneak(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""You drop down into the camp, hiding
in bushes and under carts as you 
make your way through the camp.
You take out archers in watchtowers
and guards blocking your way.Finally
you enter Revan’s tent, but find it
to be empty
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=1, rows=1)
        nextbutton = Button(text="Next")
        nextbutton.bind(on_press=self.proceed_1)
        choice.add_widget(nextbutton)
        self.add_widget(choice)

    def proceed_1(self, instance):
        game.screenmanager.current = "Level 7 Intro"


class Level_7_sneak_no(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_7_sneak_no()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_7_sneak_no(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""You drop down into the camp, hiding
in bushes and under carts as you
make your way through the camp.
An archer from a watchtower spots
you and alerts everyone, and soon
you find yourself facing an overwhelming
force. You put up a good fight but
the numbers are not in your favour,and
you soon perish

""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Game Over""", color=(0, 0, 0, 1)))


class Level_7_courtyard(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_7_courtyard()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_7_courtyard(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""You find yourself in an empty courtyard.

‘REVAN!SHOW YOURSELF’

On the hill in front of you,
a silhouette of a man appears,
before being replaced by a man
resembling a monster

‘So this is the bug that has 
been bothering me all along. I’m 
impressed you made it all the way 
here bug, but you have been a thorn 
in my side for far too long. Let’s 
get this over with, It’s almost 
lunchtime. I think I’ll have 
{h.race} today’

He jumps down and faces you in the
courtyard. Everything you have done
has led to this moment…
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Do you attack? Or Hold your ground""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        attackbutton = Button(text="Attack")
        defendbutton = Button(text="Defend")
        attackbutton.bind(on_press=self.attack)
        defendbutton.bind(on_press=self.defend)
        choice.add_widget(attackbutton)
        choice.add_widget(defendbutton)
        self.add_widget(choice)

    def attack(self, instance):
        if h.artifact == True:
            game.lvl7artifactattack()
            game.screenmanager.current = "Level 7 artifact attack"
        else:
            game.screenmanager.current = "Level 7 attack 0"

    def defend(self, instance):
        if h.defense == 0:
            game.screenmanager.current = "Level 7 defend 0"
            h.defense += 1
        elif h.defense == 1:
            game.screenmanager.current = "Level 7 defend 1"
            h.defense += 1


class Level_7_attack_0(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_7_attack_0()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_7_attack_0(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""You charge at Revan, but as soon
as you get near him,something unknown
knocks you off your feet and Revan deals
a devastating blow, hurting you.You manage
to put some distance between the two of
you and regroup.
\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Do you attack? Or Hold your ground
""", color=(0, 0, 0, 1)))
        h.hp -= 70
        choice = GridLayout(cols=2, rows=1)
        attackbutton = Button(text="Attack")
        defendbutton = Button(text="Defend")
        attackbutton.bind(on_press=self.attack)
        defendbutton.bind(on_press=self.defend)
        choice.add_widget(attackbutton)
        choice.add_widget(defendbutton)
        self.add_widget(choice)

    def attack(self, instance):
        if h.artifact == True:
            game.lvl7artifactattack()
            game.screenmanager.current = "Level 7 artifact attack"
        else:
            if h.hp > 0:
                game.screenmanager.current = "Level 7 attack 1"
            else:
                game.screenmanager.current = "Level 7 death"

    def defend(self, instance):
        if h.hp > 0:
            if h.defense == 0:
                game.screenmanager.current = "Level 7 defend 0"
                h.defense += 1
            elif h.defense == 1:
                game.screenmanager.current = "Level 7 defend 1"
                h.defense += 1
            elif h.defense == 2:
                game.screenmanager.current = "Level 7 defend 2"
                h.defense += 1
            elif h.defense == 3:
                game.screenmanager.current = "Level 7 defend 3"
                h.defense += 1
            elif h.defense == 4:
                game.lvl7defend4()
                game.screenmanager.current = "Level 7 defend 4"
                h.defense += 1
        else:
            game.screenmanager.current = "Level 7 death"


class Level_7_attack_1(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_7_attack_1()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_7_attack_1(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""You try to shoot an arrow at 
Revan, but he uses a windblast to
knock it out of the air, and proceeds
to deal a devastating blow to you.
You manage to put some distance between
the two of you and regroup.
\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp -= 70
        self.add_widget(Label(text=f"""Do you attack? Or Hold your ground""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        attackbutton = Button(text="Attack")
        defendbutton = Button(text="Defend")
        attackbutton.bind(on_press=self.attack)
        defendbutton.bind(on_press=self.defend)
        choice.add_widget(attackbutton)
        choice.add_widget(defendbutton)
        self.add_widget(choice)

    def attack(self, instance):
        if h.artifact == True:
            game.lvl7artifactattack()
            game.screenmanager.current = "Level 7 artifact attack"
        else:
            if h.hp > 0:
                game.screenmanager.current = "Level 7 attack 0"
            else:
                game.screenmanager.current = "Level 7 death"

    def defend(self, instance):
        if h.hp > 0:
            if h.defense == 0:
                game.screenmanager.current = "Level 7 defend 0"
                h.defense += 1
            elif h.defense == 1:
                game.screenmanager.current = "Level 7 defend 1"
                h.defense += 1
            elif h.defense == 2:
                game.screenmanager.current = "Level 7 defend 2"
                h.defense += 1
            elif h.defense == 3:
                game.screenmanager.current = "Level 7 defend 3"
                h.defense += 1
            elif h.defense == 4:
                game.lvl7defend4()
                game.screenmanager.current = "Level 7 defend 4"
                h.defense += 1
            else:
                game.screenmanager.current = "Level 7 death"


class Level_7_defend_0(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_7_defend_0()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_7_defend_0(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""Revan shoots a bolt of lightning at
you, but your quick reflexes allow you
to deflect it right back at him, and he
screams in pain
\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp -= 50
        self.add_widget(Label(text=f"""Maybe this is how you defeat him?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        attackbutton = Button(text="Attack")
        defendbutton = Button(text="Defend")
        attackbutton.bind(on_press=self.attack)
        defendbutton.bind(on_press=self.defend)
        choice.add_widget(attackbutton)
        choice.add_widget(defendbutton)
        self.add_widget(choice)

    def attack(self, instance):
        if h.artifact == True:
            game.lvl7artifactattack()
            game.screenmanager.current = "Level 7 artifact attack"
            pass
        else:
            if h.hp > 0:
                game.screenmanager.current = "Level 7 attack 0"
                pass
            else:
                game.screenmanager.current = "Level 7 death"
                pass

    def defend(self, instance):
        if h.hp > 0:
            if h.defense == 0:
                game.screenmanager.current = "Level 7 defend 0"
                h.defense += 1
            elif h.defense == 1:
                game.screenmanager.current = "Level 7 defend 1"
                h.defense += 1
            elif h.defense == 2:
                game.screenmanager.current = "Level 7 defend 2"
                h.defense += 1
            elif h.defense == 3:
                game.screenmanager.current = "Level 7 defend 3"
                h.defense += 1
            elif h.defense == 4:
                game.lvl7defend4()
                game.screenmanager.current = "Level 7 defend 4"
                h.defense += 1
        else:
            game.screenmanager.current = "Level 7 death"


class Level_7_defend_1(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_7_defend_1()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_7_defend_1(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""Revan, now in pain, fires a fireball.
Luckily your parrying skills are unmatched,so 
you are able to shoot it back at him.Revan was
not expecting you to match his skill
\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp -= 50
        self.add_widget(Label(text=f"""Keep it up!""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        attackbutton = Button(text="Attack")
        defendbutton = Button(text="Defend")
        attackbutton.bind(on_press=self.attack)
        defendbutton.bind(on_press=self.defend)
        choice.add_widget(attackbutton)
        choice.add_widget(defendbutton)
        self.add_widget(choice)

    def attack(self, instance):
        if h.artifact == True:
            game.lvl7artifactattack()
            game.screenmanager.current = "Level 7 artifact attack"
        else:
            if h.hp > 0:
                game.screenmanager.current = "Level 7 attack 0"
            else:
                game.screenmanager.current = "Level 7 death"

    def defend(self, instance):
        if h.hp > 0:
            if h.defense == 0:
                game.screenmanager.current = "Level 7 defend 0"
                h.defense += 1
            elif h.defense == 1:
                game.screenmanager.current = "Level 7 defend 1"
                h.defense += 1
            elif h.defense == 2:
                game.screenmanager.current = "Level 7 defend 2"
                h.defense += 1
            elif h.defense == 3:
                game.screenmanager.current = "Level 7 defend 3"
                h.defense += 1
            elif h.defense == 4:
                game.lvl7defend4()
                game.screenmanager.current = "Level 7 defend 4"
                h.defense += 1
        else:
            game.screenmanager.current = "Level 7 death"


class Level_7_death(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_7_death()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_7_death(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""As you ready yourself and look for
an opportunity to strike, Revan blinds you.
In a state of disorientation, he uses a wind
blast and pushes you off the mountain.
All you can do is scream as you fall to
your death. You came so close to being a
hero, but you could not succeed.
Rest now and be at peace.
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Game Over""", color=(0, 0, 0, 1)))


class Level_7_defend_2(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_7_defend_2()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_7_defend_2(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""You are stronger than Revan anticipated.
He throws a volley of knives at
you, but you manage to sidestep
and hit him from the side!
\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp -= 50
        self.add_widget(Label(text=f"""Keep it up!""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        attackbutton = Button(text="Attack")
        defendbutton = Button(text="Defend")
        attackbutton.bind(on_press=self.attack)
        defendbutton.bind(on_press=self.defend)
        choice.add_widget(attackbutton)
        choice.add_widget(defendbutton)
        self.add_widget(choice)

    def attack(self, instance):
        if h.artifact == True:
            game.lvl7artifactattack()
            game.screenmanager.current = "Level 7 artifact attack"
        else:
            if h.hp > 0:
                game.screenmanager.current = "Level 7 attack 0"
            else:
                game.screenmanager.current = "Level 7 death"

    def defend(self, instance):
        if h.hp > 0:
            if h.defense == 0:
                game.screenmanager.current = "Level 7 defend 0"
                h.defense += 1

            elif h.defense == 1:
                game.screenmanager.current = "Level 7 defend 1"
                h.defense += 1

            elif h.defense == 2:
                game.screenmanager.current = "Level 7 defend 2"
                h.defense += 1

            elif h.defense == 3:
                game.screenmanager.current = "Level 7 defend 3"
                h.defense += 1

            elif h.defense == 4:
                game.lvl7defend4()
                game.screenmanager.current = "Level 7 defend 4"
                h.defense += 1

        else:
            game.screenmanager.current = "Level 7 death"


class Level_7_defend_3(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_7_defend_3()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_7_defend_3(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""Your furious opponent shouts in a language
long forgotten, transforming into a wolf to
attack you.After he lunges on you, you manage
to throw him off and hit him with an arrow,
destroying his wolf form
\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp -= 50
        self.add_widget(Label(text=f"""You’re almost done!""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        attackbutton = Button(text="Attack")
        defendbutton = Button(text="Defend")
        attackbutton.bind(on_press=self.attack)
        defendbutton.bind(on_press=self.defend)
        choice.add_widget(attackbutton)
        choice.add_widget(defendbutton)
        self.add_widget(choice)

    def attack(self, instance):
        if h.artifact == True:
            game.lvl7artifactattack()
            game.screenmanager.current = "Level 7 artifact attack"
        else:
            if h.hp > 0:
                game.screenmanager.current = "Level 7 attack 0"
            else:
                game.screenmanager.current = "Level 7 death"

    def defend(self, instance):
        if h.hp > 0:
            if h.defense == 0:
                game.screenmanager.current = "Level 7 defend 0"
                h.defense += 1
            elif h.defense == 1:
                game.screenmanager.current = "Level 7 defend 1"
                h.defense += 1
            elif h.defense == 2:
                game.screenmanager.current = "Level 7 defend 2"
                h.defense += 1
            elif h.defense == 3:
                game.screenmanager.current = "Level 7 defend 3"
                h.defense += 1
            elif h.defense == 4:
                game.lvl7defend4()
                game.screenmanager.current = "Level 7 defend 4"
                h.defense += 1
        else:
            game.screenmanager.current = "Level 7 death"


class Level_7_defend_4(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_7_defend_4()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_7_defend_4(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""‘Ho-How are you still alive!!!’Shouts Revan 
as he draws his sword. You can
see him bleeding profusely,it’s 
a miracle he is still standing.

After getting into a rather shabby form,
he attempts to strike you, but you knock
the sword out of his hand and cut him
down with ease.Revan has been defeated

You fall on your knees, your foes defeated.
All the pain,screams and nightmares can now 
be put to rest knowing Revan’s evil will 
never hurt anyone.

Your journey ends here hero.The future is for you to decide.
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Thank you {h.name} of {h.home}.""", color=(0, 0, 0, 1)))


class Level_7_artifact_attack(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_7_artifact_attack()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_7_artifact_attack(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""You charge at Revan with your {h.weapon},
but before you can strike a blinding
flash knocks out both of you. 
When you come to your senses, you see
Revan on the ground,motionless.You approach
him cautiously, but you soon realise he is
dead. Next to him are shards of what appears
to be sapphire.After close examination,
you realise it’s the same sapphire you found
in the camp all those days ago.
It all makes sense, this is why Hera herself was guarding it.
It must have some special enchantments,
Which is why Hera asked you to take it to Revan.

You fall on your knees, your foes defeated.
All the pain,screams and nightmares can now
be put to rest knowing Revan’s evil will never
hurt anyone.

Your journey ends here hero.The future is for you to decide.
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Thank you {h.name} of {h.home}""", color=(0, 0, 0, 1)))


class Level_5_solo(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):

        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl5_solo()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
        )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def lvl5_solo(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
You leap through a window, and start
to scale down the wall. You move 
quickly, but not quick enough. The 
mercenaries start to close in. So 
you climb into the closest window. 
You quickly lock and barricade the 
door just as men rush inside through 
the window. You swiftly attack with 
your {h.weapon} and put them to rest. 
A couple more try to enter, but the 
bodies have piled up by the window. 
They can't enter. You use this 
opportunity to baricade the window 
even more. Suddenly a deafening thud 
comes from the door of the room. 
They must be using a battering ram 
to break down the room.

You move aside and let them enter 
and attack them mercilessly one by 
one. You see a wizard and he casts a 
spell towards you.

""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp *= 0.9
        self.add_widget(Label(text=f""" """, color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Label(text=" ")
        fIghtbutton = Button(text="MOVE ON")
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def FIGHT(self, instance):
        if h.race == "Human":
            game.screenmanager.current = "Level 5 solo Human"
        else:
            game.lvl5soloNH()
            game.screenmanager.current = "Level 5 solo Not Human"


class Level_5_solo_human(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, )
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_5_solo_human()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
            )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.lvl5solo()
        game.screenmanager.current = "Level 5 solo"

    def level_5_solo_human(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
The wizard tries but he misses
Once you spot him you make your
way to him swiftly dodging his 
attacks. When you come within 
3 ft, you lunge and grab the wand
out of his hand. But because he 
holds on tighter than expected 
and the wand breaks. A huge energy 
blast is created which knocks you 
off your feet. You are thrown to 
a wall and you see all your enemies 
being just as thrown or 
disintegrating. The wizard himself was 
burnt to bits. You look around to see 
the fort starting to crumble. Hell, 
the blast destroyed the fort's walls 
and pillars. It's going to crumble soon. 
You need to get out of here. Looking at
the damage you might have fifteen to 
twenty minutes at least.

""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""    """, color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        rationalbutton = Label(text=" ")
        aggressivebutton = Button(text="Next")
        aggressivebutton.bind(on_press=self.aggressive)
        choice.add_widget(rationalbutton)
        choice.add_widget(aggressivebutton)
        self.add_widget(choice)

    def aggressive(self, instance):
        if h.artifact == True:
            game.screenmanager.current = "Level 5 fort escape safe"
        else:
            game.lvl5fortescape()
            game.screenmanager.current = "Level 5 fort escape damaged"


class Level_5_solo_not_human(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, )
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_5_solo_not_human()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
            )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.lvl5solo()
        game.screenmanager.current = "Level 5 solo"

    def level_5_solo_not_human(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
The wizard hits you and slows you 
down for a minute. This is not 
good. Once you spot him you make 
your way to him swiftly dodging his 
attacks. When you come within 
3 ft, you lunge and grab the wand
out of his hand. But because he 
holds on tighter than expected 
and the wand breaks. A huge energy 
blast is created which knocks you 
off your feet. You are thrown to 
a wall and you see all your enemies 
being just as thrown or 
disintegrating. The wizard himself was 
burnt to bits. You look around to see 
the fort starting to crumble. Hell, 
the blast destroyed the fort's walls 
and pillars. It's going to crumble soon. 
You need to get out of here. Looking at
the damage you might have fifteen to 
twenty minutes at least.

""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp -= 50
        h.strength -= 50
        self.add_widget(Label(text=f"""    """, color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        rationalbutton = Label(text=" ")
        aggressivebutton = Button(text="Next")
        aggressivebutton.bind(on_press=self.aggressive)
        choice.add_widget(rationalbutton)
        choice.add_widget(aggressivebutton)
        self.add_widget(choice)

    def aggressive(self, instance):
        if h.artifact == True:
            game.screenmanager.current = "Level 5 fort escape safe"
        else:
            game.lvl5fortescape()
            game.screenmanager.current = "Level 5 fort escape damaged"


class Level_5_fort_escape(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, )
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_5_fort_escape()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
            )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.lvl5solo()
        game.screenmanager.current = "Level 5 solo"

    def level_5_fort_escape(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
You rush through room after room
looking for a way out. In one room,
you find Hera's desk littered with 
papers. You find on there a floor 
plan of the fort. You grab the floor 
plan and rush to the gardens, the 
closest area not under a roof. You 
reach the gardens as one of the further
wings crumble. According to the floor 
plan that was the oldest wing and was 
under heavy reconstruction. Now in open 
space, you refer the map again. There's 
a secret pathway near the inner courtyard 
which leads to Mount Lynaru. As you start 
to walk toward there Hera comes up behind 
you. She looks badly damaged, it seems the 
shockwave impacted her as well. 
"You! How dare you destroy my fort? 
I am Hera commander-in-cheif of--"

"Yeah I know all that, can you please skip 
to the part where you tell me something 
I don't know already?"

"AARGHH, I'm gonna kill you. I challenge 
you to a duel right here right now."

""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f""" Do you accept? """, color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        rationalbutton = Button(text="Accept")
        aggressivebutton = Button(text="Decline")
        rationalbutton.bind(on_press=self.rational)
        aggressivebutton.bind(on_press=self.aggressive)
        choice.add_widget(rationalbutton)
        choice.add_widget(aggressivebutton)
        self.add_widget(choice)

    def rational(self, instance):
        game.lvl5da()
        game.screenmanager.current = "level 5 duel accept"

    def aggressive(self, instance):
        game.screenmanager.current = "level 5 duel decline"


class Level_5_Duel_Decline(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, )
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_5_duel_decline()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
            )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.lvl5solo()
        game.screenmanager.current = "Level 5 solo"

    def level_5_duel_decline(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
"Yeah, I'm gonna pass." You say 
and move on to the courtyard. 
However when you're back is turned, 
Hera fires an arrow at you, 
aiming for your head. What you 
didn't know was that Hera is one the 
best archers that money can buy. She 
can shoot arrows at pretty far distances, 
quite accurately. Her throw finds its 
aim and hits you on the back of the 
head, killing you instantly. 
            GAME OVER
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f""" GAME OVER """, color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        rationalbutton = Label(text=" ")
        aggressivebutton = Label(text=" ")
        choice.add_widget(rationalbutton)
        choice.add_widget(aggressivebutton)
        self.add_widget(choice)


class Level_5_Duel_Accept(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_5_duel_Accept()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
        )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.lvl5solo()
        game.screenmanager.current = "Level 5 solo"

    def level_5_duel_Accept(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
"Alright, let's finish this," you say
as you draw your {h.weapon}. Hera draws 
her weapon. It is an intricately carved 
long bow. You try and guess the amount 
of arrows she might have. There's 30 m
between you and her, even an amateur 
can shoot straight within 3 - 5 tries. 
She draws and releases an arrow with
lightning speed, and it barely misses 
you. If you don't move, she'll kill you 
in the next attempt. You start to run in
a zig - zag manner toward her. Using the 
trees in the garden as cover. Whiile you 
take cover you hear a crash, when you look 
back you see that the building behind Hera 
crumbled, and see her body crushed under 
the debris. This was convienient. You move on
to the courtyard. Thanks to the map you find
secret passage way easily without much difficulty
You are on your way now to Mount Lynaru.  
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f""" GAME OVER """, color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        rationalbutton = Label(text=" ")
        aggressivebutton = Button(text="NEXT")
        aggressivebutton.bind(on_press=self.aggressive)
        choice.add_widget(rationalbutton)
        choice.add_widget(aggressivebutton)
        self.add_widget(choice)

    def aggressive(self, instance):
        game.screenmanager.current = "Level 6 Intro"


class Level_5_fort_escape_damage(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, )
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_5_fort_escape_damage()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
            )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.lvl5solo()
        game.screenmanager.current = "Level 5 solo"

    def level_5_fort_escape_damage(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
You try to move a little bit, but
find that you've broken some of 
your bones. Your ribs hurt, you're
sore in the back, and your shoulder 
is dislocated. But you can't stay 
here any longer. You rush through 
room after room looking for a way 
out. In one room, you find Hera's 
desk littered with papers. You find 
on there a floor plan of the fort.
You grab the floor plan and rush to 
the gardens, the closest area not 
under a roof. You reach the gardens 
as one of the further wings crumble. 
According to the floor plan that was 
the oldest wing and was under heavy 
reconstruction. Now in open space, 
you refer the map again. There's a 
secret pathway near the inner 
courtyard which leads to Mount Lynaru. 
As you start to walk toward there Hera 
comes up behind of you. She looks badly 
damaged, it seems the shockwave impacted
her as well. 

"You! How dare you destroy my fort? 
I am Hera commander-in-cheif of--"

"Yeah I know all that, can you please skip 
to the part where you tell me something 
I don't know already?"

"AARGHH, I'm gonna kill you. I challenge 
you to a duel right here right now."

""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp *= 0.7
        h.strength *= 0.7
        h.stealth *= 0.7
        self.add_widget(Label(text=f""" Do you accept? """, color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        rationalbutton = Button(text="Accept")
        aggressivebutton = Button(text="Decline")
        rationalbutton.bind(on_press=self.rational)
        aggressivebutton.bind(on_press=self.aggressive)
        choice.add_widget(rationalbutton)
        choice.add_widget(aggressivebutton)
        self.add_widget(choice)

    def rational(self, instance):
        game.lvl5da()
        game.screenmanager.current = "level 5 duel accept"

    def aggressive(self, instance):
        game.screenmanager.current = "level 5 duel decline"


class Level_5_solo_Game_over(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, )
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_5_soloko()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text="")
        grid.add_widget(back_button)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
            )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_5_soloko(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
You try and fight all of them, but 
ALAS it is of no use. The enemies are 
too many and your strength too little.
More mercenaries enter from behind Hera, 
while she looks on at them killing you 
with a sadistic smile. They cut deep into 
you, they stab you front, back and center. 
You somehow make your way to Hera and stab 
her in the stomach hard enough to kill her.
Now you fall to the ground ready for death, 
but not ready to die. You eventually fall 
into the eternal sleep, with oyur warrior
spirit still fighting. 
        GAME OVER  
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f""" GAME OVER """, color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        rationalbutton = Label(text=" ")
        aggressivebutton = Label(text=" ")
        choice.add_widget(rationalbutton)
        choice.add_widget(aggressivebutton)
        self.add_widget(choice)


class Level_5_group_Game_over(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_5_group_gameOver()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text="")
        grid.add_widget(back_button)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
            )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_5_group_gameOver(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
"No, I think we can take them on,"
you say. "After all we did win the
war doing this tons of times."

They agree, but decide to leave the
secret passageway open nonetheless.
When the soldiers arrive the entire 
group launches themselves into battle 
head first. However it is quite 
evident to you that you guys cannot 
keep this up. There's too many men. 
There's only one thing you can do. 
You tell Caldor to call for a retreat. 
While everyone is retreating, you 
stay back and hold up as many soldiers 
as possible. Soon only Caldor and you 
are left fighting the mercenaries. 
"Get out of here Caldor," you tell him.
"One of us needs to stay back to allow 
the others to retreat safely." 

"Yeah {h.name}, I'm staying back." 

"No Caldor, I should stay back, because 
the others need your skills. Go join 
them I'll hold them off." With that you 
leave Caldor a safe path to retreat as 
you keep many mercenaries engaged. 

"So long brother,"says Caldor as he 
leaves and closes the cabinet behind him. 
Now, there can only be one way for you to 
surivive fight your way out the hard way. 
Alas, you cannot. As soon as Caldor leaves 
a mercenary throws a grenade into the room. 
It explodes killing you and everyone in 
the room, instantaneously.
        GAME OVER  
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f""" GAME OVER """, color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        rationalbutton = Label(text=" ")
        aggressivebutton = Label(text=" ")
        choice.add_widget(rationalbutton)
        choice.add_widget(aggressivebutton)
        self.add_widget(choice)


class Level_5_group_inside(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):

        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl5_group()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
        )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def lvl5_group(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
You grab a bow and fire an incendiary 
arrow at the oncoming horde. You are 
able to push back the oncoming attack 
enough to close and barricade the door 
once again. 
“Alright, so we need a plan. Deruvur 
how many did you see?” 

“About two on each stair all the way 
till the entrance.” 

“Is there another entrance/exit?” 

“Not that we can use now. We must fight
this out.” 

“Alright Burk, I need you to take a bow 
and give us cover. Ruz, you and {h.name} 
are to protect Burk from incoming attackers. 
Go for clean kills; aim for head, triceps, 
and thighs only. If we can’t kill them at 
least make it agonizing for them to pick 
up weapons against us. I will also use a 
bow and help Burk. Deruvur you bring up the 
rear with arrows, weapons and supplies. 
Once we get out they will no doubt try to 
surround us. Then remember circle formation. 
{h.name}, Ruz and Deruvur in the front, Burk 
and I will get long range targets from the 
centre.”

“Ruz open the door and throw a grenade to 
disorient them. I’ll follow it by smoke 
arrows. Burk and {h.name} start taking down 
people.”

“Everybody got it?” We nod. “Good, then let’s
go.” 

The plan goes pretty according to how you 
discussed it. The enemies may be a lot but 
between Burk’s marksmanship, and your close 
range blows, the entire team was able to get 
out, without a scratch.

The entire town is on high alert,and the city
gates are closed.

‘Well that was worth a short’

The soldiers quickly surround you

‘Just like the old days guys,’ says Caldor
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp *= 0.9
        self.add_widget(Label(text=f""" """, color=(0, 0, 0, 1)))
        if h.strength > 500.00 and h.charisma == True:
            h.hp *= 0.9
        else:
            h.hp *= 0.75
        h.strength *= 0.9
        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Label(text=" ")
        fIghtbutton = Button(text="MOVE ON")
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def FIGHT(self, instance):
        game.lvl5groupoutside()
        game.screenmanager.current = "Level 5 group outside"


class Level_5_group_outside(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):

        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl5_groupOutside()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        back_button.add_widget(on_press=self.back)
        grid.add_widget(back_button)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
        )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.lvl5groupoutside()
        game.screenmanager.current = "Level 5 group outside"

    def lvl5_groupOutside(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
The circle formation works for a 
long time. It seems your military 
training never left you. You 
effectively move through the army 
of soldiers. But they seem to be 
never-ending. There weren’t these 
many soldiers before. Then you see 
a warlock chanting incantations with
his staff. You tell Caldor to shoot 
him down, but the arrows do nothing 
to him. 
“Then let me break formation and kill
 him myself.” 

“No, {h.name} it is too risky.” 

"Well, it’s riskier staying here. I’m 
going on my own.” 

With that you break off the circle and 
head toward the warlock. Caldor and Burk 
do give some backup initially to allow 
you to cover more ground. 
You reach the warlock and … 
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp *= 0.9
        self.add_widget(Label(text=f""" """, color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Label(text=" ")
        fIghtbutton = Button(text="MOVE ON")
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def FIGHT(self, instance):
        if h.artifact == True:
            game.screenmanager.current = "Level 5 group outside warlock"
        else:
            game.lvl5OWnoArtifact()
            game.screenmanager.current = "Level 5 group outside no artifact"


class Level_5_group_warlock_na(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl5_groupOutside()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
        )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.lvl5groupoutside()
        game.screenmanager.current = "Level 5 group outside"

    def lvl5_group(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
And you snap the warlock's staff
into two pieces. Immediately the
warlock disintegrates. A shockwave 
is released which is so powerful
that neighbouring buildings are 
beginning to crumble. Even you 
are thrown aside like a rag doll.
You stand up, but realize that 
everything hurts in all the wrong 
places. Your ribs feel broken, you
your back is sore, you can barely 
breathe for a while. When you can 
finally sit up you see that the 
large army you were fighting was 
just a spell by the warlock. In 
reality you might've fought only 
a tenth of that.

Your comrades are fine, as they 
were far away and felt less of the
shockwave, and are now finishing 
off the now tiny army. Suddenly 
everything starts to go dark so 
you lay down for a while.

...

...

When you wake up you see your 
comrades beside you. You slept 
for a day they say. Hera ran away, 
and after the battle there was 
no one to take care of the locals. 
The locals told your comrades to 
stay and rebuild the city. To build 
it so that no one can rule them 
again. Your buddies have agreed to 
this cause, though they still want 
to go after Hera. You tell them you
are leaving soon to go for 
Mount Lynaru. 

Revan needs to pay for what he did... 
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp *= 0.75
        h.strength *= 0.75
        h.stealth *= 0.75
        self.add_widget(Label(text=f""" """, color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Label(text=" ")
        fIghtbutton = Button(text="MOVE ON")
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 6 Intro"


class Level_5_group_warlock(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl5_groupw()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
        )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.lvl5groupoutside()
        game.screenmanager.current = "Level 5 group outside"

    def lvl5_groupw(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
And you snap the warlock's staff
into two pieces. Immediately the
warlock disintegrates. A shockwave 
is released which is so powerful
that neighbouring buildings are 
beginning to crumble.You are left
un harmed for some reason. Then 
you see the saphire glowing. It 
must be absorbing the force of 
the shockwave. You look around
and see that the large army you 
were fighting was just a spell by 
the warlock. In reality you 
might've fought only a tenth of that.

Your comrades are fine, as they 
were far away and felt less of the
shockwave, and are now finishing 
off the now tiny army. Suddenly 
everything starts to go dark so 
you lay down for a while.

...

...

When you wake up you see your 
comrades beside you. You slept 
for a day they say. Hera ran away, 
and after the battle there was 
no one to take care of the locals. 
The locals told your comrades to 
stay and rebuild the city. To build 
it so that no one can rule them 
again. Your buddies have agreed to 
this cause, though they still want 
to go after Hera. You tell them you
are leaving soon to go for 
Mount Lynaru. 

Revan needs to pay for what he did... 
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        self.add_widget(Label(text=f""" """, color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Label(text=" ")
        fIghtbutton = Button(text="MOVE ON")
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 6 Intro"


class Level_4_intro_page(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_4_intro_page()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=4, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_4_intro_page(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""The road has been long.On the
way you learnt more about Revan, 
the man leading the mercenaries.Before
long you could see it,Ruthorham’s gold
central spire towering above everything
surrounding it.On the road you had 
heard that a group of mercenaries had 
essentially taken over one of the town’s 
forts. As soon as you entered the town, 
you knew the rumours were true. The vile 
mercenaries were roaming the streets
like they owned the damn place. You’re almost 
tempted to head straight to the fort and take 
them all on at once.\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Do you give in to your temptations? Or tackle it more rationally.
""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        rationalbutton = Button(text="Do not attack the fort")
        aggressivebutton = Button(text="Attack the fort")
        rationalbutton.bind(on_press=self.rational)
        aggressivebutton.bind(on_press=self.aggressive)
        choice.add_widget(rationalbutton)
        choice.add_widget(aggressivebutton)
        self.add_widget(choice)

    def rational(self, instance):
        game.lvl4sane()
        game.screenmanager.current = "Level 4 sane"

    def aggressive(self, instance):
        game.lvl4forta()
        game.screenmanager.current = "Level 4 fort attack"


class Level_4_sane(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_4_sane()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 4 Intro"

    def level_4_sane(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)), scroll_distance=80)
        texta = Label(text=f"""You calm yourself down, and head to
the town inn to get more information.
You find a nice corner for yourself and
start looking around for suspicious folk.
No need to look very hard though, as you
see 4 hooded men staring at you, they seem
the unsavoury kind. You retire to your
chambers, knowing they are following you.
You enter a dark hallway and immediately 
draw out your {h.weapon}, but before you can
turn around you’re knocked on the ground,with
the men surrounding you.

“Slow as ever {h.name},It’s a wonder you’re 
still alive without us”

You recognized his voice immediately
”Screw you Deruvur!” You shout.

Your war buddies always knew how to make you
look like a fool, you just didn't expect to see
them here.

“What are you guys doing here anyway?”

“Well we heard about the inn at Dragontail Walk,
traced it to Hera. We’ve been chasing her ever since
the war ended. Why are you here?” 

“I was in Dragontail Walk when the attack
happened,hadnto find out who was behind it.
Who is this Hera anyway?

“She is Revan’s right hand man. She was 
there the night our squad was sent to Dewvault.
We’re positive she is the one who killed Haldi
that night. We have to avenge him”

“Woah, there’s no we here guys, this is my fight.
I need to do this alone”

The guys look at each other,”Are you 
joking {h.name},you’d have to be crazy to
think you can take them all out alone.
It’s a whole bloody army.You better come
with us if you want this to succeed”
\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Do you take their help? Or do you still prefer being a lone wolf
""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        lonebutton = Button(text="Refuse help")
        helpbutton = Button(text="Accept help")
        lonebutton.bind(on_press=self.lone)
        helpbutton.bind(on_press=self.help)
        choice.add_widget(lonebutton)
        choice.add_widget(helpbutton)
        self.add_widget(choice)

    def lone(self, instance):
        game.screenmanager.current = "Level 4 lone"

    def help(self, instance):
        game.lvl4Help()
        game.screenmanager.current = "Level 4 help"


class Level_4_lone(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_4_lone()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
            )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.lvl4sane()
        game.screenmanager.current = "Level 4 sane"

    def level_4_lone(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""“I’m sorry guys, you’d just slow me down”

“Okay you’ve officially lost it buddy. Do you
have a plan? What do you think you’ll do even
if you somehow manage to climb those massive 50
feet walls undetected. Do you expect Hera will
just surrender after seeing you amazing climbing
skills?You don’t even have the gear to take them on”

“....”

“Yeah I thought so, now shut up and follow us”

You begrudgingly tag along. 
They were right though, it’s not like you could have 
done anything alone.
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=1, rows=1)
        nextbutton = Button(text="Next")
        nextbutton.bind(on_press=self.proceed_1)
        choice.add_widget(nextbutton)
        self.add_widget(choice)

    def proceed_1(self, instance):
        game.screenmanager.current = "Level 4 safehouse"


class Level_4_help(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_4_help()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
            )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.lvl4sane()
        game.screenmanager.current = "Level 4 sane"

    def level_4_help(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""“I guess you are right, just like
the old days eh”

“That’s my boy!Now quickly, follow us to
our room, we have a plan you might be interested
in hearing. Oh and drink this, for luck.
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        self.add_widget(Label(text=f""""""))
        h.stealth += 50
        print(h.stealth)
        choice = GridLayout(cols=1, rows=1)
        nextbutton = Button(text="Next")
        nextbutton.bind(on_press=self.proceed_1)
        choice.add_widget(nextbutton)
        self.add_widget(choice)

    def proceed_1(self, instance):
        game.screenmanager.current = "Level 4 safehouse"


class Level_4_fort_attack(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_4_fort_attack()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
            )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 4 Intro"

    def level_4_fort_attack(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""As you get closer to the fort
you start seeing less of the mercenaries.
You survey the location and find what seems
to be a rather neglected portion of the wall.
After making sure the coast was clear, you
climb the wall and get inside.
It’s quiet, too quiet.

You enter the first room to your left,there you
find shipping manifests.It seems they packed everything
the night before and left for Mount Lynaru.You grab whatever
information you can and exit the room.As soon as you
step into the main courtyard you hear a voice

‘What’s this, a rat in the darkness’

You look up and see a commander staring at you
from the walls.It’s Hera!

‘Darling, I’m afraid you’re trespassing,and those
notes you found in there are confidential.Around 
here that sort of an offence means execution.
Get him boys!’

You pull out your {h.weapon} as mercenaries start 
rappelling down the walls.
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=1, rows=1)
        nextbutton = Button(text="Next")
        nextbutton.bind(on_press=self.proceed_1)
        choice.add_widget(nextbutton)
        self.add_widget(choice)

    def proceed_1(self, instance):
        if h.hp > 350.00:
            game.lvl5solo()
            game.screenmanager.current = "Level 5 solo"
        else:
            game.screenmanager.current = "Level 5 solo Game Over"


class Level_4_safehouse(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_4_safehouse()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.lvl4sane()
        game.screenmanager.current = "Level 4 sane"

    def level_4_safehouse(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""They take you to an underground room.
After fumbling around with the keys,Deruvur
manages to open the door.

‘What is this place?’ You ask

‘This is our safehouse, make yourself comfortable’

You walk around the room and find everyone’s gear
stacked in a corner. They were still as unorganized
as they were during the war.

Caldor tapped your shoulder,’Mind joining us, we’ll
show you the plan’

‘We suspect Revan and Hera are in town, 
specifically in the fort. Lucky for us their 
guards don’t have a very strong sense of loyalty. 
We bribed one of them and he’ll be here soon with 
the fort schematics and Revan’s location. I’d 
suggest get some sleep till he arrives”

A few hours later you hear a knock on the door.

Caldor gets up and says ‘What is the music of life?’

‘Silence my friend’ says the man on the door

Caldor opens the door,’Took you long enough,do you have 
the information?’

‘Yes’ says Anor,the spy. ‘But you won’t like it.Revan has
emptied the fort and is moving everyone to a base in Mt.Lynaru.
He wants to lay low for a while there. Here are the orders
he sent everyone. He left Hera in charge here’

‘Good job Anor,here’s your payment’,says Deruvur as he hands
him a pouch of gold.

Something feels off though.
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=1, rows=1)
        nextbutton = Button(text="Next")
        nextbutton.bind(on_press=self.proceed_1)
        choice.add_widget(nextbutton)
        self.add_widget(choice)

    def proceed_1(self, instance):
        if h.race == 'Dwarf':
            game.screenmanager.current = "Level 4 Dwarf"
        else:
            game.lvl4nodwarf()
            game.screenmanager.current = "Level 4 No Dwarf"


class Level_4_No_Dwarf(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):

        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_4_No_Dwarf()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 4 safehouse"

    def level_4_No_Dwarf(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""Anor quickly leaves. A few minutes later
you notice something stuck under the table.
You gather everyone around.It looks like a bomb

‘Anor!Should have expected he’d betray us too.
What do we do about this’

Suddenly you hear footsteps approaching the 
safehouse,and metal clanking.

‘Soldiers.He sold us out!Only way out is through
the door and they know it’ says Caldor 

‘Then let's not keep them waiting’ you say as you 
grab your {h.weapon}.You barge out the door together 
and see yourself surrounded by the mercenaries.
\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Do you fight them, or try and disappear?
""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        fightbutton = Button(text="Fight")
        escapebutton = Button(text="Run")
        fightbutton.bind(on_press=self.fight)
        escapebutton.bind(on_press=self.escape)
        choice.add_widget(fightbutton)
        choice.add_widget(escapebutton)
        self.add_widget(choice)

    def fight(self, instance):
        game.lvl5groupinside()
        game.screenmanager.current = "Level 5 group fight inside"

    def escape(self, instance):
        if h.stealth >= 550:
            game.lvl4disappear()
            game.screenmanager.current = "Level 4 disappear"
        else:
            game.screenmanager.current = "Level 4 no disappear"


class Level_4_disappear(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_4_disappear()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
            )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.lvl4nodwarf()
        game.screenmanager.current = "Level 4 No Dwarf"

    def level_4_disappear(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""Deruvur fires an arrow and tells you
all to duck. It explodes and creates
a blinding light,disorienting the
soldiers for a few seconds.You quickly
use all your smoke bombs to cover your
team’s escape as you cut through them.
You manage to get out,but the soldiers 
are chasing you. The entire town is on 
high alert,and the city gates are 
closed.

‘{h.name}, head for the sewers.Use them 
to get out of the city, we’ll stay here 
and cover keep them busy’

‘I’m not leaving you guys!’

‘No time to argue!This is our only shot at
getting to Revan’,with that,Caldor pushes 
you down the manhole. It’s a rough fall but
you can hear the fighting above.There is 
nothing you can do for them now.

After a few hours in horrible stench you make
it out of the sewers and emerge outside the
city. In the distance you see Mt.Lynaru.
Revan will pay,this time it’s personal.
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=1, rows=1)
        nextbutton = Button(text="Next")
        nextbutton.bind(on_press=self.proceed_1)
        choice.add_widget(nextbutton)
        self.add_widget(choice)

    def proceed_1(self, instance):
        game.screenmanager.current = "Level 6 Intro"


class Level_4_no_disappear(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_4_no_disappear()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
            )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.lvl4nodwarf()
        game.screenmanager.current = "Level 4 No Dwarf"

    def level_4_no_disappear(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""Deruvur fires an arrow and tells you
all to duck. It explodes and creates a
blinding light,disorienting the soldiers
for a few seconds.You quickly use all your
smoke bombs to cover your team’s escape 
as you cut through them. You manage to get
out,but the soldiers are chasing you.
The entire town is on high alert,and the city
gates are closed.

‘Well that was worth a short’

The soldiers quickly surround you

‘Just like the old days guys’ says Caldor
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=1, rows=1)
        nextbutton = Button(text="Next")
        nextbutton.bind(on_press=self.proceed_1)
        choice.add_widget(nextbutton)
        self.add_widget(choice)

    def proceed_1(self, instance):
        game.screenmanager.current = "Level 5 group fight outside"


class Level_4_Dwarf(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_4_Dwarf()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
            )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 4 safehouse"

    def level_4_Dwarf(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""Anor quickly leaves. A few minutes later
you notice something stuck under the table.
You gather everyone around.It looks like a 
bomb

‘Anor!Should have expected he’d betray us too.
What do we do about this’

Suddenly you hear footsteps approaching the 
safehouse,and metal clanking.

‘Soldiers.He sold us out!Only way out is through
the door and they know it’ says Caldor

‘Actually,no’ says Deruvur as he slides a cabinet.
‘This is a secret passageway that leads to the old
underground tunnels.It’s small but we can easily fit.’

‘Why didn’t you tell us about this before?’

‘You never asked’
\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Do you fight them, or try and escape?
""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        fightbutton = Button(text="Fight")
        escapebutton = Button(text="escape")
        fightbutton.bind(on_press=self.fight)
        escapebutton.bind(on_press=self.escape)
        choice.add_widget(fightbutton)
        choice.add_widget(escapebutton)
        self.add_widget(choice)

    def fight(self, instance):
        if h.hp > 350.00:
            game.screenmanager.current = "Level 5 group fight inside"
        else:
            game.lvl5groupgameover()
            game.screenmanager.current = "Level 5 group game over"

    def escape(self, instance):
        game.lvl4dwarfescape()
        game.screenmanager.current = "Level 4 dwarf escape"


class Level_4_Dwarf_escape(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_4_Dwarf_escape()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav'
            )
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 4 Dwarf"

    def level_4_Dwarf_escape(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""The team quickly enters the passageway.
Before long, the bomb goes off and 
the walls of the safehouse collapse,
blocking the passageway entrance.
Only way out is ahead.

After a few hours in the dark passageway 
and tunnels you emerge outside the city.

‘What do we do now’? You ask

‘We came here for Hera, i’m not leaving till
she’s dead’

‘That’s your fight.I’m heading for the mountain,
for Revan’

‘Don’t be foolish {h.name}’ shouts Caldor

‘You didn't see what he did to Dragontail Walk!
I was there.All the screams,the lives lost,hell I
should have died there too! Revan needs to answer.
I don’t care if I die up there, I owe it to myself
to try.’

‘In that case,good luck.Remember you can always return here.
You know how to find us’

‘I do,I’ll see you guys soon’

You set out alone,Lynaru in the distance.
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=1, rows=1)
        nextbutton = Button(text="Next")
        nextbutton.bind(on_press=self.proceed_1)
        choice.add_widget(nextbutton)
        self.add_widget(choice)

    def proceed_1(self, instance):
        game.screenmanager.current = "Level 6 Intro"


class Level_3_intro_page(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):

        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_3_intro_page()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Label(text=" ")
        grid.add_widget(back_button)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def level_3_intro_page(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""You arrive at Tiefling village, exhausted
from spending days on the road. You
decide the best place to start the
investigation would be the village
tavern. After getting a much needed
drink, you start asking around about
Feca.When you ask the man behind the
counter, he points towards the half 
naked bearded man outside the bar.
’That’s him right there’.You had heard
stories of him being a drunk loudmouth,
but actually seeing him like that was rather
hilarious.\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Do you invite him for another round
or use a more direct method to
find out what he knows…""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        friendlybutton = Button(text="Be Friendly")
        aggressivebutton = Button(text="Be Aggressive")
        friendlybutton.bind(on_press=self.friendly)
        aggressivebutton.bind(on_press=self.aggressive)
        choice.add_widget(friendlybutton)
        choice.add_widget(aggressivebutton)
        self.add_widget(choice)

    def friendly(self, instance):
        if h.charisma == True:
            game.screenmanager.current = "Level 3 friendly charisma"
        else:
            game.lvl3fnoc()
            game.screenmanager.current = "Level 3 friendly no charisma"

    def aggressive(self, instance):
        if h.strength >= 500:
            game.lvl3aggressivey()
            game.screenmanager.current = "Level 3 aggressive yes"
        else:
            game.lvl3aggressiveno()
            game.screenmanager.current = "Level 3 aggressive no"


class Level_3_friendly_charisma(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_3_friendly_charisma()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 3 intro"

    def level_3_friendly_charisma(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
You walk up to him, he immediately
shouts “Th-There’s my drinking 
buddy! What say you buy me another 
round to old times eh pal”.

He must be rather desperate if he
made you, a complete stranger is 
buddy.

“Sure Feca, lets go get you a drink”.

You get two pints of mead and slowly 
watch him get drunk. For a rather tiny 
man he sure could hold his drink. You 
were worried you’d run out of cash 
before you got anything out of him. Then, 
he suddenly says,’Say what,you look 
trustworthy. Ya wanna share some secrets,
I’ll go first. Ya know that inn that was 
raided a few days ago, I supplied them
with the weapons. It was a proper massacre 
I hear, all thanks to my weapons. Their 
Ruthorham weapons looked like toys in 
front of my creations I tell ya!’

“So they were from Ruthorham?” you ask

“Where else would they be from, it’s where 
their dumb kind lurks all the time! Hey now, 
it’s your turn.Tell me a secret!”

“Ah-well that’s easy, I’m gay Feca”

“You’re WHAT! Ge-Get out of my sight.You and 
your kind are truly the scum of the Earth, 
worse than them Ruthorham folks yeah!”

“Oh well, as you say Feca,nice meeting you”

“Don’t talk to me!”

So the rumors of him being bigoted were true 
too. Doesn't matter though, he told you exactly 
where to go. After resting a little more you set 
out for Ruthorham the next morning\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Proceed to Ruthorham?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        continuebutton = Button(text="Continue")
        continuebutton.bind(on_press=self.proceed)
        choice.add_widget(Label(text=" "))
        choice.add_widget(continuebutton)
        self.add_widget(choice)

    def proceed(self, instance):
        game.screenmanager.current = "Level 4 Intro"


class Level_3_aggressive_yes(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_3_aggressive_yes()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 3 intro"

    def level_3_aggressive_yes(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""You walk up to him and grab
him by the neck 
“H-Hey let go of me!!”
“Guards!Guards!!”
You quickly punch him in the face
to silence him.You drag him to the
back of the inn and tie him to the
stable doors.
“Now Feca, These past few days have
been rather unpleasant for me, no
thanks to you.So don’t make me ask 
you twice.Who bought the weapons for 
the mercenaries that attacked the inn
on Dragontail Walk!”
“I-I don’t know what you’re talking
about!! Me swears!”
You punch him in the stomach and draw 
your {h.weapon}
“Do your worst! If I talk Hera will have 
my head!”

“If you don’t, Hera won’t get the chance to”

“Go to hell!”

This was taking too much time, you take out 
your knife and stab him in the gut. He 
screams and twitches.

” All right All right!! It was a group from 
Ruthorham. They warned me not to talk, now 
make this stop!!”

“See, that was easy, now hold still”

You bandage him up and release him.

“This never happened Feca, are we clear?”

“Y-Yes”

“Good”

With that out of the way, you now knew exactly where to go.
After resting a little more you set out for Ruthorham the 
next morning\n""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Proceed to Ruthorham?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        continuebutton = Button(text="Continue")
        continuebutton.bind(on_press=self.proceed)
        choice.add_widget(Label(text=" "))
        choice.add_widget(continuebutton)
        self.add_widget(choice)

    def proceed(self, instance):
        game.screenmanager.current = "Level 4 Intro"


class Level_3_aggressive_no(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_3_aggressive_no()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 3 intro"

    def level_3_aggressive_no(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""You walk up to him and grab
him by the neck
“H-Hey let go of me!!” “Guards!Guards!!”
You quickly punch him in the face
to silence him.You drag him to the 
back of the inn and tie him to the
stable doors.
“Now Feca, These past few days have
been rather unpleasant for me, no thanks
to you.So don’t make me ask you twice.Who
bought the weapons for the mercenaries that
attacked the inn on Dragontail Walk!”
“I-I don’t know what you’re talking about!! Me swears!”
You punch him in the stomach and draw your {h.weapon}
“Do your worst! If I talk Hera will have my head!”
“If you don’t, Hera won’t get the chance to”
“Go to hell!”
This was taking too much time, you take out your
knife and stab him in the gut. He screams and twitches.
He goes limp,his breathing is faint.You realise
you messed up.After releasing him you rush to the
village doctor and tell him Feca was stabbed in a
bar fight.The doctor says he’s unconscious
but may survive 

You blew it, now he won’t tell you anything
even if he survives. There must be some other
way to find out more about the attack. You head
to his shop and notice the lights are out, maybe
no one’s inside?You manage to break in through 
the back window.It’s pitch black, though you 
manage to light a lamp and look around. You 
find a fancy trunk with a huge padlock on
it. Using your {h.weapon} you break it and find
it’s full of gold from Ruthorham .That must mean 
his “clients” must be from Ruthorham, and that’s 
where you must go next. As you’re leaving you 
accidentally trip the lamp,and it lands directly
on his mead collection. The fire spreads quickly
and you manage to get out of there. Guards and
villagers alike quickly surround the burning
building.
“Stop right there {h.race}! Explain Yourself!""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f""" """, color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        nextbutton = Button(text="Next")
        nextbutton.bind(on_press=self.proceed_1)
        choice.add_widget(Label(text=" "))
        choice.add_widget(nextbutton)
        self.add_widget(choice)

    def proceed_1(self, instance):
        game.screenmanager.current = "Level 3 caught"


class Level_3_friendly_no_charisma(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_3_friendly_no_charisma()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 3 intro"

    def level_3_friendly_no_charisma(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
You walk up to him, he 
immediately shouts 
“Th-There’s my drinking buddy!
What say you buy me another 
round to old times eh pal”.
He must be rather desperate 
if he made you, a complete 
stranger is buddy.

“Sure Feca, lets go get you a 
drink."

You get two pints of mead and 
slowly watch him get drunk. For 
a rather tiny man he sure could 
hold his drink. You were worried 
you’d run out of cash before you 
got anything out of him. Desperate 
for information, you ask him 

“So,what do you know about the inn 
that burned down a few days ago."

He looked at you suspiciously.

“No-Nothing! Why do you ask!Ya know 
what, you’re not my buddy!A buddy 
won’t ask incriminating questions
like that.N-Now get out before I 
call the guards!!”

You blew it, now he won’t tell you 
anything. There must be some other 
way to find out more about the 
attack.You head to his shop and 
notice the lights are out, maybe 
no one’s inside?You manage to break
in through the back window. It’s pitch 
black, though you manage to light a lamp 
and look around. You find a fancy trunk 
with a huge padlock on it. Using your 
{h.weapon} you break it and find it’s 
full of gold from Ruthorham. That must 
mean his “clients” must be from Ruthorham, 
and that’s where you must go next.

As you’re leaving you accidentally trip 
the lamp,and it lands directly on his 
mead collection. The fire spreads
quickly and you manage to get out 
of there. Guards and villagers alike 
quickly surround the burning building.

“Stop right there {h.race}! 
Explain Yourself!""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f""" """, color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        nextbutton = Button(text="Next")
        nextbutton.bind(on_press=self.proceed_1)
        choice.add_widget(nextbutton)
        self.add_widget(choice)

    def proceed_1(self, instance):
        game.screenmanager.current = "Level 3 caught"


class Level_3_caught(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):

        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_3_caught()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 3 intro"

    def level_3_caught(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
“Woah now, let’s all just calm down.
That was nothing more than an accident,
I’m sure we can find a compromise here."

You throw a pouch of Ruthorham gold you 
took from the trunk.

“That pouch is more valuable than anything 
either of you own, let me go and it’s all 
yours."

One of the guards slowly approaches the pouch
and picks it up.

“By the Gods, it’s Ruthorham gold!”

The captain of the guards fires an arrow that
whizzes past your ear.

“Thanks for the treasure scum!”

You need to think fast.
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Take them head on or try 
and take them out one by one? """, color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        attackbutton = Button(text="Be Aggressive")
        tacticalbutton = Button(text="Be Tactical")
        attackbutton.bind(on_press=self.attack)
        tacticalbutton.bind(on_press=self.tactical)
        choice.add_widget(attackbutton)
        choice.add_widget(tacticalbutton)
        self.add_widget(choice)

    def attack(self, instance):
        if h.strength >= 500:
            game.lvl3attack()
            game.screenmanager.current = "Level 3 attack"
        else:
            game.lvl3attackd()
            game.screenmanager.current = "Level 3 attack death"

    def tactical(self, instance):
        if h.charisma == True:
            game.screenmanager.current = "Level 3 tactical"
        else:
            game.screenmanager.current = "Level 3 tactical death"


class Level_3_attack(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_3_attack()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 3 caught"

    def level_3_attack(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""You take out your {h.weapon} and charge
at the guards. Seeing the berserker in
front of them, the guards drop their weapons
and flee. The captain orders his men back, 
and attacks you with the ones remaining. 
You cut through them with ease, until it’s 
just you and the captain.“You monster!” Shouts
the captain as he swings his sword at you wildly.
You duck and strike him down.

As soon as the carnage is over, you head for
Ruthorham without looking back. You know you
can never return to Tiefling again.""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Proceed to Ruthorham?""", color=(0, 0, 0, 1)))
        if h.strength >= 550:
            h.hp -= 50
        else:
            h.hp -= 100
        print(h.hp)
        choice = GridLayout(cols=1, rows=1)
        continuebutton = Button(text="Continue")
        continuebutton.bind(on_press=self.proceed)
        choice.add_widget(continuebutton)
        self.add_widget(choice)

    def proceed(self, instance):
        game.screenmanager.current = "Level 4 Intro"


class Level_3_tactical(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_3_tactical()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 3 caught"

    def level_3_tactical(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""You use a smoke bomb and manage
to disappear in the chaos. After climbing a
nearby building, you use your bow to snipe 
off the guards below looking for you below. 
One by one they fall in the darkness of the
night.Once you cleared a path for yourself, 
you slowly descend and leave Tiefling village 
knowing you can never return.
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Proceed to Ruthorham?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=1, rows=1)
        continuebutton = Button(text="Continue")
        continuebutton.bind(on_press=self.proceed)
        choice.add_widget(continuebutton)
        self.add_widget(choice)

    def proceed(self, instance):
        game.screenmanager.current = "Level 4 Intro"


class Level_3_tactical_death(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_3_tactical_death()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 3 caught"

    def level_3_tactical_death(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""You try to run away hoping to
regroup and take the guards on later,
but you’re hit on the head with a stone
by a villager. Knocked out, the guards 
easily capture you and execute you!

Alas mighty hero! Your tale ends here....""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Game Over""", color=(0, 0, 0, 1)))


class Level_3_attack_death(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)
        self.orientation = "vertical"

        self.level_3_attack_death()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 3 caught"

    def level_3_attack_death(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f""" You take out your {h.weapon} and charge
at the guards, a brave gesture.But foolish.
They fire arrow after arrow till you drop 
dead in your tracks

Alas mighty hero! Your tale ends here....""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        self.add_widget(Label(text=f"""Game Over""", color=(0, 0, 0, 1)))


class Level_2_final_no(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl2_fno()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        grid.add_widget(Label(text=" "))
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def lvl2_fno(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
ALAS great warrior. The enemies are 
too many, and your strength too little. 
As you continue to fight your enemies, 
someone stabs you in the back. Almost 
on cue you are cut in the stomach and 
the neck. You are then left for dead. 
You never found out why they were out 
to kill you. You slowly give in to the 
Eternal Slumber, 
the warrior spirit still fighting...
            GAME OVER
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp -= 100
        h.strength += 50
        h.stealth += 50
        self.add_widget(Label(text=f"""GAME OVER""", color=(0, 0, 0, 1), font_size=20))
        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Label(text="")
        fIghtbutton = Label(text="")
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)


class Level_2_final_yes_d(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl2_s2no()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def lvl2_s2no(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
Yes! Greek fire is indestructable, it 
can catch anything on fire, be it metal 
or clothes. You dip a spare piece of wood 
into it, light it and throw it onto the 
incoming army. As they burn, you set up a 
rudimentary bomb using gunpowder and 
greek fire. However for the plan to work, 
you need to draw as many soldiers as 
possible into the armory tent.
You quickly position yourself at the exit 
and prepare to lure as many possible 
mercenaries in as possible. 

The enemies are lured into your trap and 
you leave just as the bomb explodes, 
igniting greek fire and spraying it all
over the camp. Because of the explosion, 
the entire camp is in complete disarray. 
Many men are dead. There is confusion all 
around, similar to what happened at the inn. 
You smile to yourself. 
Tonight was good... 
As you walk down your path you see the sun 
rise. A good omen, but a signal that a lot
of time has passed. You continue down the
path to meet Feca in Tiefling.

There are some things he has to answer for...
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        self.add_widget(Label(text=f"""Move to the next slide""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Label(text=" ")
        fIghtbutton = Button(text="Next")
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 3 intro"


class Level_2_final_yes(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl2_s2no()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def lvl2_s2no(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
The enemies are lured into your 
trap and you leave just as the 
bomb explodes, igniting greek 
fire and spraying it all over 
the camp. However, you are late 
by barely a second and your armor 
is caught on fire. You quickly 
run out of the camp lighting 
everything on fire. Once you have 
caused more chaos, you run to the 
lake to douse the fire. The fire 
douses out, but you have suffered 
some burns. Luckily as you were in 
the army, you know how to take care 
of them. But you are weakened for 
your journey. On a positive note, 
because of the explosion, the entire 
camp is in complete disarray.Many men 
are dead. There is confusion all around, 
similar to what happened at the inn. 
You smile to yourself. 
Tonight was good...

As you walk down your path you see the 
sun rise. A good omen, but a signal that 
a lot of time has passed. You continue 
down the path to meet Feca in Tiefling.
There are some things he has to answer for...
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp -= 100
        h.strength += 50
        h.stealth += 50
        self.add_widget(Label(text=f"""Move to the next slide""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Label(text=" ")
        fIghtbutton = Button(text="Next")
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 3 intro"


class Level_2_Sneak_2_SCES(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl2_s2s()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def lvl2_s2s(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
After you pick up the saphire you 
leave the camp. You continue down 
the path to meet Feca in Tiefling.

There are some things he must answer for...

""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp += 50
        h.strength += 75
        h.stealth += 75
        h.artifact = True
        print(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
              h.weapon, h.artifact)
        self.add_widget(Label(text=f"""Move Onto the next screen""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Label(text="")
        fIghtbutton = Button(text="MOVE ON")
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 3 intro"


class Level_2_Sneak_2_FAIL(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):

        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl2_s2f()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def lvl2_s2f(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
After you pick up the artifact you walk
straight to get out of the camp. But you 
see him. The {h.race} who was bathing
has come back. He got new armor somehow. 
The entire camp is facing you at the entrance 
to the armory. Fighting head on is stupid.
Before you cane figure an escape, 10 of the 
newbies charge. You fight them off with near 
ease, they've just been woken up that there 
is an intruder in the armory. They're sleep 
deprived and not at all battle hardened. But 
as you finish of those 10, 10 more attack, 
with more coming up behind them. 
You can't fight this entire army alone, 
it isn't possible. And definitely not in this 
setting where you are pinned down by the 
oncoming swarm. Wait! The armory is right 
behind you.

Maybe you can use something in there. 

Inside you find a barrel of greek fire. 
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp -= 50
        h.strength -= 50
        h.stealth += 50
        h.artifact = True
        self.add_widget(Label(text=f"""Do you use the Greek Fire, Yes or No?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Button(text="Yes")
        fIghtbutton = Button(text="No")
        sNeakbutton.bind(on_press=self.sneak)
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def sneak(self, instance):
        if h.race == "Dwarf":
            game.screenmanager.current = "Level 2 final Yes dwarf"
        else:
            game.lvl2S2finalyesnd()
            game.screenmanager.current = "Level 2 final Yes"

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 2 final No"


class Level_2_Sneak_2_No(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):

        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl2_s2no()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def lvl2_s2no(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
"No, I'm a new recruit from 
Tiefling," you say.

"Oh you stupid new recruits. Look
for the blue commander's tent. 
You can't miss it. And don't tell
the guards you're a new recruit. 
If Hera finds out I sent her a newbie, 
she'll have my head for breakfast!" 
He says running off.

You wander around a little trying
to find Hera's tent. You overhear 
that she is the commander-in-charge 
of the company and the right hand 
of Revan nowadays. Again that name,
Revan who is that? 

You see that the camp is organised 
quite intelligently. You found Hera's
tent just facing opposite to the 
"armory" tent. There has to be something 
important in there. You wouldn't risk the 
commander's life putting her in front of 
the armory. As you enter the tent, you 
find Hera sipping wine. 

"The troll sent me", you say remembering 
your war years. You immediately stand at 
attention.

"At ease," says Hera. "Do you know why we 
burnt down the inn?"

You nod no.

"We had to steal a very important saphire 
from the bank in the town. The inn is owned 
by the same person who owns the bank. When 
the inn burnt, he diverted most of his men 
to salvage whatever they could from the inn. 
Quite useless, as greek fire burns through 
everything. And while the bank was 
unprotected we robbed it."

You nod yes, this makes sense.

"Your job now", she continued "is to 
transport the artifact to Revan himself.
The saphire was cursed by an ancient 
warlock from the old country to bring 
the cause of Revan's death. Now if I send 
you on such a mission then I need your 
trust. You need to take this saphire to 
Feca of Tiefling. He knows how to crush 
cursed stones into powder, and destroy them. 
You will be given 7000 gold pieces upon the 
completion of this mission. 1350 now and the
rest later. Pick it up from the armory."

You go to the armory and pick up the saphire 
and the gold.""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""You go to the armory and
pick up the saphire and the gold.""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Label(text=" ")
        fIghtbutton = Button(text="Next")
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def FIGHT(self, instance):
        if h.stealth >= 550:
            game.lvl2S2sces()
            game.screenmanager.current = "Level 2 Sneak 2 successful"
        else:
            game.lvl2S2fail()
            game.screenmanager.current = "Level 2 Sneak 2 fail"


class Level_2_Sneak_2_Yes(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):

        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl2_s2yes()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def lvl2_s2yes(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
"Great! Saved me a lot of time." 
He says running off
You wander around a little trying
to find Hera's tent. You overhear 
that she is the commander-in-charge 
of the company and the right hand 
of Revan nowadays. Again that name,
Revan who is that? 

You see that the camp is organised 
quite intelligently. You found Hera's
tent just facing opposite to the 
"armory" tent. There has to be something 
important in there. You wouldn't risk the 
commander's life putting her in front of 
the armory. As you enter the tent, you 
find Hera sipping wine. 

"The troll sent me", you say remembering 
your war years. You immediately stand at 
attention.

"At ease," says Hera. "Do you know why we 
burnt down the inn?"

You nod no.

"We had to steal a very important saphire 
from the bank in the town. The inn is owned 
by the same person who owns the bank. When 
the inn burnt, he diverted most of his men 
to salvage whatever they could from the inn. 
Quite useless, as greek fire burns through 
everything. And while the bank was 
unprotected we robbed it."

You nod yes, this makes sense.

"Your job now", she continued "is to 
transport the artifact to Revan himself.
The saphire was cursed by an ancient 
warlock from the old country to bring 
the cause of Revan's death. Now if I send 
you on such a mission then I need your 
trust. You need to take this saphire to 
Feca of Tiefling. He knows how to crush 
cursed stones into powder, and destroy them. 
You will be given 7000 gold pieces upon the
completion of this mission. 1350 now and 
the rest later. Pick it up from the armory."

You go to the armory and pick up the saphire 
and the gold.""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""You go to the armory and
pick up the saphire and the gold.""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Label(text=" ")
        fIghtbutton = Button(text="Next")
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def FIGHT(self, instance):
        if h.stealth >= 550:
            game.lvl2S2sces()
            game.screenmanager.current = "Level 2 Sneak 2 successful"
        else:
            game.level_2_s2fail()
            game.screenmanager.current = "Level 2 Sneak 2 fail"


class Level_2_Sneak_1_SCES(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl2_s1sces()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def lvl2_s1sces(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
You continue to sneak around the
outskirts of the camp. Soon you 
see another {h.race}. He goes to 
a nearby lake to swim and bathe. 
You quietly manage to steal his 
clothes and armor. You put your 
visor down so no one will 
recognise you.

You hear a voice. 
"Hey! You! give me back my armor." 
You turn around and you quickly 
attack with your{h.weapon} before 
he makes anymore noise. Even though 
he puts up a fight, he is no match 
for you. He dies quickly when you 
land a strong blow with your {h.weapon} 
on his head. You quickly tie his legs 
to a stone using a nearby vine. 
You pick up the body and throw it into 
the lake. The stone keeps the body 
from floating up.

You enter the camp without suspicion.
As you are walking through the camp 
a troll rushes up to you and says,
"Hey! You're just the {h.race} 
I am looking for! I know it's late 
but Hera needs to see you. She has a 
job for a {h.race}. She said you might 
get some extra gold if you do it. 
I can't take you there, I have to fetch 
her some more wine, but you know her 
tent don't you?"
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""What do you want to do?
Nod yes? OR Nod no?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Button(text="Nod Yes")
        fIghtbutton = Button(text="Nod No")
        sNeakbutton.bind(on_press=self.sneak)
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def sneak(self, instance):
        game.screenmanager.current = "Level 2 Sneak 2 Yes"

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 2 Sneak 2 No"


class Level_2_Sneak_1_FAIL(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl2_s1sces()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def lvl2_s1sces(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
You continue to sneak around the
outskirts of the camp. Soon you 
see another {h.race}. He goes to 
a nearby lake to swim and bathe. 
You quietly manage to steal his 
clothes and armor. You put your 
visor down so no one will 
recognise you.

You enter the camp without suspicion.
As you are walking through the camp 
a troll rushes up to you and says,
"Hey! You're just the {h.race} 
I am looking for! I know it's late 
but Hera needs to see you. She has a 
job for a {h.race}. She said you might 
get some extra gold if you do it. 
I can't take you there, I have to fetch 
her some more wine, but you know her 
tent don't you?"
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""What do you want to do?
Nod yes? OR Nod no?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Button(text="Nod Yes")
        fIghtbutton = Button(text="Nod No")
        sNeakbutton.bind(on_press=self.sneak)
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def sneak(self, instance):
        game.screenmanager.current = "Level 2 Sneak 2 Yes"

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 2 Sneak 2 No"


class Level_2_Fight_1_FAIL(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl2_f1f()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        grid.add_widget(Label(text=" "))
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def lvl2_f1f(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
Digusted by these men you attack the 
entire camp head on! You were in the 
war you can take on these lumps of 
clay. You catch the camp by surprise 
and kill all the guards who are awake. 
The rest still sleep. It is only you 
who was awake.


Or so you thought. 

Men awoke in the commotion and are 
charging at you for battle. You 
fight and give one last stand but 
ALAS great warrior. The enemies are 
too many, and your strength too little. 
As you continue to fight your enemies, 
someone stabs you in the back. Almost 
on cue you are cut in the stomach and 
the neck. You are then left for dead. 
You never were able to take revenge 
for what happened at the inn.

You slowly give in to the Eternal Slumber, 
the warrior spirit still fighting...
            GAME OVER
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp -= 100
        h.strength += 50
        h.stealth += 50
        self.add_widget(Label(text=f"""GAME OVER""", color=(0, 0, 0, 1), font_size=20))
        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Label(text="")
        fIghtbutton = Label(text="")
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)


class Level_2_Fight_1_NORM(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl2_f1n()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def lvl2_f1n(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
Digusted by these men you attack the 
entire camp head on! You were in the 
war you can take on these lumps of 
clay. You catch the camp by surprise 
and kill all the guards who are awake. 
The rest still sleep. It is only you 
who was awake.


Or so you thought. 

Men awoke in the commotion and are 
charging at you for battle. You fight 
and give one last stand. You fight 
left and right. A sort of blood lust 
takes over you. You take down tens or 
hundreds of men with their bodies piling
up around you. You take some deep cuts, 
but it is almost like the warrior 
goddess has blessed you. Soon enough 
the mercenaries are scared of facing 
you and they run away. You finally 
calm down enough to walk through the 
near deserted camp. You reach the armory
and find a saphire just carelessly sitting
there. It seems to call to you. You pick 
it up and decide to keep it. You leave the
camp soon after. You continue down the 
path to meet Feca in Tiefling. 

There are some things he must answer for...


""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp -= 100
        h.strength += 50
        h.stealth += 50
        h.artifact = True
        print(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
              h.weapon, h.artifact)
        self.add_widget(Label(text=f"""Move Onto the next screen""", color=(0, 0, 0, 1)))
        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Label(text="")
        fIghtbutton = Button(text="MOVE ON")
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 3 intro"


class Level_2_Fight_1_SCES(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl2_f1s()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def lvl2_f1s(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
Digusted by these men you attack the 
entire camp head on! You were in the 
war you can take on these lumps of 
clay. You catch the camp by surprise 
and kill all the guards who are awake. 
The rest still sleep. It is only you 
who was awake.


Or so you thought. 

Men awoke in the commotion and are 
charging at you for battle. You fight 
and give one last stand. You fight 
left and right. A sort of blood lust 
takes over you. You take down tens or 
hundreds of men with their bodies piling
up around you. You take some deep cuts, 
but it is almost like the warrior 
goddess has blessed you. This thought 
gives you more strength that anything. 
Soon enough the mercenaries are scared 
of facing you and they run away. You 
finally calm down enough to walk through
the near deserted camp. You reach the 
armory and find a saphire just carelessly 
sitting there. It seems to call to you. 
You pick it up and decide to keep it. 
You then leave the camp. You continue 
down the path to meet Feca in Tiefling. 

There are some things he must answer for...

""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp += 50
        h.strength += 75
        h.stealth += 75
        h.artifact = True
        print(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
              h.weapon, h.artifact)
        self.add_widget(Label(text=f"""Move Onto the next screen""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Label(text="")
        fIghtbutton = Button(text="MOVE ON")
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 3 intro"


class Level_2_INTRO(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):

        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl2_start()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        grid.add_widget(Label(text=" "))
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def lvl2_start(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
As you approach the camp you notice 
something curious. The men are happy 
and merry as if they just came back 
from battle victorious. You decide 
to get closer in the camp. As you 
sneak around in the camp you hear 
someone speak. You crouch down 
low lest you be found. 

"I don't believe those little idiots 
had a chance. No one could have survived 
that burning Dragontal Walk. Revan will 
be pleased when we bring him the bounty."

"Piss on that... I just want the gold I
was promised. But what sort of an oaf
names an inn 'Dragontail Walk'. The place
deserved to go down in ashes." 

After saying this the men leave. You 
breathe a little easy, but realize...
These are the same men who attacked you!
They walk away to a set of tents. 
Everyone seems to retire to their tents now. 
It seems that the camp is going to sleep...""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Do continue to sneak?
OR
Do you attack?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        jumpbutton = Button(text="Sneak")
        fightbutton = Button(text="Attack")
        jumpbutton.bind(on_press=self.JUMP)
        fightbutton.bind(on_press=self.FIGHT)
        choice.add_widget(jumpbutton)
        choice.add_widget(fightbutton)
        self.add_widget(choice)

    def JUMP(self, instance):
        if h.stealth >= 550:
            game.lvl2s1secs()
            game.screenmanager.current = "Level 2 Sneak 1 Successful"
        else:
            game.lvl2s1f()
            game.screenmanager.current = "Level 2 Sneak 1 Fail"

    def FIGHT(self, instance):
        if h.strength < 500:
            game.screenmanager.current = "Level 2 Fight 1 Fail"
        elif h.strength >= 500 and h.strength <= 550:
            game.lvl2F1norm()
            game.screenmanager.current = "Level 2 Fight 1 Normal"
        elif h.strength > 550:
            game.lvl2F1sces()
            game.screenmanager.current = "Level 2 Fight 1 Successful"


class Level_1_inn_fight_norm(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl1_ifn()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.lvl1fight()
        game.screenmanager.current = "Level 1 FIGHT"

    def lvl1_ifn(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
You jump out from behind the counter,
confronting the brute in front of you.
He proves to be a worthy adversary. 
You take quite a few hits from him, 
but eventually you get the upper hand
and manage to overpower him! As you 
walk out you find no other enemies 
outside. Looking back, you see the 
burning inn, listen to the cries of the
people still trapped inside. There is 
nothing you can do for them now. You 
catch your breath and continue down 
the road. 

This night is far from over…

You’re walking along the dark road,
thinking about what just happened. 
You look at your {h.weapon} more closely, 
and see something rather interesting,
a brand. You have seen this before.
Surely this is the symbol of the 
great blacksmith Feca of Tiefling. But
he doesn't just hand out his weapons 
to common mercenaries; no, there 
is more to this. The only person who
can tell you more about this is Feca 
himself. Looks like you’re going 
to Tiefling village.

On the way to Tiefling, you spot a small 
camp of mercenaries. They’re wearing the
same armor as the ones who attacked the 
inn. It’s not a company you recognize, 
could there be something more sinister 
at play here? 

""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp -= 50
        self.add_widget(Label(text=f"""Do you want to infiltrate the camp? 
Or do you want to move on 
to Tiefling village?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Button(text="INFILTRATE")
        fIghtbutton = Button(text="MOVE ON")
        sNeakbutton.bind(on_press=self.sneak)
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def sneak(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 3 intro"


class Level_1_inn_fight_fail(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl1_iff()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.lvl1fight()
        game.screenmanager.current = "Level 1 FIGHT"

    def lvl1_iff(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
You jump out from behind the counter, 
confronting the brute in front of you. 
A foolish decision! He quickly 
overpowers you and knocks you on 
the ground with his club. He stands 
over you, ready to finish you off when
suddenly a large burning beam falls on
him. You got lucky! But don’t count on
luck all the time. You manage to walk 
out, still reeling from the hit you 
took. As you walk out you find no other
enemies outside. Looking back, you see
the burning inn, listen to the cries of
the people still trapped inside. There 
is nothing you can do for them now. 
You catch your breath and continue 
down the road.

This night is far from over…

You’re walking along the dark road,
thinking about what just happened. 
You look at your {h.weapon} more closely, 
and see something rather interesting,
a brand. You have seen this before.
Surely this is the symbol of the 
great blacksmith Feca of Tiefling. But
he doesn't just hand out his weapons 
to common mercenaries; no, there 
is more to this. The only person who
can tell you more about this is Feca 
himself. Looks like you’re going 
to Tiefling village.

On the way to Tiefling, you spot a small 
camp of mercenaries. They’re wearing the
same armor as the ones who attacked the 
inn. It’s not a company you recognize, 
could there be something more sinister 
at play here? 

""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp -= 100
        self.add_widget(Label(text=f"""Do you want to infiltrate the camp? 
Or do you want to move on 
to Tiefling village?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Button(text="INFILTRATE")
        fIghtbutton = Button(text="MOVE ON")
        sNeakbutton.bind(on_press=self.sneak)
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def sneak(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 3 intro"


class Level_1_inn_fight_sces(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl1_ifs()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=4, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def back(self, instance):
        game.lvl1fight()
        game.screenmanager.current = "Level 1 FIGHT"

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def lvl1_ifs(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
You jump out from behind the 
counter, confronting the brute in 
front of you. He is no match for your 
skill and before long he lies 
defeated at your feet. As you walk 
out you find no other enemies outside. 
Looking back, you see the burning inn, 
listen to the cries of the people 
still trapped inside. There is nothing 
you can do for them now. You catch your 
breath and continue down the road.

This night is far from over…

You’re walking along the dark road,
thinking about what just happened. 
You look at your {h.weapon} more closely, 
and see something rather interesting,
a brand. You have seen this before.
Surely this is the symbol of the 
great blacksmith Feca of Tiefling. But
he doesn't just hand out his weapons 
to common mercenaries; no, there 
is more to this. The only person who
can tell you more about this is Feca 
himself. Looks like you’re going 
to Tiefling village.

On the way to Tiefling, you spot a small 
camp of mercenaries. They’re wearing the
same armor as the ones who attacked the 
inn. It’s not a company you recognize, 
could there be something more sinister 
at play here? 

""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""
Do you want to infiltrate the camp? 
Or do you want to move on 
to Tiefling village?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Button(text="INFILTRATE")
        fIghtbutton = Button(text="MOVE ON")
        sNeakbutton.bind(on_press=self.sneak)
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def sneak(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 3 intro"


class Level_1_inn_sneak_fail(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl1_isf()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def back(self, instance):
        game.lvl1fight()
        game.screenmanager.current = "Level 1 FIGHT"

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def lvl1_iss(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
The brute notices you sneaking around!
He approaches you and swings his club 
wildly, knocking you on the ground. 
He stands over you, ready to finish you 
off when suddenly a large burning beam 
falls on him. You got lucky! But don’t 
count on luck all the time. You manage
to walk out, still reeling from the 
hit you took. As you walk out you find
no other enemies outside. Looking back,
you see the burning inn, listen to the 
cries of the people still trapped 
inside. There is nothing you can do 
for them now. You catch your breath and
continue down the road.

This night is far from over…

You’re walking along the dark road,
thinking about what just happened. 
You look at your {h.weapon} more closely, 
and see something rather interesting,
a brand. You have seen this before.
Surely this is the symbol of the 
great blacksmith Feca of Tiefling. But
he doesn't just hand out his weapons 
to common mercenaries; no, there 
is more to this. The only person who
can tell you more about this is Feca 
himself. Looks like you’re going 
to Tiefling village.

On the way to Tiefling, you spot a small 
camp of mercenaries. They’re wearing the
same armor as the ones who attacked the 
inn. It’s not a company you recognize, 
could there be something more sinister 
at play here? 

""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp -= 50
        self.add_widget(Label(text=f"""Do you want to infiltrate the camp? 
Or do you want to move on 
to Tiefling village?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Button(text="INFILTRATE")
        fIghtbutton = Button(text="MOVE ON")
        sNeakbutton.bind(on_press=self.sneak)
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def sneak(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 3 intro"


class Level_1_inn_sneak_sces(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl1_iss()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=4, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def back(self, instance):
        game.lvl1fight()
        game.screenmanager.current = "Level 1 FIGHT"

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def lvl1_iss(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
You successfully sneak out from behind
him! As you walk out you find no other 
enemies outside. Looking back, you see 
the burning inn, listen to the cries 
of the people still trapped inside. 
There is nothing you can do for them 
now. You catch your breath and continue
down the road.

This night is far from over…

You’re walking along the dark road,
thinking about what just happened. 
You look at your {h.weapon} more closely, 
and see something rather interesting,
a brand. You have seen this before.
Surely this is the symbol of the 
great blacksmith Feca of Tiefling. But
he doesn't just hand out his weapons 
to common mercenaries; no, there 
is more to this. The only person who
can tell you more about this is Feca 
himself. Looks like you’re going 
to Tiefling village.

On the way to Tiefling, you spot a small 
camp of mercenaries. They’re wearing the
same armor as the ones who attacked the 
inn. It’s not a company you recognize, 
could there be something more sinister 
at play here? 

""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Do you want to infiltrate the camp? 
Or do you want to move on 
to Tiefling village?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Button(text="INFILTRATE")
        fIghtbutton = Button(text="MOVE ON")
        sNeakbutton.bind(on_press=self.sneak)
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def sneak(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 3 intro"


class Level_1_1_fight(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):

        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl1_1_Fight()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=4, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def back(self, instance):
        game.screenmanager.current = "Level 1 Intro Page"

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def lvl1_1_Fight(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
You grab the man’s {h.weapon},
and make your way downstairs, 
all while the whole building 
collapses around you. There 
are people trapped, people who
can’t defend themselves, but 
there’s no time to save them. 
A few men do try to attack you 
again but you make quick work 
of them. It’s not long before 
you find yourself right in front 
of the main door. Just as you're
about to leave, a huge brute jumps
walks in,blocking the exit. You 
quickly hide behind the counter, 
contemplating your next move…""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Do you fight him or try and sneak out?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Button(text="SNEAK OUT")
        fIghtbutton = Button(text="FIGHT")
        sNeakbutton.bind(on_press=self.sneak)
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def sneak(self, instance):
        if h.stealth >= 500:
            game.lvl1iss()
            game.screenmanager.current = "Level 1 inn sneak successful"
        else:
            game.l1_inn_sneak_fail()
            game.screenmanager.current = "Level 1 inn sneak fail"

    def FIGHT(self, instance):
        if h.strength >= 550:
            game.lvl1ifs()
            game.screenmanager.current = "Level 1 inn fight successful"
        elif h.strength >= 500 and h.strength < 500:
            game.l1_inn_fight_norm()
            game.screenmanager.current = "Level 1 inn fight normal"
        else:
            game.l1_inn_fight_fail()
            game.screenmanager.current = "Level 1 inn fight fail"


class Level_1_1_rjump(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl1_1_rjump()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=4, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def back(self, instance):
        game.screenmanager.current = "Level 1 Intro Page"

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def lvl1_1_rjump(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
You leap through the window, using
your wings to descend safely. 
Looking back, you see the burning 
inn, listen to the cries of the 
people still trapped inside. There
is nothing you can do for them now,
it’s way too dangerous to go back 
inside. You pick up a {h.weapon} 
form one of the corpses outside, 
catch your breath and continue 
down the road.

This night is far from over…

You’re walking along the dark road,
thinking about what just happened. 
You look at your {h.weapon} more closely, 
and see something rather interesting,
a brand. You have seen this before.
Surely this is the symbol of the 
great blacksmith Feca of Tiefling. But
he doesn't just hand out his weapons 
to common mercenaries; no, there 
is more to this. The only person who
can tell you more about this is Feca 
himself. Looks like you’re going 
to Tiefling village.

On the way to Tiefling, you spot a small 
camp of mercenaries. They’re wearing the
same armor as the ones who attacked the 
inn. It’s not a company you recognize, 
could there be something more sinister 
at play here? 

""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Do you want to infiltrate the camp? 
Or do you want to move on 
to Tiefling village?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Button(text="INFILTRATE")
        fIghtbutton = Button(text="MOVE ON")
        sNeakbutton.bind(on_press=self.sneak)
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def sneak(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 3 intro"


class Level_1_1_ejump(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl1_1_ejump()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=4, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        stop_music_button = Button(text="Stop Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        grid.add_widget(stop_music_button)
        stop_music_button.bind(on_press=self.stop_music)
        self.add_widget(grid)

    def stop_music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.stop()

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def back(self, instance):
        game.screenmanager.current = "Level 1 Intro Page"

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def lvl1_1_ejump(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
You leap through the window, using
your elevn agility to climb down 
safely. Looking back, you see the 
burning inn, listen to the cries 
of the people still trapped inside. 
There is nothing you can do for them
now, it’s way too dangerous to go 
back inside. You pick up a {h.weapon}
form one of the corpses outside, 
catch your breath and continue down
the road.

This night is far from over…

You’re walking along the dark road,
thinking about what just happened. 
You look at your {h.weapon} more 
closely, and see something rather 
interesting, a brand. You have 
seen this before. Surely this is 
the symbol of the great blacksmith
Feca of Tiefling.But he doesn't 
just hand out his weapons to 
common mercenaries, no there is
more to this.The only person who 
can tell you more about this is
Feca himself. Looks like you’re 
going to Tiefling village. On the 
way to Tiefling, you spot a small
camp of mercenaries. They’re 
wearing the same armor as the ones
who attacked the inn. It’s not a 
company you recognize, could there
be something more sinister at play 
here? 
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)

        self.add_widget(Label(text=f"""Do you want to infiltrate the camp? 
Or do you want to move on 
to Tiefling village?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Button(text="INFILTRATE")
        fIghtbutton = Button(text="MOVE ON")
        sNeakbutton.bind(on_press=self.sneak)
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def sneak(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 3 intro"


class Level_1_1_hjump(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.lvl1_1_hjump()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=4, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        stop_music_button = Button(text="Stop Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def back(self, instance):
        game.screenmanager.current = "Level 1 Intro Page"

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def lvl1_1_hjump(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
You leap through the window, but 
don’t quite stick the landing. 
You’re hurt and you know it, but 
you also know it isn’t safe to 
stick around here. You manage 
to get up on your feet and look
back at the burning inn, listening 
to the cries of the people still 
trapped inside. There is nothing
you can do for them now, it’s 
way too dangerous to go back 
inside. You pick up a {h.weapon}
form one of the corpses outside, 
catch your breath and continue 
down the road.

This night is far from over…

You’re walking along the dark 
road, thinking about what just
happened. You look at your 
{h.weapon} more closely, and 
see something rather interesting, 
a brand. You have seen this before.
Surely this is the symbol of the 
great blacksmith Feca of Tiefling.
But he doesn't just hand out his
weapons to common mercenaries, 
no there is more to this. The 
only person who can tell you 
more about this is Feca himself. 
Looks like you’re going to Tiefling 
village. On the way to Tiefling, 
you spot a small camp of mercenaries. 
They’re wearing the same armor as 
the ones who attacked the inn.
It’s not a company you recognize, 
could there be something more 
sinister at play here? 
""", color=(0, 0, 0, 1), size_hint=(1, None), pos=(self.width, 400))
        frame.add_widget(texta)
        scroll.add_widget(frame)
        self.add_widget(scroll)
        h.hp -= 100
        print(h.hp)
        self.add_widget(Label(text=f"""Do you want to infiltrate the camp? 
Or do you want to move on 
to Tiefling village?""", color=(0, 0, 0, 1)))

        choice = GridLayout(cols=2, rows=1)
        sNeakbutton = Button(text="INFILTRATE")
        fIghtbutton = Button(text="MOVE ON")
        sNeakbutton.bind(on_press=self.sneak)
        fIghtbutton.bind(on_press=self.FIGHT)
        choice.add_widget(sNeakbutton)
        choice.add_widget(fIghtbutton)
        self.add_widget(choice)

    def sneak(self, instance):
        game.screenmanager.current = "Level 2 intro"

    def FIGHT(self, instance):
        game.screenmanager.current = "Level 3 intro"


class Level_1_intro_page(character, BoxLayout):
    _disabled_count = 0

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):

        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        print(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name, h.weapon, h.artifact)

        self.orientation = "vertical"

        self.lvl1_1_start()
        self.bottom_bar()

    def bottom_bar(self):
        grid = GridLayout(cols=3, rows=1, padding=5, spacing=10)
        homescreen_button = Button(text="Home")
        music_button = Button(text="Music")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        grid.add_widget(music_button)
        music_button.bind(on_press=self.music)
        self.add_widget(grid)

    def music(self, instance):
        sound = SoundLoader.load(
            'extra files for mini project\VIKING music -Epic Action Background Music No Copyright.wav')
        sound.play()

    def back(self, instance):
        game.screenmanager.current = "User Input"

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def lvl1_1_start(self):
        frame = GridLayout(cols=1, rows=1, size_hint_y=None)
        frame.bind(minimum_height=frame.setter('height'))
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, size_hint=(1, None), scroll_y=(1),
                            size=(Window.width, Window.height * (1 / 3)))
        texta = Label(text=f"""
After returning from {h.home} you 
thought the worst was behind you.

The war was over,
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
        fightbutton.bind(on_press=self.FIGHT)
        choice.add_widget(jumpbutton)
        choice.add_widget(fightbutton)
        self.add_widget(choice)

    def JUMP(self, instance):
        if h.race == "Rito":
            game.lvl1rjump()
            game.screenmanager.current = "Level 1 JUMP Rito"
        elif h.race == "Elf":
            game.lvl1ejump()
            game.screenmanager.current = "Level 1 JUMP Elf"
        else:
            game.l1_jump_hurt()
            game.screenmanager.current = "Level 1 JUMP Hurt"

    def FIGHT(self, instance):
        game.lvl1fight()
        game.screenmanager.current = "Level 1 FIGHT"


class User_input_page(character, BoxLayout):
    _disabled_count = 0
    global h
    n = "name"

    def __init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense, **kwargs):
        character.__init__(self, race, hp, stealth, strength, charisma, home, name, weapon, artifact, defense)
        BoxLayout.__init__(self, **kwargs)

        self.orientation = "vertical"

        self.userInput()

    def userInput(self):
        self.add_widget(Label(text=f"""Welcome Player! What is your name?""", color=(0, 0, 0, 1)))
        self.nameinput = TextInput(multiline=False)
        self.add_widget(self.nameinput)
        self.add_widget(Label(text=f"""Choose a race for your character from below""", color=(0, 0, 0, 1)))
        self.Race_Input()
        self.add_widget(Label(text=f"""Choose a weapon for your character from below""", color=(0, 0, 0, 1)))
        self.Weapon_Input()
        story_button = Button(text="Go to story")
        story_button.bind(on_press=self.story)
        self.add_widget(story_button)

    def Race_Input(self):
        race = GridLayout(cols=4, rows=1, padding=10, spacing=10)
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

    def Weapon_Input(self):
        Weapon = GridLayout(cols=3, rows=1, padding=10, spacing=10)
        sword = Button(text="Sword")
        axe = Button(text="AXE")
        mace = Button(text="MACE")
        sword.bind(on_press=self.sworD)
        axe.bind(on_press=self.axE)
        mace.bind(on_press=self.macE)
        Weapon.add_widget(sword)
        Weapon.add_widget(axe)
        Weapon.add_widget(mace)
        self.add_widget(Weapon)

    def ritO(self, instance):
        h.race = 'Rito'
        h.hp = 500.0
        h.stealth = 550.0
        h.strength = 500.0
        h.charisma = False
        h.home = 'High Rock'

    def elF(self, instance):
        h.race = 'Elf'
        h.hp = 600.0
        h.stealth = 600.0
        h.strength = 450.0
        h.charisma = True
        h.home = 'Valenwood'

    def humaN(self, instance):
        h.race = 'Human'
        h.hp = 500.0
        h.stealth = 500.0
        h.strength = 550.0
        h.charisma = True
        h.home = 'Cyrodill'

    def dwarF(self, instance):
        h.race = 'Dwarf'
        h.hp = 600.0
        h.stealth = 450.0
        h.strength = 600.0
        h.charisma = False
        h.home = 'Moria'

    def sworD(self, instance):
        h.weapon = 'sword'

    def axE(self, instance):
        h.weapon = 'axe'

    def macE(self, instance):
        h.weapon = 'mace'

    def story(self, instance):
        h.name = self.nameinput.text
        game.l1_intro()
        game.screenmanager.current = "Level 1 Intro Page"


class HUMAN_CD_Screen(BoxLayout):
    def __init__(self, **kwargs):
        super(HUMAN_CD_Screen, self).__init__(**kwargs)

        self.orientation = "vertical"

        self.homescreen()

    def homescreen(self):
        display = Label(text=f"""
Humans are one of the most charismatic 
races from Cyrodill. Humans are often 
underestimated by the other races as they 
aren’t the strongest, nor the most stealthy. 
But the humans are crafty and flexible to
any given situation. Humans are known for their
cunning and clever ways to get out of any 
situation. However, they are very much capable 
of battle and war where it may be needed.""", color=(0, 0, 0, 1), font_size=17)
        self.add_widget(display)
        pic = Image(source='extra files for mini project\human.png')
        self.add_widget(pic)
        self.grid()

    def grid(self):
        grid = GridLayout(cols=2, rows=1, padding=10, spacing=10)
        homescreen_button = Button(text="Home")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        self.add_widget(grid)

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Character Description"


class RITO_CD_Screen(BoxLayout):
    def __init__(self, **kwargs):
        super(RITO_CD_Screen, self).__init__(**kwargs)

        self.orientation = "vertical"

        self.homescreen()

    def homescreen(self):
        display = Label(text=f"""
The rito are a strong race. They have the 
body of a human with wings, but they have 
the head of a bird. They are covered in 
feathers. Rito are predominantly situated 
in the mountains of High Rock, which is 
easy for them considering they can scale 
any mountain via flight. The rito are known 
for their aerial archers and their strength,
the way humans are known for their charisma 
and versatility.    """, color=(0, 0, 0, 1), font_size=17)
        self.add_widget(display)
        pic = Image(source='extra files for mini project\hrito.png')
        self.add_widget(pic)
        self.grid()

    def grid(self):
        grid = GridLayout(cols=2, rows=1, padding=10, spacing=10)
        homescreen_button = Button(text="Home")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        self.add_widget(grid)

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Character Description"


class DWARF_CD_Screen(BoxLayout):
    def __init__(self, **kwargs):
        super(DWARF_CD_Screen, self).__init__(**kwargs)

        self.orientation = "vertical"

        self.homescreen()

    def homescreen(self):
        display = Label(text=f"""
The dwarf is a simple creature. They are
smart and hardy, but loud and obnoxious. 
What they lack in stealth, they more than 
make up for in strength. It is said that 
an army of dwarfs has never lost a battle, 
no matter the odds. The dwarfs are 
predominantly from the mines of Moria and,
and are well-versed in explosives and jewels.
""", color=(0, 0, 0, 1), font_size=17)
        self.add_widget(display)
        pic = Image(source='extra files for mini project\dwarf.png')
        self.add_widget(pic)
        self.grid()

    def grid(self):
        grid = GridLayout(cols=2, rows=1, padding=10, spacing=10)
        homescreen_button = Button(text="Home")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        self.add_widget(grid)

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Character Description"


class ELF_CD_Screen(BoxLayout):
    def __init__(self, **kwargs):
        super(ELF_CD_Screen, self).__init__(**kwargs)

        self.orientation = "vertical"

        self.homescreen()

    def homescreen(self):
        display = Label(text=f"""
Elves are the smartest of the four races.
It is said that their home Valenwood used be 
filled with jungle predators. It is there 
that elves learnt the skill of stealth, and
used their higher intelligence to convert 
Valenwood's jungles into a kingdom of 
prosperity and haven for learning. Elves 
may be small, but they aren’t weak. It is
a matter of pride for an elf to be able 
to get out of any situation. Their stealth 
enables them to evade and dodge any form of 
war that comes their way.
""", color=(0, 0, 0, 1), font_size=12)
        self.add_widget(display)
        pic = Image(source='extra files for mini project\elf.png')
        self.add_widget(pic)
        self.grid()

    def grid(self):
        grid = GridLayout(cols=2, rows=1, padding=10, spacing=10)
        homescreen_button = Button(text="Home")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        self.add_widget(grid)

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Character Description"


class CD_Screen(BoxLayout):
    def __init__(self, **kwargs):
        super(CD_Screen, self).__init__(**kwargs)

        self.orientation = "vertical"

        self.CDscreen()

    def CDscreen(self):
        cd = GridLayout(cols=2, rows=2, padding=10, spacing=10)
        ritocdbtn = Button(text="Rito", size_hint=(.3, .3), pos_hint={"x": 0.35, "y": 0.3})
        ritocdbtn.bind(on_press=self.ritocdfunc)
        elfcdbtn = Button(text="Elf", size_hint=(.3, .3),
                          pos_hint={"x": 0.35, "y": 0.3})
        elfcdbtn.bind(on_press=self.elfcdfunc)
        dwarfcdbtn = Button(text="Dwarf", size_hint=(.3, .3),
                            pos_hint={"x": 0.35, "y": 0.3})
        dwarfcdbtn.bind(on_press=self.dwarfcdfunc)
        humancdbtn = Button(text="Human", size_hint=(.3, .3),
                            pos_hint={"x": 0.35, "y": 0.3})
        humancdbtn.bind(on_press=self.humancdfunc)
        cd.add_widget(ritocdbtn)
        cd.add_widget(elfcdbtn)
        cd.add_widget(humancdbtn)
        cd.add_widget(dwarfcdbtn)
        self.add_widget(cd)

    def ritocdfunc(self, instance):
        game.screenmanager.current = "RITO CD"

    def elfcdfunc(self, instance):
        game.screenmanager.current = "ELF CD"

    def dwarfcdfunc(self, instance):
        game.screenmanager.current = "DWARF CD"

    def humancdfunc(self, instance):
        game.screenmanager.current = "HUMAN CD"


class Help(BoxLayout):
    def __init__(self, **kwargs):
        super(Help, self).__init__(**kwargs)

        self.orientation = "vertical"

        self.homescreen()

    def homescreen(self):
        display = Label(text=f"""
Welcome to the Dragontale Quest. 
This is a choose your own adventure,
which means that you are in command
of your character's adventure. Upon 
starting the game you will be asked
to choose a race for your character.
Choose wisely as certain races hold
a higher advantage in some situations
than others. You can learn about the 
differnt races from the character 
descriptions given in the previous 
screen. Along with choosing a race,
you will be asked to give yourself a
name and choose a weapon. There are
different weapons available and you
may choose according to your liking.


We hope you enjoy the game!""", color=(0, 0, 0, 1), font_size=12)
        self.add_widget(display)
        self.grid()

    def grid(self):
        grid = GridLayout(cols=2, rows=1, padding=10, spacing=10)
        homescreen_button = Button(text="Home")
        back_button = Button(text="Back")
        grid.add_widget(back_button)
        back_button.bind(on_press=self.back)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        self.add_widget(grid)

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def back(self, instance):
        game.screenmanager.current = "Help Screen"


class Help_Screen(BoxLayout):
    def __init__(self, **kwargs):
        super(Help_Screen, self).__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 100
        self.spacing = 25
        self.helpScreenDisplay()

    def helpScreenDisplay(self):
        Helpbutton = Button(text="Help")
        Helpbutton.bind(on_press=self.help)
        self.add_widget(Helpbutton)
        CDbutton = Button(text="Character Description")
        CDbutton.bind(on_press=self.chardesc)
        self.add_widget(CDbutton)

    def help(self, instance):
        game.screenmanager.current = "HELP"

    def chardesc(self, instance):
        game.screenmanager.current = "Character Description"


class Home_page(BoxLayout):
    def __init__(self, **kwargs):
        super(Home_page, self).__init__(**kwargs)

        self.orientation = "vertical"

        self.homescreen()

    def homescreen(self):
        titledisplay = Label(text=f"""Dragon Tale Quest""", color=(0, 0, 0, 1), font_size=32)
        self.add_widget(titledisplay)
        subtitledisplay = Label(text=f"""A Choose your Own adventure Story""", color=(0, 0, 0, 1), font_size=20)
        pic = Image(source='extra files for mini project\homescreen image.png')
        self.add_widget(pic)
        self.add_widget(subtitledisplay)
        self.grid()

    def grid(self):
        grid = GridLayout(cols=3, rows=1, padding=10, spacing=10)
        homescreen_button = Button(text="Home")
        playGame_button = Button(text="Start")
        help_button = Button(text=f"""Help""")
        grid.add_widget(help_button)
        help_button.bind(on_press=self.help_screen)
        grid.add_widget(playGame_button)
        playGame_button.bind(on_press=self.game)
        grid.add_widget(homescreen_button)
        homescreen_button.bind(on_press=self.Homescreen)
        self.add_widget(grid)

    def help_screen(self, instance):
        game.screenmanager.current = "Help Screen"

    def Homescreen(self, instance):
        game.screenmanager.current = "Home"

    def game(self, instance):
        game.screenmanager.current = "User Input"


class cyoaApp(App):
    def build(self):
        self.screenmanager = ScreenManager()

        self.home_page = Home_page()
        screen = Screen(name="Home")
        screen.add_widget(self.home_page)
        self.screenmanager.add_widget(screen)

        self.help_screen = Help_Screen()
        screen0 = Screen(name="Help Screen")
        screen0.add_widget(self.help_screen)
        self.screenmanager.add_widget(screen0)

        self.cd_screen = CD_Screen()
        screen0cd = Screen(name="Character Description")
        screen0cd.add_widget(self.cd_screen)
        self.screenmanager.add_widget(screen0cd)

        self.ritocd_screen = RITO_CD_Screen()
        screen0rcd = Screen(name="RITO CD")
        screen0rcd.add_widget(self.ritocd_screen)
        self.screenmanager.add_widget(screen0rcd)

        self.dwarfcd_screen = DWARF_CD_Screen()
        screen0dcd = Screen(name="DWARF CD")
        screen0dcd.add_widget(self.dwarfcd_screen)
        self.screenmanager.add_widget(screen0dcd)

        self.elfcd_screen = ELF_CD_Screen()
        screen0ecd = Screen(name="ELF CD")
        screen0ecd.add_widget(self.elfcd_screen)
        self.screenmanager.add_widget(screen0ecd)

        self.humancd_screen = HUMAN_CD_Screen()
        screen0hcd = Screen(name="HUMAN CD")
        screen0hcd.add_widget(self.humancd_screen)
        self.screenmanager.add_widget(screen0hcd)

        self.help_screen = Help()
        screen0h = Screen(name="HELP")
        screen0h.add_widget(self.help_screen)
        self.screenmanager.add_widget(screen0h)

        self.user_input_page = User_input_page(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                               h.weapon, h.artifact, h.defense)
        screen = Screen(name="User Input")
        screen.add_widget(self.user_input_page)
        self.screenmanager.add_widget(screen)

        self.level_1_1_rjump = Level_1_1_rjump(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                               h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 1 JUMP Rito")
        screen.add_widget(self.level_1_1_rjump)
        self.screenmanager.add_widget(screen)

        self.level_1_1_ejump = Level_1_1_ejump(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                               h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 1 JUMP Elf")
        screen.add_widget(self.level_1_1_ejump)
        self.screenmanager.add_widget(screen)

        self.level_1_1_fight = Level_1_1_fight(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                               h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 1 FIGHT")
        screen.add_widget(self.level_1_1_fight)
        self.screenmanager.add_widget(screen)

        self.level_1_innfs = Level_1_inn_fight_sces(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                    h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 1 inn fight successful")
        screen.add_widget(self.level_1_innfs)
        self.screenmanager.add_widget(screen)

        self.level_1_innss = Level_1_inn_sneak_sces(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                    h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 1 inn sneak successful")
        screen.add_widget(self.level_1_innss)
        self.screenmanager.add_widget(screen)

        self.level_2_intro = Level_2_INTRO(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                           h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 2 intro")
        screen.add_widget(self.level_2_intro)
        self.screenmanager.add_widget(screen)

        self.level_2_s1sces = Level_2_Sneak_1_SCES(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                   h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 2 Sneak 1 Successful")
        screen.add_widget(self.level_2_s1sces)
        self.screenmanager.add_widget(screen)

        self.level_2_s1fail = Level_2_Sneak_1_FAIL(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                   h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 2 Sneak 1 Fail")
        screen.add_widget(self.level_2_s1fail)
        self.screenmanager.add_widget(screen)

        self.level_2_f1fail = Level_2_Fight_1_FAIL(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                   h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 2 Fight 1 Fail")
        screen.add_widget(self.level_2_f1fail)
        self.screenmanager.add_widget(screen)

        self.level_2_s2yes = Level_2_Sneak_2_Yes(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                 h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 2 Sneak 2 Yes")
        screen.add_widget(self.level_2_s2yes)
        self.screenmanager.add_widget(screen)

        self.level_2_s2no = Level_2_Sneak_2_No(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                               h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 2 Sneak 2 No")
        screen.add_widget(self.level_2_s2no)
        self.screenmanager.add_widget(screen)

        self.level_2_s2fyd = Level_2_final_yes_d(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                 h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 2 final Yes dwarf")
        screen.add_widget(self.level_2_s2fyd)
        self.screenmanager.add_widget(screen)

        self.level_2_s2fn = Level_2_final_no(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                             h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 2 final No")
        screen.add_widget(self.level_2_s2fn)
        self.screenmanager.add_widget(screen)

        self.level_3_intro_page = Level_3_intro_page(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                     h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 3 intro")
        screen.add_widget(self.level_3_intro_page)
        self.screenmanager.add_widget(screen)

        self.level_3_friendly_charisma = Level_3_friendly_charisma(h.race, h.hp, h.stealth, h.strength, h.charisma,
                                                                   h.home, h.name,
                                                                   h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 3 friendly charisma")
        screen.add_widget(self.level_3_friendly_charisma)
        self.screenmanager.add_widget(screen)

        self.level_3_aggressive_yes = Level_3_aggressive_yes(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                                             h.name,
                                                             h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 3 aggressive yes")
        screen.add_widget(self.level_3_aggressive_yes)
        self.screenmanager.add_widget(screen)

        self.level_3_aggressive_no = Level_3_aggressive_no(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                                           h.name,
                                                           h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 3 aggressive no")
        screen.add_widget(self.level_3_aggressive_no)
        self.screenmanager.add_widget(screen)

        self.level_3_friendly_no_charisma = Level_3_friendly_no_charisma(h.race, h.hp, h.stealth, h.strength,
                                                                         h.charisma, h.home, h.name,
                                                                         h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 3 friendly no charisma")
        screen.add_widget(self.level_3_friendly_no_charisma)
        self.screenmanager.add_widget(screen)

        self.level_3_caught = Level_3_caught(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                             h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 3 caught")
        screen.add_widget(self.level_3_caught)
        self.screenmanager.add_widget(screen)

        self.level_3_tactical = Level_3_tactical(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                 h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 3 tactical")
        screen.add_widget(self.level_3_tactical)
        self.screenmanager.add_widget(screen)

        self.level_3_attack_death = Level_3_attack_death(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                                         h.name,
                                                         h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 3 attack death")
        screen.add_widget(self.level_3_attack_death)
        self.screenmanager.add_widget(screen)

        self.level_3_tactical_death = Level_3_tactical_death(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                                             h.name,
                                                             h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 3 tactical death")
        screen.add_widget(self.level_3_tactical_death)
        self.screenmanager.add_widget(screen)

        self.level_4_intro_page = Level_4_intro_page(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                     h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 4 Intro")
        screen.add_widget(self.level_4_intro_page)
        self.screenmanager.add_widget(screen)

        self.level_4_fort_attack = Level_4_fort_attack(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                       h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 4 fort attack")
        screen.add_widget(self.level_4_fort_attack)
        self.screenmanager.add_widget(screen)

        self.level_4_sane = Level_4_sane(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                         h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 4 sane")
        screen.add_widget(self.level_4_sane)
        self.screenmanager.add_widget(screen)

        self.level_4_lone = Level_4_lone(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                         h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 4 lone")
        screen.add_widget(self.level_4_lone)
        self.screenmanager.add_widget(screen)

        self.level_4_help = Level_4_help(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                         h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 4 help")
        screen.add_widget(self.level_4_help)
        self.screenmanager.add_widget(screen)

        self.level_4_safehouse = Level_4_safehouse(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                   h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 4 safehouse")
        screen.add_widget(self.level_4_safehouse)
        self.screenmanager.add_widget(screen)

        self.level_4_Dwarf = Level_4_Dwarf(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                           h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 4 Dwarf")
        screen.add_widget(self.level_4_Dwarf)
        self.screenmanager.add_widget(screen)

        self.level_4_No_Dwarf = Level_4_No_Dwarf(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                 h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 4 No Dwarf")
        screen.add_widget(self.level_4_No_Dwarf)
        self.screenmanager.add_widget(screen)

        self.level_4_disappear = Level_4_disappear(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                   h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 4 disappear")
        screen.add_widget(self.level_4_disappear)
        self.screenmanager.add_widget(screen)

        self.level_4_no_disappear = Level_4_no_disappear(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                                         h.name,
                                                         h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 4 safehouse")
        screen.add_widget(self.level_4_no_disappear)
        self.screenmanager.add_widget(screen)

        self.level_4_Dwarf_escape = Level_4_Dwarf_escape(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                                         h.name,
                                                         h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 4 Dwarf escape")
        screen.add_widget(self.level_4_Dwarf_escape)
        self.screenmanager.add_widget(screen)

        self.level_5_gw = Level_5_group_warlock(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                                h.name, h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 5 group outside warlock")
        screen.add_widget(self.level_5_gw)
        self.screenmanager.add_widget(screen)

        self.level_5_gout = Level_5_group_outside(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                                  h.name, h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 5 group outside")
        screen.add_widget(self.level_5_gout)
        self.screenmanager.add_widget(screen)

        self.level_5_gko = Level_5_group_Game_over(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                                   h.name, h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 5 group game over")
        screen.add_widget(self.level_5_gko)
        self.screenmanager.add_widget(screen)

        self.level_5_solo = Level_5_solo(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                         h.name, h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 5 solo")
        screen.add_widget(self.level_5_solo)
        self.screenmanager.add_widget(screen)

        self.level_5_soloh = Level_5_solo_human(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                                h.name, h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 5 solo Human")
        screen.add_widget(self.level_5_soloh)
        self.screenmanager.add_widget(screen)

        self.level_5_sko = Level_5_solo_Game_over(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                                  h.name, h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 5 solo Game Over")
        screen.add_widget(self.level_5_sko)
        self.screenmanager.add_widget(screen)

        self.level_5_fe = Level_5_fort_escape(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                              h.name, h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 5 fort escape safe")
        screen.add_widget(self.level_5_fe)
        self.screenmanager.add_widget(screen)

        self.level_5_dd = Level_5_Duel_Decline(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                               h.name, h.weapon, h.artifact, h.defense)
        screen = Screen(name="level 5 duel decline")
        screen.add_widget(self.level_5_dd)
        self.screenmanager.add_widget(screen)

        self.level_5_da = Level_5_Duel_Accept(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                              h.name, h.weapon, h.artifact, h.defense)
        screen = Screen(name="level 5 duel accept")
        screen.add_widget(self.level_5_da)
        self.screenmanager.add_widget(screen)

        self.level_6_intro_page = Level_6_intro_page(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                     h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 6 Intro")
        screen.add_widget(self.level_6_intro_page)
        self.screenmanager.add_widget(screen)

        self.level_6_Rito = Level_6_Rito(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name, h.weapon,
                                         h.artifact, h.defense)
        screen = Screen(name="Level 6 Rito")
        screen.add_widget(self.level_6_Rito)
        self.screenmanager.add_widget(screen)

        self.level_6_climb = Level_6_climb(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name, h.weapon,
                                           h.artifact, h.defense)
        screen = Screen(name="Level 6 climb")
        screen.add_widget(self.level_6_climb)
        self.screenmanager.add_widget(screen)

        self.level_6_no = Level_6_no(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name, h.weapon,
                                     h.artifact, h.defense)
        screen = Screen(name="Level 6 no offering")
        screen.add_widget(self.level_6_no)
        self.screenmanager.add_widget(screen)

        self.level_7_intro = Level_7_intro_page(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 7 Intro")
        screen.add_widget(self.level_7_intro)
        self.screenmanager.add_widget(screen)

        self.level_7_yes_drink = Level_7_yes_drink(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                   h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 7 yes drink")
        screen.add_widget(self.level_7_yes_drink)
        self.screenmanager.add_widget(screen)

        self.level_7_no_drink = Level_7_no_drink(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                 h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 7 no drink")
        screen.add_widget(self.level_7_no_drink)
        self.screenmanager.add_widget(screen)

        self.level_7_attack = Level_7_attack(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name, h.weapon,
                                             h.artifact, h.defense)
        screen = Screen(name="Level 7 attack")
        screen.add_widget(self.level_7_attack)
        self.screenmanager.add_widget(screen)

        self.level_7_attack_no = Level_7_attack_no(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                   h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 7 no attack")
        screen.add_widget(self.level_7_attack_no)
        self.screenmanager.add_widget(screen)

        self.level_7_sneak = Level_7_sneak(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name, h.weapon,
                                           h.artifact, h.defense)
        screen = Screen(name="Level 7 sneak")
        screen.add_widget(self.level_7_sneak)
        self.screenmanager.add_widget(screen)

        self.level_7_sneak_no = Level_7_sneak_no(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                 h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 7 no sneak")
        screen.add_widget(self.level_7_sneak_no)
        self.screenmanager.add_widget(screen)

        self.level_7_courtyard = Level_7_courtyard(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                   h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 7 courtyard")
        screen.add_widget(self.level_7_courtyard)
        self.screenmanager.add_widget(screen)

        self.level_7_attack_0 = Level_7_attack_0(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                 h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 7 attack 0")
        screen.add_widget(self.level_7_attack_0)
        self.screenmanager.add_widget(screen)

        self.level_7_attack_1 = Level_7_attack_1(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                 h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 7 attack 1")
        screen.add_widget(self.level_7_attack_1)
        self.screenmanager.add_widget(screen)

        self.level_7_defend_0 = Level_7_defend_0(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                 h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 7 defend 0")
        screen.add_widget(self.level_7_defend_0)
        self.screenmanager.add_widget(screen)

        self.level_7_defend_1 = Level_7_defend_1(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                 h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 7 defend 1")
        screen.add_widget(self.level_7_defend_1)
        self.screenmanager.add_widget(screen)

        self.level_7_defend_2 = Level_7_defend_2(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                 h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 7 defend 2")
        screen.add_widget(self.level_7_defend_2)
        self.screenmanager.add_widget(screen)

        self.level_7_defend_3 = Level_7_defend_3(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                 h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 7 defend 3")
        screen.add_widget(self.level_7_defend_3)
        self.screenmanager.add_widget(screen)

        self.level_7_defend_4 = Level_7_defend_4(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                 h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 7 defend 4")
        screen.add_widget(self.level_7_defend_4)
        self.screenmanager.add_widget(screen)

        self.level_7_death = Level_7_death(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name, h.weapon,
                                           h.artifact, h.defense)
        screen = Screen(name="Level 7 death")
        screen.add_widget(self.level_7_death)
        self.screenmanager.add_widget(screen)

        self.level_7_artifact_attack = Level_7_artifact_attack(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                                               h.name, h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 7 artifact attack")
        screen.add_widget(self.level_7_artifact_attack)
        self.screenmanager.add_widget(screen)

        return self.screenmanager

    def l1_intro(self):
        self.level_1_intro = Level_1_intro_page(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 1 Intro Page")
        screen.add_widget(self.level_1_intro)
        self.screenmanager.add_widget(screen)

    def l1_jump_hurt(self):
        self.level_1_1_hjump = Level_1_1_hjump(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                               h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 1 JUMP Hurt")
        screen.add_widget(self.level_1_1_hjump)
        self.screenmanager.add_widget(screen)

    def l1_inn_fight_norm(self):
        self.level_1_innfn = Level_1_inn_fight_norm(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                    h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 1 inn fight normal")
        screen.add_widget(self.level_1_innfn)
        self.screenmanager.add_widget(screen)

    def l1_inn_fight_fail(self):
        self.level_1_innff = Level_1_inn_fight_fail(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                    h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 1 inn fight fail")
        screen.add_widget(self.level_1_innff)
        self.screenmanager.add_widget(screen)

    def l1_inn_sneak_fail(self):
        self.level_1_innsf = Level_1_inn_sneak_fail(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                    h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 1 inn sneak fail")
        screen.add_widget(self.level_1_innsf)
        self.screenmanager.add_widget(screen)

    def lvl2F1norm(self):
        self.level_2_f1norm = Level_2_Fight_1_NORM(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                   h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 2 Fight 1 Normal")
        screen.add_widget(self.level_2_f1norm)
        self.screenmanager.add_widget(screen)

    def lvl2F1sces(self):
        self.level_2_f1sces = Level_2_Fight_1_SCES(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                   h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 2 Fight 1 Successful")
        screen.add_widget(self.level_2_f1sces)
        self.screenmanager.add_widget(screen)

    def lvl2S2fail(self):
        self.level_2_s2fail = Level_2_Sneak_2_FAIL(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                   h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 2 Sneak 2 fail")
        screen.add_widget(self.level_2_s2fail)
        self.screenmanager.add_widget(screen)

    def lvl2S2sces(self):
        self.level_2_s2sces = Level_2_Sneak_2_SCES(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                   h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 2 Sneak 2 successful")
        screen.add_widget(self.level_2_s2sces)
        self.screenmanager.add_widget(screen)

    def lvl2S2finalyesnd(self):
        self.level_2_s2fynd = Level_2_final_yes(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                                h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 2 final Yes")
        screen.add_widget(self.level_2_s2fynd)
        self.screenmanager.add_widget(screen)

    def lvl3attack(self):
        self.level_3_attack = Level_3_attack(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                             h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 3 attack")
        screen.add_widget(self.level_3_attack)
        self.screenmanager.add_widget(screen)

    def lvl4Help(self):
        self.level_4_help = Level_4_help(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home, h.name,
                                         h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 4 help")
        screen.add_widget(self.level_4_help)
        self.screenmanager.add_widget(screen)

    def lvl5OWnoArtifact(self):
        self.level_5_gw = Level_5_group_warlock_na(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                                   h.name, h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 5 group outside no artifact")
        screen.add_widget(self.level_5_gw)
        self.screenmanager.add_widget(screen)

    def lvl5groupinside(self):
        self.level_5_gi = Level_5_group_inside(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                               h.name, h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 5 group fight inside")
        screen.add_widget(self.level_5_gi)
        self.screenmanager.add_widget(screen)

    def lvl5soloNH(self):
        self.level_5_gi = Level_5_solo_not_human(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                                 h.name, h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 5 solo Not Human")
        screen.add_widget(self.level_5_gi)
        self.screenmanager.add_widget(screen)

    def lvl5fortescape(self):
        self.level_5_fed = Level_5_fort_escape_damage(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                                      h.name, h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 5 fort escape damaged")
        screen.add_widget(self.level_5_gi)
        self.screenmanager.add_widget(screen)

    def lvl6offering(self):
        self.level_6_yes = Level_6_yes(h.race, h.hp, h.stealth, h.strength, h.charisma, h.home,
                                       h.name, h.weapon, h.artifact, h.defense)
        screen = Screen(name="Level 6 offering")
        screen.add_widget(self.level_6_yes)
        self.screenmanager.add_widget(screen)


if __name__ == "__main__":
    game = cyoaApp()
    game.run()
