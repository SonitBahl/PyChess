import pygame

def home_screen():
    pygame.init()
    
    # Constants
    WIDTH, HEIGHT = 600, 600
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FONT = pygame.font.SysFont(None, 48)
    
    # Create the game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess Game - Home")
    
    def draw_text(text, x, y):
        text_surface = FONT.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)
    
    running = True
    while running:
        screen.fill(WHITE)
        draw_text("Welcome to Chess", WIDTH // 2, HEIGHT // 3)
        draw_text("Press ENTER to Start", WIDTH // 2, HEIGHT // 2)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False 

    return 

if __name__ == "__main__":
    home_screen()  
