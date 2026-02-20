import pygame
import sys

pygame.init()

screen_width = 800
screen_length = 800

screen = pygame.display.set_mode((screen_width, screen_length))
pygame.display.set_caption("Money Clicker")

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load the image and get it's rect. Then get the center of the screen
money = pygame.image.load("32px-United-states-dollar-usd.jpg").convert_alpha()
money_rect = money.get_rect()
money_rect.center = (screen_width // 2, screen_length // 2)

# Make a loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicks on the money
            if money_rect.collidepoint(event.pos):
                print("Money clicked!!!")

    screen.fill(WHITE)
    # Draw the money
    screen.blit(money, money_rect)

    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()