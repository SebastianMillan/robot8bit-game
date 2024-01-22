import sys, pygame

pygame.init()
width, height= 800,600
screen = pygame.display.set_mode((width,height))
bg_color= (41,44,53)
player_sprite=pygame.image.load('resources/basic_robot.png')
x_pos=100
y_pos=100
velocity=12

# Comenzamos el bucle del juego
run=True
while run:
	screen.blit(player_sprite,(100,100))
	for event in pygame.event.get():
		if event.type == pygame.QUIT: run = False
		if event.type == pygame.KEYDOWN:
			if pygame.K_LEFT:
				x_pos -= velocity
			if pygame.K_RIGHT:
				x_pos += velocity
			if pygame.K_UP:
				y_pos -= velocity
			if pygame.K_DOWN:
				y_pos += velocity
		pygame.display.update()

	screen.fill(bg_color)
	screen.blit(player_sprite, (0, 0))

	# Salgo de pygame
pygame.quit()