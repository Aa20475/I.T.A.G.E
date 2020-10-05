import pygame as pg

import screenmanager as sm
import eventhandler as eh


pg.init()

gameDisp = pg.display.set_mode((800,800))
pg.display.set_caption("Path Visualiser")

clock = pg.time.Clock()	

crash = False

screenmanager = sm.ScreenManager(gameDisp)
eventhandler = eh.EventHandler(screenmanager)

while not crash:

	crash = eventhandler.update()

	screenmanager.render()

	pg.display.update()
	clock.tick(60)