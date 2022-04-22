import random

class Field:

    def __init__(self,board_size):

        self.board = []
        self.bombs = set({})
        self.size = board_size
        self.fields_left = board_size ** 2

        """
        
        0 - emply space
        X - bomb
        1+ - bombs around
        
        """

        for x in range(board_size):

            self.board.append([0 for i in range(board_size)])

    def roll_bombs(self,amount):

        if amount > (self.fields_left*0.8):
            print("Too many bombs")
            return False

        while len(self.bombs) != amount:
            x = random.randrange(self.size)
            y = random.randrange(self.size)
            self.bombs.add((x,y))


     
        """
        apply bombs
        """

        for cords in self.bombs:
            self.board[cords[0]][cords[1]] = "X"

    def Apply_numbers(self):

        for cords in self.bombs:

            x, y = cords

            for i in range(3):
                current_x = x-1+i
                if current_x < 0: continue
                for j in range(3):
                    current_y = y-1+j
                    if current_y < 0: continue
                    try:
                        field = self.board[current_x][current_y]
                    except:
                        continue

                    if type(field) == int:
                        self.board[current_x][current_y] +=1


    def discover_board(self,cords) -> list:
        x , y = cords
        discovered = []

        if self.board[x][y] == "X" : return False

        def look_deeper(cord_x , cord_y):
            
            if cord_x < 0 or cord_x >= self.size or cord_y < 0 or cord_y >= self.size: return False

            value = self.board[cord_x][cord_y] 
            if value == "X": return False

            if (cord_x,cord_y) in discovered : return False

            if value > 0:
                discovered.append((cord_x,cord_y))
                return False

            discovered.append((cord_x,cord_y))

            for i in range(-1 , 2):
                for j in range(-1 , 2):
                    if i == 0 and j == 0 : continue
                    look_deeper(cord_x + i , cord_y +j)


   
        look_deeper(x ,y)
        
        self.fields_left -= len(discovered)


        return discovered

    def get_bombs(self):
        return self.bombs   

