import pygame

pygame.init()

screen = pygame.display.set_mode((500,600)) # Tạo ra màn hình chiều roonjg500, chiều dài 600

GREY = (171,133,44)
WHITE = (255,255,255)

running = True
while True:
	screen.fill(GREY)

	mouse_x, mouse_y = pygame.mouse.get_pos()
	print(mouse_y)
	
	pygame.draw.rect(screen, WHITE,(100, 50, 50, 50 )) #draw : vẽ, rect : Hình chữ nhật
	pygame.draw.rect(screen, WHITE,(200, 50, 50, 50 ))
	pygame.draw.rect(screen, WHITE,(100, 200, 50, 50 ))
	pygame.draw.rect(screen, WHITE,(200, 200, 50, 50 ))
	pygame.draw.rect(screen, WHITE,(300, 50, 150, 50 ))
	pygame.draw.rect(screen, WHITE,(300, 50, 150, 50 ))
	pygame.draw.rect(screen, WHITE,(300, 150, 150, 50 ))

	for event in pygame.event.get(): #event: sự kiện nào đấy
		if event.type == pygame.QUIT:
			running = False
	pygame.display.flip() #in ra màn hình

pygame.quit()