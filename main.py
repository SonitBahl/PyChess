import pygame
import chess
import home_screen

pygame.init()

WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8
WHITE = (238, 238, 210)
BLACK = (118, 150, 86)
HIGHLIGHT_COLOR = (255, 255, 0)
MOVE_COLOR = (0, 255, 0)
TEXT_COLOR = (0, 0, 0)
FONT = pygame.font.SysFont(None, 36)
POPUP_FONT = pygame.font.SysFont(None, 28)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

board = chess.Board()

def draw_board(selected_square=None, moves=[]):
    for row in range(8):
        for col in range(8):
            square = chess.square(col, 7 - row)
            color = WHITE if (row + col) % 2 == 0 else BLACK
            
            if square == selected_square:
                color = HIGHLIGHT_COLOR

            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    for move in moves:
        move_col, move_row = chess.square_file(move.to_square), 7 - chess.square_rank(move.to_square)
        center_x = move_col * SQUARE_SIZE + SQUARE_SIZE // 2
        center_y = move_row * SQUARE_SIZE + SQUARE_SIZE // 2
        pygame.draw.circle(screen, MOVE_COLOR, (center_x, center_y), 10)

def draw_pieces():
    for row in range(8):
        for col in range(8):
            square = chess.square(col, 7 - row)
            piece = board.piece_at(square)
            if piece:
                text = FONT.render(piece.symbol(), True, TEXT_COLOR)
                text_rect = text.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
                screen.blit(text, text_rect)

def draw_instructions():
    popup_width, popup_height = 400, 300
    popup_x, popup_y = (WIDTH - popup_width) // 2, (HEIGHT - popup_height) // 2
    pygame.draw.rect(screen, (200, 200, 200), (popup_x, popup_y, popup_width, popup_height), border_radius=10)

    instructions = [
        "Chess Game Instructions:",
        "- Click on a piece to see its legal moves.",
        "- Click on a highlighted square to move the piece.",
        "- Press 'I' to toggle this instruction screen.",
        "- Press 'Esc' to close this screen.",
        "- Standard chess rules apply."
    ]

    y_offset = popup_y + 30
    for line in instructions:
        text = POPUP_FONT.render(line, True, TEXT_COLOR)
        screen.blit(text, (popup_x + 20, y_offset))
        y_offset += 40

def run_game():
    running = True
    selected_square = None
    moves = []
    show_instructions = False
    
    while running:
        screen.fill((0, 0, 0))
        draw_board(selected_square, moves)
        draw_pieces()

        if show_instructions:
            draw_instructions()

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    show_instructions = not show_instructions
                elif event.key == pygame.K_ESCAPE:
                    show_instructions = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not show_instructions:
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
