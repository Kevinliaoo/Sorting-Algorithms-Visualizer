import pygame
from constants import * 
pygame.init()

class Slider: 
	barLength = 400
	barThick = 5
	scrollerSize = 20
	barColor = WHITE
	sliderColor = RED
	font = pygame.font.SysFont ('comicsans', 25, True, False)

	def __init__ (self, minium, maxium, posX, posY, tag, default): 
		"""
		:param minium: int
		:param maxium: int
		:param posX: int
		:param posY: int
		:param color: tuple
		:param tag: String
		"""
		
		self.x = posX
		self.y = posY
		self.minium = minium
		self.maxium = maxium
		self.tag = tag
		self.value = default

		# Calculate the position of the scroller 
		percent = ((100 * self.value) // self.maxium) / 100
		self.scrollerPos = Slider.barLength * percent + self.x

		# Turn True when scroller is clicked
		self.flag = False

	def onClick (self, x, y): 
		"""
		This method changes the scroller position and the slider value when slider is scrolled.
		"""
		clickedX = x > self.scrollerPos - Slider.scrollerSize//2 and x < self.scrollerPos - Slider.scrollerSize//2 + Slider.scrollerSize
		clickedY = y > self.y - Slider.scrollerSize//4 and y < self.y - Slider.scrollerSize//4 + Slider.scrollerSize
		clicked = clickedX and clickedY

		if self.flag: 

			if clicked: 
				pass

			else: 
				# Change scroller position and slider value
				# Extreme cases
				if x > self.x + Slider.barLength: 
					self.scrollerPos = Slider.barLength + self.x
					self.value = self.maxium
				elif x < self.x: 
					self.value = 1
					percent = ((100 * self.value) // self.maxium) / 100
					self.scrollerPos = Slider.barLength * percent + self.x

				else: 
					self.scrollerPos = x
					percent = (x - self.x) / Slider.barLength
					self.value = int (percent * self.maxium)

			self.flag = False

		else:

			if clicked: 
				self.flag = True

	def draw (self, window): 
		# Draw slider bar
		pygame.draw.rect (window, Slider.barColor, (self.x, self.y, Slider.barLength, Slider.barThick))

		# Draw labels
		label = Slider.font.render (self.tag + ': ' + str(self.value), 1, WHITE)
		window.blit (label, (self.x, self.y - 40))

		minVal = Slider.font.render (str(self.minium), 1, WHITE)
		window.blit (minVal, (self.x - 25, self.y - 5))

		maxVal = Slider.font.render (str(self.maxium), 1, WHITE)
		window.blit (maxVal, (self.x + 25 + Slider.barLength, self.y - 5))

		# Draw scroller
		pygame.draw.rect (window, Slider.sliderColor, (self.scrollerPos - Slider.scrollerSize//2, self.y - Slider.scrollerSize//4, Slider.scrollerSize, Slider.scrollerSize))