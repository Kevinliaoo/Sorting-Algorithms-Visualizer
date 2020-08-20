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
		pygame.display.set_caption ('Running Insertion sort algorithm...')
		insertionSort (bars, window)

	elif algorithm == RUN_MERGE: 
		pygame.display.set_caption ('Running Merge sort algorithm...')
		indexes = [x for x in range(len(bars))]
		print (bars)
		mergeSort (bars, indexes, window)
		print (bars)

	elif algorithm == RUN_BUBBLE: 
		pygame.display.set_caption ('Running Bubble sort algorithm...')
		bubbleSort (window, bars)

def regenerateClicked(size): 
	"""
	This function regenerates a new set of bars when regenerate button is clicked.
	:param size: int
	"""
	return generateBars (size)

# ***** Sorting algorithms *****
def insertionSort (bars, window): 
	"""
	Insertion sort algorithm. 
	:param bars: list
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

def mergeSort (bars, indexes, window): 

	if len(bars) > 1: 
		

def mergeSortr(arr, indexes, window): 

	if len(arr) > 1: 
		mid = len(arr) // 2 
		L = arr[:mid] 
		R = arr[mid:] 
		L_index = indexes[:mid]
		R_index = indexes[mid:]

		mergeSort(L, L_index, window)
		mergeSort(R, R_index, window) 

		i = j = k = 0

		while i < len(L_index) and j < len(R_index): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i += 1
			else: 
				arr[k] = R[j] 
				j += 1
 
			k += 1

		while i < len(L): 
			arr[k] = L[i] 
			i += 1
			k += 1

		while j < len(R): 
			arr[k] = R[j] 
			j += 1
			k += 1

def bubbleSort (window, bars): 
	"""
	Bubble sort algorithm. 
	:param window: pygame.Surface
	:param bars: list
	"""
	n = len(bars)

	for i in range(n): 

		for j in range(0, n-i-1):

			if bars[j] > bars[j+1]: 
				switchBars (bars, j, j+1, window)
				bars[j], bars[j+1] = bars[j+1], bars[j]