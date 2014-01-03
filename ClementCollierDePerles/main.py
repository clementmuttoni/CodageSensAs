# -*-coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.colorpicker import *
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from random import randint
from kivy.core.audio import SoundLoader # pour le son

voyDispo = ['O', 'U']

class Perle(Widget):
	couleur = NumericProperty(0)
	
	
class JeuPerles(Widget):	
	perleVoy0 = ObjectProperty(None) #rouge
	perleVoyU = ObjectProperty(None) #bleu
	consigneSound = ''
	
	def consigneAlea():
		global voyDispo
		a = randint(0, voyDispo.__len__()-1)
		print("Voyelle tirée au hasard  : {}".format(voyDispo[a]))
		if a == 0:
		    return 'rouge.wav'
		elif a == 1:
		    return 'bleu.wav'
		    
		print("élément enlevé : {}".format(voyDispo.remove(0))
		
	
		    
	
	
	
	consigneSound = consigneAlea()
	print("son retenu : {}".format(consigneSound))
	print(voyDispo)
	
	sound = SoundLoader.load(consigneSound)
	sound.play()
	
	 #   print("Sound found at %s" % sound.source)
	  #  print("Sound is %.3f seconds" % sound.length)

	    
	
	
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
