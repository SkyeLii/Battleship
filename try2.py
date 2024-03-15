import pygame

pygame.init()

bg = pygame.image.load("c:\\Users\\asus\\Battleship\\bg.jpg")
bs = pygame.image.load("c:\\Users\\asus\\Battleship\\bs.png")
screen = pygame.display.set_mode([1200, 800])
clock = pygame.time.Clock() 
text = []
text2 = []
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', ' I', 'J']
background = pygame.Surface([600, 600], pygame.SRCALPHA)
backgr = pygame.Surface([600, 600], pygame.SRCALPHA)
color1 = (0,0,49)
color2 = (0,0,134)
color3 = (49,0,0)
color4 = (134,0,0)
WHITE = (255,255,255)
font = pygame.font.SysFont('Helvetica', 30)
sx, sy = 40, 40
for i in range(11):
    for j in range(11):
        if i == 0 or j == 0: 
            c = color1 if (i+j) % 2 == 0 else color2
            c2 = color3 if (i+j) % 2 == 0 else color4
            if i == 0 and j != 0: text.append(font.render(str(j), True, WHITE))
            if j == 0 and i != 0: text2.append(font.render(letters[i-1], True, WHITE))
        else: 
            c = (0,0,5)
            c2 = (5,0,0)
        pygame.draw.rect(background, c, (i*sx, j*sy, sx, sy), 0)
        pygame.draw.rect(background, WHITE, (i*sx, j*sy, sx, sy), 1)        
        pygame.draw.rect(backgr, c2, (i*sx, j*sy, sx, sy), 0)
        pygame.draw.rect(backgr, WHITE, (i*sx, j*sy, sx, sy), 1)

run = True 
while run:  
    screen.blit(bg, (0, 0))
    screen.blit(bs, (220, 20))
    clock.tick(100)
    for event in pygame.event.get():         
        if event.type == pygame.QUIT:             
            run = False      

    screen.blit(background, (110, 210))     
    screen.blit(backgr, (670, 210))  
    
    for i in range(10):
        
        screen.blit(text[i], ((i+1)*sx + 120, 210))
        screen.blit(text2[i], ( 120, (i+1)*sy + 210))
        screen.blit(text[i], ((i+1)*sx + 680, 210))
        screen.blit(text2[i], ( 680, (i+1)*sy + 210))
          
    pygame.display.update()

pygame.quit()