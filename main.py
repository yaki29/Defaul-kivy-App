from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import random
from kivy.properties import ListProperty, ObjectProperty

from kivy.graphics.vertex_instructions import (Rectangle,
						Ellipse,
						Line)
from kivy.graphics.context_instructions import Color


class ScatterTextWidget(BoxLayout):

	text_colour = ObjectProperty([random.random() for i in range(3)] + [1])
	
	def colour_change(self, *args):
		color = [random.random() for i in range(3)] + [0.75]
		self.text_colour = color
	
#	def __init__(self, **kwargs):
#		super(ScatterTextWidget, self).__init__(**kwargs)
	def canvas_drawing(self):
		pass
#		with self.canvas.before:
#			Color(0, 1, 0, 1)
#			Rectangle(pos=(0,100), size=(300, 100))
#			Ellipse(pos=(100,400), size=(300,100))
#			Line(points=[0, 0, 500, 600, 400, 300],
#				close=True,
#				width=3)





class TutorialApp(App):
	def build(self):
		return ScatterTextWidget()

#def function(*args):
#	print("Text Changed")

if __name__ == '__main__':
	TutorialApp().run()
