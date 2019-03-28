import pygame

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("PATHFINDER")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)               ## Redundant
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def show_map(map, considered_points):

    for i in range(len(map)):
        for j in range(len(map)):
            if((i, j) in considered_points):
                pygame.draw.rect(screen, RED, ((i * 5), (j * 5), 5, 5))
            elif(map[i][j]):
                pygame.draw.rect(screen, WHITE, ((i * 5), (j * 5), 5, 5))
    
    pygame.display.flip()

def show_path(map, considered_points, path):

    for i in range(len(map)):
        for j in range(len(map)):
            if((i, j) in path):
                pygame.draw.rect(screen, GREEN, ((i * 5), (j * 5), 5, 5))
            elif((i, j) in considered_points):
                pygame.draw.rect(screen, RED, ((i * 5), (j * 5), 5, 5))
            elif(map[i][j]):
                pygame.draw.rect(screen, WHITE, ((i * 5), (j * 5), 5, 5))
    
    pygame.display.flip()