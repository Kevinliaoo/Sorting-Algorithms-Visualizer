import pygame 
from functions import *
from constants import *
from widgets import button
from widgets import spinner
from widgets import slider
pygame.init()

# pygame display setting
WIN = pygame.display.set_mode ((WIDTH, HEIGHT))
pygame.display.set_caption ("Sorting algorithms visualizator")

def main (window): 
	"""
	Main function
	"""
	# Adding widgets
	buttons = set()
	start_btn = button.Button (20, 525, BTN_WIDTH, BTN_HEIGHT, RED, "Start", startBtnClicked)
	regenerate_btn = button.Button (140, 525, BTN_WIDTH2, BTN_HEIGHT, RED, "Regenerate", regenerateClicked)
	algo_select = spinner.Spinner (10, 10, SPINNER_WIDTH, SPINNER_HEIGHT, GREEN, "Select sorting algorithm", ALGORITHMS)
	sizeSlider = slider.Slider (0, 100, 480, 550, 'Size', 20)

	buttons.add (start_btn)
	buttons.add (regenerate_btn)
	buttons.add (algo_select)
	buttons.add (sizeSlider)

	size = sizeSlider.value
	bars = generateBars (size)

	run = True
	while run: 
		pygame.display.set_caption ("Sorting algorithms visualizator")
		draw (window, buttons, bars)
		algorithm = algo_select.text
		size = sizeSlider.value

		for event in pygame.event.get(): 

			# Quit
			if event.type == pygame.QUIT: 
				run = False

			# Left mouse click
			if pygame.mouse.get_pressed()[0]: 
				posX, posY = pygame.mouse.get_pos()
				
				# Check if any button was clicked
				for btn in buttons: 

					btn.onClick(posX, posY)

				newBar = regenerate_btn.onClick(posX, posY, size)
				start_btn.onClick(posX, posY, bars, window, algorithm)
				# When anything else is clicked returns None. Protective programming
				if newBar != None: 
					bars = newBar

		# Check wether slider's values were changed
		if sizeSlider.value != size:
			size = sizeSlider.value
			# Regenerate bars when size is changed
			bars = generateBars (size)

	pygame.quit()


if __name__ == '__main__':
	main(WIN)