
import pygame
from checkers.game import Game
from minimax.algorithm import minimax

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 51)
GREEN = (128, 255, 0)
GREY = (128, 128, 128)


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def _move(self, row, col):
    piece = self.board.get_piece(row, col)
    if self.selected and piece == 0 and (row, col) in self.valid_moves:
        self.board.move(self.selected, row, col)
        skipped = self.valid_moves[(row, col)]
        if skipped:
            self.board.remove(skipped)
        self.change_turn()
    else:
        return False

    return True


def draw_valid_moves(self, moves):
    for move in moves:
        row, col = move
        pygame.draw.circle(self.win, GREEN, (col * SQUARE_SIZE +
                           SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)


def change_turn(self):
    self.valid_moves = {}
    if self.turn == RED:
        self.turn = WHITE
    else:
        self.turn = RED


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


main()
