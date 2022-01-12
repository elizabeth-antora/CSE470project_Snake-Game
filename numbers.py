class SnakeCursesGame:

    def __init__(self):
    self.snake = Snake()

    self.game = Game(80, 24)
    self.game.add_snake(self.snake)
    self.game.start()

    self.w = curses.initscr()
    self.w.nodelay(True)
    self.w.keypad(True)
    curses.curs_set(0) # hide cursor

    self.view = SnakeCursesView(self.w, self.game)
    self.view.add_action_listener(self)

    def turn_action(self, direction):
    self.snake.turn(direction)

    def run(self):
    while True:
        self.view.draw()
        self.w.refresh()
        time.sleep(0.1)
        self.view.undraw()

        ch = self.w.getch()
        if ch in [curses.KEY_UP, curses.KEY_DOWN,
              curses.KEY_LEFT, curses.KEY_RIGHT]:
        self.view.got_key(ch)
        elif ch != -1:
        break

        self.game.tick()

def main():
    try:
    game = SnakeCursesGame()
    game.run()
    finally:
    try:
        curses.endwin() # ensure that exceptions display correctly
    except:
        pass

if __name__ == '__main__':
    main()
import random

class Numbers:

    def __init__(self, w, h, checker):
        self.number = 0
        self.top = 9
        self.w = w
        self.h = h
        self.x = self.y = -1
        self.checker = checker
        self.valid = False

    def next(self):

        if self.number == self.top:
            # option: don't show any more numbers
            #self.valid = False
            #return False

            # option: start over at 1
            self.number = 0

        self.number += 1
        self.rand_pos()
        while not self.checker.check_space_empty(self.x, self.y):
            self.rand_pos()
        self.valid = True
        return True

    def rand_pos(self):
        self.x = random.randint(0, self.w - 1)
        self.y = random.randint(0, self.h - 1)

    def get_x(self): return self.x
    def get_y(self): return self.y
    def get_number(self): return self.number
    def is_valid(self): return self.valid
