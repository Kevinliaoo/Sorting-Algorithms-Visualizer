import random
import math 
import pygame
from constants import * 
from widgets.spinner import Spinner
pygame.init()

def draw (window, buttons, bars): 
	"""
	Drawing function.
	:param window: pygame.Surface
	:param buttons: set
	:param bars: list
	"""
	# Fill background
	window.fill (BLACK)
	
	# Draw screen
	pygame.draw.rect (window, WHITE, (100, 80, RECT_WIDTH, RECT_HEIGHT))
	drawBars (bars, window)
	drawButtons (buttons, window)

	pygame.display.update()

def drawButtons (buttons, window): 
	"""
	This function draws buttons. 
	:param buttons: set or list or tuple
	:param window: pygame.Surface
	"""

	for btn in buttons:
		btn.draw (window)

		if isinstance(btn, Spinner): 

			if btn.showChilds:
				for i in btn.subButtons: 
					i.draw(window)

def drawBars (bars, window): 
	"""
	This function draws the bars in the white screen. 
	:param bars: list
	:param window: pygame.Surface
	"""
	for index, bar in enumerate(bars): 
		drawBar (window, index, len(bars), bar, LBLUE)

def drawBar (window, index, barLength, height, color, x=None):
	"""
	This function draws a single bar. 
	:param window: pygame.Surface
	:param index: int 
	:param barLength: int
	:param height: int
	:param color: tuple
	"""
	height *= 2
	barWidth = (RECT_WIDTH-SCREEN_BLANK) / barLength
	if x == None: 
		x = SCREEN_BLANK + index * barWidth
	y = 80 + RECT_HEIGHT - height

	pygame.draw.rect (window, color, (x, y, barWidth, height))

def switchBars (bars, pos1, pos2, window): 
	"""
	This function switches places grafically two bars. 
	:param bars: list
	:param pos1: int
	:param pos2: int 
	"""
	barWidth = (RECT_WIDTH-SCREEN_BLANK) / len(bars)
	xPos1 = 180 + barWidth * pos1
	temp1 = xPos1
	xPos2 = 180 + barWidth * pos2
	temp2 = xPos2
	run = True

	# Position processing
	difPos1 = xPos1 - math.floor(xPos1)
	xPos1 = math.floor (xPos1)
	difPos2 = xPos2 - math.floor(xPos2)
	xPos2 = math.floor(xPos2)
 
	while run: 
		# Redraw display
		pygame.draw.rect (window, WHITE, (100, 80, RECT_WIDTH, RECT_HEIGHT))

		# Draw rects (not the switching ones)
		for index, bar in enumerate (bars): 
			if index != pos1 and index != pos2:
				drawBar (window, index, len(bars), bar, GREEN)

		xPos1 += .5
		xPos2 -= .5

		# Moving bars
		drawBar (window, pos1, len(bars), bars[pos1], RED, x=xPos1)
		drawBar (window, pos2, len(bars), bars[pos2], RED, x=xPos2)

		pygame.display.update()

		if xPos1 == math.floor(temp2):
			xPos1 = temp2
			xPos2 = temp1
			run = False

	drawBar (window, pos1, len(bars), bars[pos1], RED, x=xPos1)
	drawBar (window, pos2, len(bars), bars[pos2], RED, x=xPos2)

def generateBars (size): 
	"""
	This function generates random integers. 
	"""
	bars = []
	for _ in range (size): 
		bars.append (random.randint(0, 100))

	return bars

def startBtnClicked (bars, window, algorithm): 

	if algorithm == RUN_INSERTION: 
		insertionSort (bars, window)

def regenerateClicked(size): 
	"""
	This function regenerates a new set of bars when regenerate button is clicked.
	"""
	print ("Regenerating")
	return generateBars (size)

# ***** Sorting algorithms *****
def insertionSort (bars, window): 
	"""
	:param bars: list
	:param speed: int
	:param:window: pygame.Surface
	"""

	for i in range(1, len(bars)): 

		key = bars[i] 

		j = i-1
		while j >= 0 and key < bars[j] : 
			# Move
			switchBars (bars, j, j+1, window)
			bars[j + 1] = bars[j] 
			j -= 1
			bars[j + 1] = key 