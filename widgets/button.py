import pygame
from constants import *
pygame.init()

class Button: 
	font = pygame.font.SysFont ('comicsans', 30, True, False)

	def __init__ (self, x, y, width, height, color, text, function=None): 
		"""
		:param x: int
		:param y: int
		:param width: int
		:param height: int
		:param color: tuple
		:param text: String
		"""
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.text = text
		self.function = function

	def draw (self, window): 
		pygame.draw.rect (window, self.color, (self.x, self.y, self.width, self.height))
		
		text = Button.font.render (self.text, 1, WHITE)
		window.blit (text, (self.x + self.width * .15, self.y + self.height * .2))

	def onClick (self, x, y, *args): 

		if x > self.x and x < self.x + self.width: 

			if y > self.y and y < self.y + self.height: 

				try: 
					return self.function(*args)

				except: 
					pass