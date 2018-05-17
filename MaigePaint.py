import pygame
from pygame.locals import *

pygame.display.init()
pygame.font.init()

#pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

done = False

screen = pygame.display.set_mode((0,0), pygame.SRCALPHA)
pygame.display.toggle_fullscreen()

text = pygame.font.SysFont(None, 70)
text2 = pygame.font.SysFont(None, 30)

logo = pygame.image.load("MaigeWide.jpg")
logo = logo.convert()
logo = pygame.transform.scale(logo, (screen.get_width(), screen.get_height()))

def loadScreen():
    #Loading screen for startup
    alphaFill = 0

    for i in range(30):
        screen.fill((255, 255, 255))
        pygame.display.flip()
        pygame.time.delay(17)

    while (alphaFill <= 255):
        logo.set_alpha(alphaFill)
        screen.fill((255, 255, 255))
        screen.blit(logo, (0,0))
        pygame.display.flip()
        pygame.time.delay(17)
        alphaFill += 3

def drawConfig():
    nextStage = False
    height = 10
    width = 10
    lastPress = "none"

    while(not nextStage):
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.display.quit()
                    pygame.quit()
                    nextStage = True
                    break
        else:
            if (pygame.mouse.get_pressed()[0]):

                if ((x >= 700) & (y >= 400)):
                    nextStage = True
                
                if ((((490 - x)**2 + (210 - y)**2) <= 900) & (height < 50)):
                    height += 1
                    if (lastPress == "height-"):
                        height += 1
                    if (lastPress == "width-"):
                        width += 1
                    if (lastPress == "width+"):
                        width -= 1
                    lastPress = "height+"
                    
                elif ((((345 - x)**2 + (210 - y)**2) <= 900) & (height > 1)):
                    height -= 1
                    if (lastPress == "height+"):
                        height -= 1
                    if (lastPress == "width-"):
                        width += 1
                    if (lastPress == "width+"):
                        width -= 1
                    lastPress = "height-"
                    
                elif ((((490 - x)**2 + (330 - y)**2) <= 900) & (width < 70)):
                    width += 1
                    if (lastPress == "height+"):
                        height -= 1
                    if (lastPress == "width-"):
                        width += 1
                    if (lastPress == "height-"):
                        height += 1
                    lastPress = "width+"
                    
                elif ((((345 - x)**2 + (330 - y)**2) <= 900) & (height > 1)):
                    width -= 1
                    if (lastPress == "height+"):
                        height -= 1
                    if (lastPress == "width+"):
                        width -= 1
                    if (lastPress == "height-"):
                        height += 1
                    lastPress = "width-"
                    
                else:
                    if (lastPress == "height+"):
                        height -= 1
                    if (lastPress == "height-"):
                        height += 1
                    if (lastPress == "width-"):
                        width += 1
                    if (lastPress == "width+"):
                        width -= 1
                    lastPress = "none"
                    
            screen.fill((230, 230, 230))
            pygame.draw.rect(screen, (255, 255, 255), ((380, 170), (75, 75)))
            pygame.draw.rect(screen, (255, 255, 255), ((380, 290), (75, 75)))
            pygame.draw.rect(screen, (255, 255, 255), ((700, 400), (150, 80)))
            pygame.draw.circle(screen, (255, 255, 255), (490, 210), 30)
            pygame.draw.circle(screen, (255, 255, 255), (345, 210), 30)
            pygame.draw.circle(screen, (255, 255, 255), (490, 330), 30)
            pygame.draw.circle(screen, (255, 255, 255), (345, 330), 30)
            screen.blit(text.render("Input grid dimensions:", 1, (0, 0, 0)), (150, 50))
            screen.blit(text2.render("Height:", 1, (0, 0, 0)), (380, 140))
            screen.blit(text2.render("Width:", 1, (0, 0, 0)), (380, 260))
            screen.blit(text.render("+", 1, (0, 0, 0)), (475, 177))
            screen.blit(text.render("+", 1, (0, 0, 0)), (475, 297))
            screen.blit(text.render("-", 1, (0, 0, 0)), (337, 180))
            screen.blit(text.render("-", 1, (0, 0, 0)), (337, 300))
            screen.blit(text.render(("%d" % height), 1, (0, 0, 0)), (390, 180))
            screen.blit(text.render(("%d" % width), 1, (0, 0, 0)), (390, 300))
            screen.blit(text.render("Begin", 1, (0, 0, 0)), (700, 410))
            pygame.display.flip()
            pygame.time.delay(150)
        
    drawArt(width, height)

def drawArt(x, y):
    width = x
    height = y
    pixelArray = [[None for i in range(width)] for j in range(height)]
    lastArray = []
    lastArray.append(pixelArray)
    colorArray = [(0,0,0),(128,128,128),(255,255,255),(128,0,0),(255,0,0),(0,128,0),(0,255,0),(0,0,128),(0,0,255),(255,128,0),(255,255,0),(255,0,128),(255,0,255),(0,255,128),(0,255,255),(128,255,0),(128,0,255)]
    nextStage = False
    held = False
    currentColor = 0
    page = 0

    while (not nextStage):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.display.quit()
                    pygame.quit()
                    nextStage = True
                    break
                
        screen.fill((230, 230, 230))
        
        for i in range(35):
            for j in range(25):
                pygame.draw.rect(screen, (128, 128, 128), ((16*i, 16*j), (8, 8)))
                pygame.draw.rect(screen, (128, 128, 128), ((8 + 16*i, 8 + 16*j), (8, 8)))
                pygame.draw.rect(screen, (255, 255, 255), ((8 + 16*i, 16*j), (8, 8)))
                pygame.draw.rect(screen, (255, 255, 255), ((16*i, 8 + 16*j), (8, 8)))

        pygame.draw.rect(screen, colorArray[currentColor], ((0, 400), (80,80)))

        for i in range(20):
            if (20*page + i < len(colorArray)):
                pygame.draw.rect(screen, colorArray[20*page + i], ((570 + 70 * (i % 4), 70 * int(i/4) + 10), (60, 60)))

        for i in range(x):
            for j in range(y):
                if (pixelArray[i][j] != None):
                    pygame.draw.rect(screen, pixelArray[i][j], (((560/x)*i, (400/y)*j), (560/x, 400/y)))

        if (pygame.mouse.get_pressed()[0]):
            mousex, mousey = pygame.mouse.get_pos()
            if ((mousex < 560) & (mousey < 400)):
                held = True
                (pixelArray[int(mousex/(560/x))])[int(mousey/(400/y))] = currentColor
                
            else:
                if (held == True):
                    held = False
                    lastArray.append(pixelArray)

        else:
            if (held == True):
                held = False
                lastArray.append(pixelArray)

        pygame.display.flip()
        #pygame.time.delay(17)
    
    plot()

def plot():
    unload()

def unload():
    
    screenOrig = pygame.Surface((screen.get_width(), screen.get_height()))
    screenOrig.blit(screen, (0,0))

    alphaFill = 255

    while (alphaFill >= 0):
        screenOrig.set_alpha(alphaFill)
        screen.fill((255, 255, 255))
        screen.blit(screenOrig, (0,0))
        pygame.display.flip()
        pygame.time.delay(17)
        alphaFill -= 6

while(not done):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.display.quit()
                pygame.quit()
                done = True
                break
    else:
        loadScreen()
        drawConfig()
