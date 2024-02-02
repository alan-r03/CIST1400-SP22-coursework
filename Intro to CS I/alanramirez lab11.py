import turtle

def draw_grid():
    lines = ((-150, 50), (150, 50), (-150, -50), (150, -50), (-50, 150), (-50, -150), (50, 150), (50, -150))
    benjamin.width(3)
    
    for i in range(0, len(lines), 2): #draws the grid lines of the tic-tac-toe grid
        benjamin.penup()
        benjamin.goto(lines[i][0], lines[i][1])
        benjamin.pendown()
        benjamin.goto(lines[i+1][0], lines[i+1][1])

def process_mouse(x, y):
    global winner
    if winner == True:
        return
    def change_grid_symbol(x, y, pos):
        global spots, player_symbol
        if spots[pos] == "-":
            spots[pos] = player_symbol
            benjamin.penup()
            benjamin.goto(x, y+25)
            benjamin.write(player_symbol, align="center", font=("Arial", 32))
            check_for_win(pos)
            switch_player()

    if -150 < x < -50 and 50 < y < 150:      #top left
        change_grid_symbol(-100, 50, 0)
    elif -50 < x < 50 and 50 < y < 150:      #top middle
        change_grid_symbol(0, 50, 1)
    elif 50 < x < 150 and 50 < y < 150:      #top right
        change_grid_symbol(100, 50, 2)
    elif -150 < x < -50 and -50 < y < 50:    #middle left
        change_grid_symbol(-100, -50, 3)
    elif -50 < x < 50 and -50 < y < 50:      #middle middle
        change_grid_symbol(0, -50, 4)
    elif 50 < x < 150 and -50 < y < 50:      #middle right
        change_grid_symbol(100, -50, 5)
    elif -150 < x < -50 and -150 < y < -50:  #bottom left
        change_grid_symbol(-100, -150, 6)
    elif -50 < x < 50 and -150 < y < -50:    #bottom middle
        change_grid_symbol(0, -150, 7)
    elif 50 < x < 150 and -150 < y < -50:    #bottom right
        change_grid_symbol(100, -150, 8)

def switch_player():
    global player_symbol
    player_symbol = "O" if player_symbol == "X" else "X"
    
def check_for_win(pos):
    global spots, winner
    winning_combos = [(0, 1, 2), (0, 3, 6), (0, 4, 8), (1, 4, 7), (2, 5, 8), (2, 4, 6), (3, 4, 5), (6, 7, 8)]
    # winning conditions with list keys: 0+1+2, 0+3+6, 0+4+8, 1+4+7, 2+5+8, 2+4+6, 3+4+5, 6+7+8
    for i in range(len(winning_combos)):
        if (spots[winning_combos[i][0]] != "-" and spots[winning_combos[i][1]] != "-" and spots[winning_combos[i][2]] != "-") and (spots[winning_combos[i][0]] == spots[winning_combos[i][1]] and spots[winning_combos[i][0]] == spots[winning_combos[i][2]]):
            winner = True
            benjamin.goto(0, -230)
            benjamin.write(f"{player_symbol} Wins!", align="center", font=("Arial",50, "underline"))
            break
    
screen = turtle.Screen()
benjamin = turtle.Turtle()
player_symbol = "X"
winner = False
spots = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

benjamin.speed(10)
benjamin.penup()
benjamin.hideturtle()
benjamin.goto(0, 160)
benjamin.write("Tic-Tac-Toe", align="center", font=("Arial", 50, "underline"))

draw_grid()
screen.onclick(process_mouse)