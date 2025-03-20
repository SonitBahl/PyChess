import pygame
import chess
import home_screen

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8
WHITE = (238, 238, 210)
BLACK = (118, 150, 86)
HIGHLIGHT_COLOR = (255, 255, 0)  # Yellow for move highlighting
MOVE_COLOR = (0, 255, 0)  # Green circles for legal moves
TEXT_COLOR = (0, 0, 0)
FONT = pygame.font.SysFont(None, 36)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Chess board
board = chess.Board()

# Function to draw the chessboard
def draw_board(selected_square=None, moves=[]):
    for row in range(8):
        for col in range(8):
            square = chess.square(col, 7 - row)
            color = WHITE if (row + col) % 2 == 0 else BLACK
            
            # Highlight the selected square
            if square == selected_square:
                color = HIGHLIGHT_COLOR

            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Highlight legal moves
    for move in moves:
        move_col, move_row = chess.square_file(move.to_square), 7 - chess.square_rank(move.to_square)
        center_x = move_col * SQUARE_SIZE + SQUARE_SIZE // 2
        center_y = move_row * SQUARE_SIZE + SQUARE_SIZE // 2
        pygame.draw.circle(screen, MOVE_COLOR, (center_x, center_y), 10)  # Small circle

# Function to draw pieces as text
def draw_pieces():
    for row in range(8):
        for col in range(8):
            square = chess.square(col, 7 - row)
            piece = board.piece_at(square)
            if piece:
                text = FONT.render(piece.symbol(), True, TEXT_COLOR)
                text_rect = text.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
                screen.blit(text, text_rect)

# Function to run the chess game
def run_game():
    running = True
    selected_square = None
    moves = []
    
    while running:
        screen.fill((0, 0, 0))  # Clear screen
        draw_board(selected_square, moves)
        draw_pieces()
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col, row = x // SQUARE_SIZE, y // SQUARE_SIZE
                square = chess.square(col, 7 - row)
                
                if selected_square is None:
                    piece = board.piece_at(square)
                    if piece and (piece.color == board.turn):
                        selected_square = square
                        moves = [move for move in board.legal_moves if move.from_square == selected_square]
                else:
                    move = chess.Move(selected_square, square)
                    if move in moves:
                        board.push(move)
                    selected_square = None
                    moves = []

    pygame.quit()

if __name__ == "__main__":
    home_screen.home_screen() 
    run_game()
