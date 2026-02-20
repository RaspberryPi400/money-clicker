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
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Font settings
font_size = 20
font = pygame.font.SysFont(None, font_size)

# Upgrades
class Upgrade:
    def __init__(self, x, y, width, height, base_cost, boost, name):
        self.rect = pygame.Rect(x, y, width, height)
        self.cost = base_cost
        self.boost = boost
        self.name = name
        self.color = GRAY

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2) # Add a border
        
        # Text for name and boost.
        text_line1 = f"{self.name} (+${self.boost})"
        text_line2 = f"Cost: ${self.cost}"
        
        surf1 = font.render(text_line1, True, BLACK)
        surf2 = font.render(text_line2, True, BLACK)
        
        # Center the text inside the button.
        surface.blit(surf1, (self.rect.x + 10, self.rect.y + 10))
        surface.blit(surf2, (self.rect.x + 10, self.rect.y + 30))

# List of upgrades
upgrades = [
    Upgrade(20, 100, 200, 60, 50, 2, "Basic Clicker"),
    Upgrade(20, 180, 200, 60, 500, 15, "Better Mouse"),
    Upgrade(20, 260, 200, 60, 2500, 100, "Money Printer")
]

# Game Variables
cash = 0
cash_per_click = 1 
won = False 
WIN_CONDITION = 10000

# Load the image
try:
    mone = pygame.image.load('32px-United-states-dollar-usd.jpg').convert_alpha()
    money_width = 300
    money_length = 150
    money = pygame.transform.scale(mone, (money_width, money_length))
    money_rect = money.get_rect()
    # Move it slightly to the right to make room for upgrade buttons.
    money_rect.center = (screen_width // 2 + 100, screen_length // 2)
except pygame.error as e:
    print(f"Error loading image: {e}")
    money = pygame.Surface((300, 150))
    money.fill(GREEN)
    money_rect = money.get_rect()
    money_rect.center = (screen_width // 2 + 100, screen_length // 2)

# UI Functions
def display_ui():
    # Show Cash
    cash_surf = font.render(f"Cash: ${cash}", True, BLACK)
    screen.blit(cash_surf, (20, 20))
    
    # Show current click power
    power_surf = font.render(f"Cash per click: ${cash_per_click}", True, BLACK)
    screen.blit(power_surf, (20, 50))
    
    # Show Goal
    goal_surf = font.render(f"Goal: ${WIN_CONDITION}", True, BLACK)
    screen.blit(goal_surf, (screen_width - 150, 20))

def display_win_screen():
    won_size = 80
    won_font = pygame.font.SysFont(None, won_size)
    won_text_surface = won_font.render("YOU WON!", True, GREEN)
    won_text_rect = won_text_surface.get_rect(center=(screen_width // 2, screen_length // 4))
    
    # Draw a background box for the win text so it's readable.
    box_rect = won_text_rect.inflate(40, 40)
    pygame.draw.rect(screen, WHITE, box_rect)
    pygame.draw.rect(screen, BLACK, box_rect, 4)
    screen.blit(won_text_surface, won_text_rect)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Clicking the Money
            if money_rect.collidepoint(event.pos):
                cash += cash_per_click
                if cash >= WIN_CONDITION and not won:
                    won = True

            # Clicking Upgrades
            for upgrade in upgrades:
                if upgrade.rect.collidepoint(event.pos):
                    if cash >= upgrade.cost:
                        cash -= upgrade.cost
                        cash_per_click += upgrade.boost
                        # INCREASE THE COST BY 50% FOR NEXT TIME (Scaling Difficulty)
                        upgrade.cost = int(upgrade.cost * 1.5) 
                        print(f"Bought {upgrade.name}! Click power: {cash_per_click}")
                    else:
                        print("Not enough cash!")

    # Drawing
    screen.fill(WHITE)

    # Draw upgrades
    for upgrade in upgrades:
        upgrade.draw(screen)
        
    # Draw money image
    screen.blit(money, money_rect)

    # Draw UI text
    display_ui()

    # Draw win screen if applicable
    if won:
        display_win_screen()

    pygame.display.flip()

pygame.quit()
sys.exit()