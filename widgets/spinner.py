from widgets.button import Button

class Spinner (Button): 

	def __init__ (self, x, y, width, height, color, text, *args): 
		"""
		:param *args: list or tuple
		"""
		Button.__init__ (self, x, y, width, height, color, text)

		self.subButtons = []
		self.showChilds = False

		pos = 0
		for btn in args[0]: 
			# Change the color of spinner's sub elements
			c = []
			for i in color: 
				c.append (i - int(i * 0.2))

			sub = SubSpinner (x, y, width, height, tuple(c), btn, pos)
			self.subButtons.append (sub)
			pos += 1

	# Override
	def onClick (self, x, y): 
		"""
		This function shows the sub items of the spinner when is clicked.
		:param x: int
		:param y: int
		"""
		# Ckeck if clicked inside the spinner's area
		clickedInside = x > self.x and x < self.x + self.width and y > self.y and y < self.y + self.height

		# Check if clicked a sub item
		clickedChild = x > self.x and x < self.x + self.width and y > self.y + self.height and y < self.y + self.height + len(self.subButtons) * self.height

		if self.showChilds: 

			if clickedChild: 
				self.showChilds = False

				# Get the sub item cliked
				for i in self.subButtons: 
					algo = i.onClick(x, y)
					
					if algo != None:
						self.text = algo

			else: 
				self.showChilds = False

		else: 

			if clickedInside: 
				self.showChilds = True


class SubSpinner (Button): 

	def __init__ (self, spinX, spinY, width, height, color, text, position): 
		"""
		:param position: int
		"""

		x = spinX
		y = spinY + height + height * position
		Button.__init__ (self, x, y, width, height, color, text, self._clickFunc)

	def _clickFunc (self): 
		"""
		Function that is triggered when is clicked.
		"""
		return self.text