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
	start_btn = button.Button (50, 550, BTN_WIDTH, BTN_HEIGHT, RED, "Start", startBtnClicked)
	algo_select = spinner.Spinner (10, 10, SPINNER_WIDTH, SPINNER_HEIGHT, GREEN, "Select sorting algorithm", ALGORITHMS)
	speedSlider = slider.Slider (0, 20, 320, 550, 'Speed', 5)
	sizeSlider = slider.Slider (0, 100, 520, 50, 'Size', 20)

	buttons.add (start_btn)
	buttons.add (algo_select)
	buttons.add (speedSlider)
	buttons.add (sizeSlider)

	run = True
	while run: 
		draw (window, buttons)
		algorithm = algo_select.text
		speed = speedSlider.value
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


	pygame.quit()


if __name__ == '__main__':
	main(WIN)