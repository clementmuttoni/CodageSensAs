# -*-coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.colorpicker import *
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from random import randint
from kivy.core.audio import SoundLoader # pour le son

class Perle(Widget):
	couleur = NumericProperty(0)
	
	
			
			
			
	
class JeuPerles(Widget):	
	perleVoy0 = ObjectProperty(None) #rouge
	perleVoyU = ObjectProperty(None) #bleu
	
	voyDispo = ['O', 'U']
	def consigneAlea():
		a = randint(0, voyDispo.len)
		print(a)
	
	
	consigneAlea()
	
	
	
	sound = SoundLoader.load('bleu.wav')
	if sound:
	    print("Sound found at %s" % sound.source)
	    print("Sound is %.3f seconds" % sound.length)
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
