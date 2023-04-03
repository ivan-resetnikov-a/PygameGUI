import PyGUI as gui
import pygame as pg


def test():
	print('sosi!')


button0 = gui.Button(text='Click me!', size=(200, 50), onPress=test)


window = pg.display.set_mode((500, 500))
clock = pg.time.Clock()

running = True
while running:
	window.fill((255, 255, 255))
	for event in pg.event.get():
		match event.type:
			case pg.QUIT: running = False

	button0.render(window)

	clock.tick(60)
	pg.display.flip()
