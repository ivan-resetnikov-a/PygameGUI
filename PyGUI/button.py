import pygame as pg
pg.font.init()

defaulFont = pg.font.SysFont('Arial', 50)



class Button:
	def __init__(self,
			onPress,
			
			text:str='<text>',
			textColor:tuple[int]=(255, 255, 255),
			textFont:pg.font.Font=defaulFont,
			textAntiAliasing:bool=True,

			size:tuple[int]=(150, 50),
			color:tuple[int]=(0, 0, 0),
			pos:list[float]=[0, 0],

			customImage:pg.Surface=None):

		self._pos = pos
		self._size = size

		self._onPress = onPress
		self._holdingButton = False

		self._customImage = customImage

		self._generateWiget(text, textColor, textFont, textAntiAliasing, size, color)


	def _generateWiget(self, text, textColor, textFont, textAntiAliasing, size, color):
		text = textFont.render(text, textAntiAliasing, textColor)

		self._buttonSurface = pg.Surface(size)
		self._buttonSurface.fill(color)

		if self._customImage:
			self._buttonSurface.blit(self._customImage, (0, 0))

		self._buttonSurface.blit(text, (
			size[0] * 0.5 - text.get_width()  * 0.5,
			size[1] * 0.5 - text.get_height() * 0.5))


	def render(self, window):
		mouse = pg.mouse.get_pos()
		if self._pos[0]+self._size[0] > mouse[0] > self._pos[0] and\
		   self._pos[1]+self._size[1] > mouse[1] > self._pos[1] and\
		   pg.mouse.get_pressed()[0] and not self._holdingButton:
			self._onPress()
			self._holdingButton = True

		if not pg.mouse.get_pressed()[0]:
			self._holdingButton = False

		window.blit(self._buttonSurface, self._pos)