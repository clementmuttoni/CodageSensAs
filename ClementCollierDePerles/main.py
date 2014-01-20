# -*-coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.colorpicker import *
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from random import randint
from kivy.core.audio import SoundLoader
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

class Perle(Widget):
    couleur = NumericProperty(0)                      
        
class JeuPerles(Widget):        
    perleVoy0 = ObjectProperty(None) #rouge
    perleVoyU = ObjectProperty(None) #bleu
        
    voyDispo = ['O', 'U'] #liste des voyelles disponibles
    a=0
    print voyDispo
    print len(voyDispo)

    def consigneAlea(voyDispo):   #J'ai passé voyDispo en variable locale puisque ce n'est pas dans cette fonction qu'on la modifiera
        global a
        a = randint( 0, len(voyDispo)-1 )
        print(a)
        if(a==0):
            return "rouge.wav"
        elif(a==1):
            return "bleu.wav"    
               
    sound = SoundLoader.load( consigneAlea(voyDispo) )
    if sound:
        print("Sound found at %s" % sound.source)
            
        sound.play()
            
        
        
    def on_touch_move(self, touch):
        if self.perleVoyO.collide_point(touch.x,touch.y):
            self.perleVoyO.center = touch.pos
        elif self.perleVoyU.collide_point(touch.x,touch.y):
            self.perleVoyU.center=touch.pos
        
        print()
        
        
        

class PerlesApp(App):
    def build(self):
        jeuP = JeuPerles()
        return jeuP


if __name__ == '__main__':
    PerlesApp().run()
