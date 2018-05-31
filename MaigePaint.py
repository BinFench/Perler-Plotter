import pygame
from pygame.locals import *
from copy import deepcopy

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
    lastAction = "none"
    indice = 0
    maxIndice = 0
    width = x
    height = y
    pixelArray = [[None for i in range(width)] for j in range(height)]
    lastArray = []
    lastArray.append(deepcopy(pixelArray))
    colorArray = [(255,255,255),(216,204,146),(175,137,92),(205,158,128),(160,95,91),(120,95,91),(0,0,0),(96,105,110),(145,146,150),(88,20,35),(157,19,42),(225,73,98),(250,125,139),(241,193,179),(233,198,158),(255,207,242),(218,110,160),(222,84,169),(199,16,140),(255,114,171),(155,138,242),(156,93,163),(124,86,171),(245,151,87),(238,106,57),(238,159,54),(219,206,13),(236,232,107),(209,226,36),(169,247,231),(181,242,165),(163,228,146),(130,183,49),(121,171,86),(84,151,74),(135,172,243),(85,135,198),(93,154,201),(124,155,219),(86,108,183),(4,40,124),(51,155,156),(155,212,221),(153,153,153),(223,172,153),(222,147,126),(223,212,71),(143,166,120),(147,198,193),(176,106,57),(147,77,26),(221,158,185),(249,133,110),(140,183,101),(152,198,211),(157,151,211),(182,182,182)]
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

        pygame.draw.rect(screen, (255,255,255), ((570, 360), (40,40)))
        pygame.draw.rect(screen, (255,255,255), ((520, 410), (40,40)))
        pygame.draw.rect(screen, (255,255,255), ((190, 400), (180,80)))
        pygame.draw.rect(screen, (255,255,255), ((105, 410), (60,60)))
        pygame.draw.rect(screen, (255,255,255), ((400, 410), (60,60)))

        screen.blit(text.render("+", 1, (0, 0, 0)), (576, 353))
        screen.blit(text.render("+", 1, (0, 0, 0)), (526, 403))
        screen.blit(text2.render("undo", 1, (0, 0, 0)), (110, 430))
        screen.blit(text.render("%d x %d" % (width, height), 4, (0, 0, 0)), (200, 415))
        screen.blit(text2.render("redo", 1, (0, 0, 0)), (405, 430))

        for i in range(x):
            for j in range(y):
                if (pixelArray[i][j] != None):
                    pygame.draw.rect(screen, colorArray[pixelArray[i][j]], (((560/x)*i, (400/y)*j), (560/x, 400/y)))

        if (pygame.mouse.get_pressed()[0]):
            mousex, mousey = pygame.mouse.get_pos()
            if ((mousex < 560) & (mousey < 400)):
                lastAction = "draw"
                held = True
                (pixelArray[int(mousex/(560/x))])[int(mousey/(400/y))] = currentColor
            elif ((mousex >= 105) & (mousex <= 165) & (mousey >= 410) & (mousey <= 470)):
                if (held == False):
                    held = True
                    if (indice > 0):
                        indice -= 1
                        newPixelArray = deepcopy(lastArray[indice])
                        newWidth = len(newPixelArray)
                        newHeight = len(newPixelArray[0])
                        pixelArray = deepcopy(newPixelArray)
                lastAction = "undo"
            elif ((mousex >= 400) & (mousex <= 460) & (mousey >= 410) & (mousey <= 470)):
                if (held == False):
                    held = True
                    if (indice < maxIndice):
                        indice += 1
                        newPixelArray = deepcopy(lastArray[indice])
                        newWidth = len(newPixelArray)
                        newHeight = len(newPixelArray[0])
                        pixelArray = deepcopy(newPixelArray)
                lastAction = "redo"
            elif ((mousex > 560) & (mousey < 350)):
                if (held == True):
                    if (lastAction == "draw"):
                        for i in range(maxIndice - indice):
                            lastArray.pop()
                        maxIndice = indice + 1
                        indice = maxIndice
                        lastArray.append(deepcopy(pixelArray))
                    held = False
                for i in range(20):
                    if (((mousex >= 570 + 70 * (i % 4)) and (mousex <= (570 + 70 * (i % 4) + 60)) and (mousey >= 10 + 70 * int(i/4)) and (mousey <= 70 + 70 * int(i/4)))):
                        if (20*page + i < len(colorArray)):
                            currentColor = 20*page + i
                lastAction = "none"
            else:
                if (held == True):
                    held = False
                    if (lastAction == "draw"):
                        for i in range(maxIndice - indice):
                            lastArray.pop()
                        maxIndice = indice + 1
                        indice += 1
                        lastArray.append(deepcopy(pixelArray))
                lastAction = "none"
        else:
            if (held == True):
                held = False
                if (lastAction == "draw"):
                    for i in range(maxIndice - indice):
                        lastArray.pop()
                    maxIndice = indice + 1
                    indice += 1
                    lastArray.append(deepcopy(pixelArray))
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
