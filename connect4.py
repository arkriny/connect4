#!/usr/bin/env python3
#
# Written by Artem Krinitsyn. Public domain.

COLOR_YELLOW='\033[1;33m'
COLOR_RED='\033[1;31m'
COLOR_RESET='\033[0m'

class Game:
    def __init__(self):
        self.ROWS = 6
        self.COLS = 7
        self.grid = [[0] * self.COLS for _ in range(self.ROWS)]
        self.player = 1
        self.ended = False

    def move(self, move):
        if not (0 <= move < self.COLS):
            raise ValueError('move out of range')
        for i in range(self.ROWS-1, -1, -1):
            if self.grid[i][move] == 0:
                self.grid[i][move] = self.player
                for d in [[0, 1], [1, 0], [1, 1], [1, -1]]:
                    count = 0
                    for k in range(-3, 3+1):
                        x, y = i + (d[0] * k), move + (d[1] * k)
                        if 0 <= x < self.ROWS and 0 <= y < self.COLS and self.grid[x][y] == self.player:
                            count += 1
                            if count == 4:
                                self.ended = True
                                return
                        else:
                            count = 0

                self.player = 3 - self.player
                return
        raise ValueError('column is full')

    def render(self):
        for row in self.grid:
            for cell in row:
                if cell == 1:
                    print(COLOR_YELLOW, 'O', COLOR_RESET, sep='', end=' ')
                elif cell == 2:
                    print(COLOR_RED, 'O', COLOR_RESET, sep='', end=' ')
                else:
                    print('-', end=' ')
            print()
        # print number bar
        for i in range(self.COLS):
            print(i+1, end=' ')
        print()

def print_player(player):
    if player == 1:
        print(f'{COLOR_YELLOW}Yellow', end='')
    else:
        print(f'{COLOR_RED}Red', end='')
    print(COLOR_RESET, end='')

game = Game()
while True:
    game.render()
    if game.ended:
        print_player(game.player)
        print(' player won!')
        break

    print_player(game.player)
    print(f"'s turn. Enter the move (1-{game.COLS}): ", end='')
    try:
        while True:
            try:
                move = int(input().strip())
                game.move(move-1)
                break
            except ValueError as e:
                print(f'Invalid input: {e}, try again: ', end='')
    except BaseException:
        print()
        break
