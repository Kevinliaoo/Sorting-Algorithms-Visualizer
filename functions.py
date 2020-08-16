import pygame
from constants import * 
from widgets.spinner import Spinner
pygame.init()

def draw (window, buttons): 
	"""
	Drawing function.
	"""
	# Fill background
	window.fill (BLACK)
	
	# Draw screen
	pygame.draw.rect (window, WHITE, (100, 80, RECT_WIDTH, RECT_HEIGHT))
	drawButtons (buttons, window)

	pygame.display.update()

def drawButtons (buttons, window): 
	"""
	This function draws buttons. 
	:param buttons: set or list or tuple
	:param window: 
	"""

	for btn in buttons:
		btn.draw (window)

		if isinstance(btn, Spinner): 

			if btn.showChilds:
				for i in btn.subButtons: 
					i.draw(window)



def startBtnClicked (): 
	print ("Algorithm started")
