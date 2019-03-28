import pygame

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("PATHFINDER")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)               ## Redundant

def showmap(map):

    for i in range(len(map)):
        for j in range(len(map)):
            if(map[i][j]):
                pygame.draw.rect(screen, WHITE, ((i * 10), (j * 10), 10, 10))
    
    pygame.display.flip()

