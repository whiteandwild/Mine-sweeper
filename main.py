from window import *

from Field import Field


flags = 0


def start(size , b,v_board , obj):
    
    global board , visible_board , bombs , board_size , game,flags
    game = obj
    bombs = b
    board_size = size
    board = Field(board_size)
    flags = 0
    board.roll_bombs(bombs)
    board.Apply_numbers()

    visible_board = v_board
    '''
    visible_board = []

    for x in range(board_size):

            visible_board.append(["?" for i in range(board_size)])
    '''

def print_nice(l):

    
    print('-' * board_size*4)

    for elem in l:
        for field in elem:

            print(str(field).center(3) , end="")
        print('')
    print('-' * board_size*4)

def press(where , type):
    
    x = where // board_size
    y = where % board_size

    #if visible_board[x][y] != "?": return False

    if type == "left": #left click
        if game.get_val(where) == "F" : return False
        found = board.discover_board((x,y))
        
        if not found :
            for bomb in board.get_bombs():

                bomb = bomb[0] * board_size + bomb[1]
                game.disable_all()
                game.show_bomb(bomb)
               

            print('You lost')
            return
            
        show_on_board(found)

    elif type == "right":
        Add_flag(where)
        

    if Check_win():\
        print('you won')
def show_on_board(args):
    for elem in args:
        game.show(elem[0] * board_size + elem[1] ,board.board[elem[0]][elem[1]] if board.board[elem[0]][elem[1]] != 0 else "" )
        
def Add_flag(cords):
    global flags
    
    value = game.get_val(cords)
    x = "F"
    print(value)
    match value:
        
        case "":
            
            flags +=1
        case "F":
            x = ""
            flags -=1
        case _:
            return False
    game.show_flag(cords , x)
def Check_win():
    print(flags , bombs , board.fields_left)
    if flags != bombs : return False

    if board.fields_left == bombs : return True

    return False


    





'''
print_nice(board.board)
print_nice(visible_board)

show_on_board(board.discover_board((2,3)))


print_nice(visible_board)'''