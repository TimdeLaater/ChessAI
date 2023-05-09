# set up the window
import pygame

board= any

def createBoard():
    size = (640, 640)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Chess Game")

    # set up the board
    board = pygame.Surface((600, 600))
    board.fill((255, 206, 158))

    # draw the board
    for x in range(0, 8, 2):
        for y in range(0, 8, 2):
            pygame.draw.rect(board, (210, 180, 140), (x*75, y*75, 75, 75))
            pygame.draw.rect(board, (210, 180, 140), ((x+1)*75, (y+1)*75, 75, 75))

    # add the board to the screen
    screen.blit(board, (20, 20))

    pygame.display.flip()
    return(board, screen)
def setPieces():
    piece_positions = {
    "black_pawn": [(i, 1) for i in range(8)],
    "white_pawn": [(i, 6) for i in range(8)],
    "black_rook": [(0, 0), (7, 0)],
    "white_rook": [(0, 7), (7, 7)],
    "black_knight": [(1, 0), (6, 0)],
    "white_knight": [(1, 7), (6, 7)],
    "black_bishop": [(2, 0), (5, 0)],
    "white_bishop": [(2, 7), (5, 7)],
    "black_queen": [(3, 0)],
    "white_queen": [(3, 7)],
    "black_king": [(4, 0)],
    "white_king": [(4, 7)],
}

    pieces = []
    for piece_type, positions in piece_positions.items():
        for position in positions:
            color = "black" if piece_type.startswith("black") else "white"
            piece = Piece(color, position[0], position[1], piece_type.split("_")[1])
            pieces.append(piece)

    # draw the pieces
    for piece in pieces:
     piece.draw(board)