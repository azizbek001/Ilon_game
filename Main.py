import pygame
from random import randrange

RES = 600
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }


length = 1
snake = [(x, y)]

dx, dy = 0, 0
score = 0
fps = 5

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 38, bold=True)
img = pygame.image.load("1.jpg").convert()

while True:
	sc.blit(img, (0, 0))
	[(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
	pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))

	render_score = font_score.render(f"TEZLIK > {score}", 1, pygame.Color('orange'))

	sc.blit(render_score, (5, 5))

	x += dx * SIZE
	y += dy * SIZE 

	snake.append((x, y))
	snake = snake[-length:]

	if snake[-1] == apple:
		apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
		length += 1
		fps += 1
		score += 1
	if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
		while True:
			render_end = font_end.render("O'YIN TUGADI !!!", 1, pygame.Color('orange'))
			sc.blit(render_end, (RES // 2 - 200, RES // 3))
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()



	pygame.display.flip()
	clock.tick(fps)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	key = pygame.key.get_pressed()
	if key[pygame.K_w] and dirs['W']:
		dx, dy = 0, -1
		dirs = {'W': True, 'S': False, 'A': True, 'D': True, }


	if key[pygame.K_s] and dirs['S']:
		dx, dy = 0, 1
		dirs = {'W': False, 'S': True, 'A': True, 'D': True, }


	if key[pygame.K_a] and dirs['A']:
		dx, dy = -1, 0
		dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
		

	if key[pygame.K_d] and dirs['D']:
		dx, dy = 1, 0
		dirs = {'W': True, 'S': True, 'A': False, 'D': True, }
		
