import pygame

class Player():

	def __init__(self,start_pos):
		self.x, self.y = start_pos
		self.speed = 10

	def draw(self,win):
		pygame.draw.rect(win,(255,255,255), (self.x,self.y, 10, 50))

	def move(self,keys):
		if keys[pygame.K_UP] and self.y > 0:
			self.y -= self.speed
		elif keys[pygame.K_DOWN] and self.y < 350:
			self.y += self.speed