from email.policy import default
import kivy



from Field import Field

board_size = 10
bombs = 30
flags = 0


def __init__():
    
    global board , visible_board

    board = Field(board_size)

    board.roll_bombs(bombs)
    board.Apply_numbers()
    visible_board = []

    for x in range(board_size):

            visible_board.append(["?" for i in range(board_size)])
    

def print_nice(l):

    
    print('-' * board_size*4)

    for elem in l:
        for field in elem:

            print(str(field).center(3) , end="")
        print('')
    print('-' * board_size*4)
    
def show_on_board(args):
    for elem in args:
        visible_board[elem[0]][elem[1]] = board.board[elem[0]][elem[1]]

def Add_flag(cords):

    value = visible_board[cords[0]][cords[1]]

    match value:
        
        case "?":
            visible_board[cords[0]][cords[1]] = "F"
            flags +=1
        case "F":
            visible_board[cords[0]][cords[1]] = "?"
            flags -=1
        case default:
            return False
    
def Check_win():
    
    if flags != bombs : return False

    if board.fields_left == bombs : return True

    return False

__init__()



print_nice(board.board)
print_nice(visible_board)

show_on_board(board.discover_board((2,3)))


print_nice(visible_board)