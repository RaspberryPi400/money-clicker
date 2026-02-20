import pygame
import sys

# Initialize Pygame and fonts
pygame.init()
pygame.font.init()

# Screen settings
screen_width = 600
screen_length = 600
screen = pygame.display.set_mode((screen_width, screen_length))
pygame.display.set_caption("Money Clicker")

# Colors
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Upgrade 1 settings
upgrade1_color = GREEN
upgrade1_x = 100
upgrade1_y = 100
upgrade1_width = 160
upgrade1_length = 50
upgrade1_cost = 30
upgrade1_cash_per_click = 5

# Make upgrade 1 rectangle
upgrade1 = pygame.Rect(upgrade1_x, upgrade1_y, upgrade1_width, upgrade1_length)

# Font settings
font_size = 15
font = pygame.font.SysFont(None, font_size)
upgrade1_content = f"Cash per click: {upgrade1_cash_per_click} - Cost: {upgrade1_cost}"
upgrade1_text_color = BLACK

# Make the text for upgrade 1
upgrade1_text_surface = font.render(upgrade1_content, True, upgrade1_text_color)
# Get the text rect and center on rectangle
upgrade1_text_rect = upgrade1_text_surface.get_rect()
upgrade1_text_rect.center = upgrade1.center

# This is the amount of cash the player has (the score)
cash = 0
cash_per_click = 1 # Initial cash per click
won = False # Flag to track if the player has won

# Load the image and get its rect. Then make it bigger. Then get the center of the screen and put it there
# Make sure you have a file named '32px-United-states-dollar-usd.jpg' in the same directory
try:
    mone = pygame.image.load('32px-United-states-dollar-usd.jpg').convert_alpha()
    money_width = 400
    money_length = 100
    money = pygame.transform.scale(mone, (money_width, money_length))
    money_rect = money.get_rect()
    money_rect.center = (screen_width // 2, screen_length // 2)
except pygame.error as e:
    print(f"Error loading image: {e}")
    # Create a placeholder if image fails to load
    money = pygame.Surface((money_width, money_length))
    money.fill(GREEN)
    money_rect = money.get_rect()
    money_rect.center = (screen_width // 2, screen_length // 2)


# Function to display the cash counter
def display_cash():
    cash_content = f"Cash: {cash}"
    cash_text_surface = font.render(cash_content, True, BLACK)
    screen.blit(cash_text_surface, (10, 10))

# Function to display the win screen
def display_win_screen():
    won_size = 100
    won_font = pygame.font.SysFont(None, won_size) # Use the correct font variable name here
    won_content = "YOU WON!"
    won_text_color = GREEN
    won_text_surface = won_font.render(won_content, True, won_text_color) # Render with the larger font
    won_text_rect = won_text_surface.get_rect()
    won_text_rect.center = (screen_width // 2, screen_length // 2)
    screen.blit(won_text_surface, won_text_rect)

# Make a loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicks on the money
            if money_rect.collidepoint(event.pos):
                print("Money clicked!")
                cash += cash_per_click # Use the variable for cash per click
                if cash >= 100 and not won:
                    print("You won!")
                    won = True # Set the win flag to True

            # If the user clicks on the upgrade button
            if upgrade1.collidepoint(event.pos):
                if cash >= upgrade1_cost:
                    cash -= upgrade1_cost
                    cash_per_click += upgrade1_cash_per_click
                    print(f"Upgrade purchased! Cash per click is now {cash_per_click}.")
                else:
                    print("Not enough cash!")

    # Drawing
    screen.fill(WHITE) # Fill the screen with white each frame

    # Draw the upgrade button and text
    pygame.draw.rect(screen, upgrade1_color, upgrade1)
    screen.blit(upgrade1_text_surface, upgrade1_text_rect)
    
    # Draw the money image
    screen.blit(money, money_rect)

    # Display the cash counter
    display_cash()

    # Display the win screen if the player has won
    if won:
        display_win_screen()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()