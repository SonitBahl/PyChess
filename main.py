import pygame
import chess

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8
WHITE = (238, 238, 210)
BLACK = (118, 150, 86)
TEXT_COLOR = (0, 0, 0)
FONT = pygame.font.SysFont(None, 36)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Chess board
board = chess.Board()

# Function to draw the chessboard
def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

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

# Main loop
running = True
selected_square = None
moves = []
while running:
    draw_board()
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
