import random
import curses

# Getting the screen to listen to all the action taking place
screen = curses.initscr()

# Hiding the screen
curses.curs_set(0)

# getting dimnetions
screen_height, screen_width = screen.getmaxyx()

# making the interface window
window = curses.newwin(screen_height, screen_width, 0,0)

# Listining to keyboard input
window.keypad(1)
# refresh every 100 ms
window.timeout(100)

# Snake position
snake_x = screen_width/4
snake_y = screen_height/2

# snake
snake = [
    [snake_x, snake_y],
    [snake_x, snake_y-1],
    [snake_x, snake_y-2]
]

# Food
food = [screen_height/2, screen_width/2]

# Drawing the food
window.addch(food[0], food[1], curses.ACS_DIAMOND)

# addign the keyboard input into a variable
key = curses.KEY_RIGHT

# while running
while True:
    # get next key pressed
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    # if snake is dead
    if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:] :
        # end game
        curses.curs_set(1)
        curses.endwin()
        quit()

    # The head of the snake
    new_head = [snake[0][0], snake[0][1]]

    # user input
    if key == curses.KEY_DOWN:
        new_head[0] +=1
    if key == curses.KEY_UP:
        new_head[0] -=1
    if key == curses.KEY_RIGHT:
        new_head[1] +=1
    if key == curses.KEY_LEFT:
        new_head[1] -=1

    # add the head the snake object
    snake.insert(0, new_head)

    # if the snake eats food
    if snake[0] == food:
        food = None
        # make new food
        while food is None:
            new_food = [
                random.randint(1, screen_height-1),
                random.randint(1, screen_width-1)
            ]

            food  = new_food if new_food not in snake else None

        # increase snake size
        window.addch(food[0], food[1], curses.ACS_DIAMOND)

    else:
        # Draw the snake
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
