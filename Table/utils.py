import random

class Utils:
    def __init__(self):
        ceva = 0

    def init_board_player1(self):
        # de retinut !! maxim 350 pixeli dimensiunea pentru o coloana
        board_player1 = []
        # un element din board = o coloana pe tabla, o coloana are lista de elemente, coord x si coord y pentru primul element
        # as fi putut sa fac o clasa pentru tabla si init_board() sa fie defapt constructorul, dar am vrut sa fie ceva mai unic =))
        coloana = [[], 1000, 40]
        board_player1.append(coloana)
        coloana = [[], 930, 40]
        board_player1.append(coloana)
        coloana = [[], 860, 40]
        board_player1.append(coloana)
        coloana = [[], 790, 40]
        board_player1.append(coloana)
        coloana = [[], 720, 40]
        board_player1.append(coloana)
        coloana = [[], 650, 40]
        board_player1.append(coloana)
        coloana = [[], 555, 40]
        board_player1.append(coloana)
        coloana = [[], 485, 40]
        board_player1.append(coloana)
        coloana = [[], 415, 40]
        board_player1.append(coloana)
        coloana = [[], 345, 40]
        board_player1.append(coloana)
        coloana = [[], 275, 40]
        board_player1.append(coloana)
        coloana = [[], 200, 40]
        board_player1.append(coloana)
        coloana = [[], 200, 770]
        board_player1.append(coloana)
        coloana = [[], 275, 770]
        board_player1.append(coloana)
        coloana = [[], 345, 770]
        board_player1.append(coloana)
        coloana = [[], 415, 770]
        board_player1.append(coloana)
        coloana = [[], 485, 770]
        board_player1.append(coloana)
        coloana = [[], 555, 770]
        board_player1.append(coloana)
        coloana = [[], 650, 770]
        board_player1.append(coloana)
        coloana = [[], 720, 770]
        board_player1.append(coloana)
        coloana = [[], 790, 770]
        board_player1.append(coloana)
        coloana = [[], 860, 770]
        board_player1.append(coloana)
        coloana = [[], 930, 770]
        board_player1.append(coloana)
        coloana = [[], 1000, 770]
        board_player1.append(coloana)

        board_player1[5][0].append(1)
        board_player1[5][0].append(1)
        board_player1[5][0].append(1)
        board_player1[5][0].append(1)
        board_player1[5][0].append(1)

        board_player1[7][0].append(1)
        board_player1[7][0].append(1)
        board_player1[7][0].append(1)

        board_player1[12][0].append(1)
        board_player1[12][0].append(1)
        board_player1[12][0].append(1)
        board_player1[12][0].append(1)
        board_player1[12][0].append(1)

        board_player1[23][0].append(1)
        board_player1[23][0].append(1)

        return board_player1

    def init_board_player2(self):
        board_player2 = []
        coloana = [[], 1000, 770]
        board_player2.append(coloana)
        coloana = [[], 930, 770]
        board_player2.append(coloana)
        coloana = [[], 860, 770]
        board_player2.append(coloana)
        coloana = [[], 790, 770]
        board_player2.append(coloana)
        coloana = [[], 720, 770]
        board_player2.append(coloana)
        coloana = [[], 650, 770]
        board_player2.append(coloana)
        coloana = [[], 555, 770]
        board_player2.append(coloana)
        coloana = [[], 485, 770]
        board_player2.append(coloana)
        coloana = [[], 415, 770]
        board_player2.append(coloana)
        coloana = [[], 345, 770]
        board_player2.append(coloana)
        coloana = [[], 275, 770]
        board_player2.append(coloana)
        coloana = [[], 200, 770]
        board_player2.append(coloana)
        coloana = [[], 200, 40]
        board_player2.append(coloana)
        coloana = [[], 275, 40]
        board_player2.append(coloana)
        coloana = [[], 345, 40]
        board_player2.append(coloana)
        coloana = [[], 415, 40]
        board_player2.append(coloana)
        coloana = [[], 485, 40]
        board_player2.append(coloana)
        coloana = [[], 555, 40]
        board_player2.append(coloana)
        coloana = [[], 650, 40]
        board_player2.append(coloana)
        coloana = [[], 720, 40]
        board_player2.append(coloana)
        coloana = [[], 790, 40]
        board_player2.append(coloana)
        coloana = [[], 860, 40]
        board_player2.append(coloana)
        coloana = [[], 930, 40]
        board_player2.append(coloana)
        coloana = [[], 1000, 40]
        board_player2.append(coloana)

        board_player2[5][0].append(2)
        board_player2[5][0].append(2)
        board_player2[5][0].append(2)
        board_player2[5][0].append(2)
        board_player2[5][0].append(2)

        board_player2[7][0].append(2)
        board_player2[7][0].append(2)
        board_player2[7][0].append(2)

        board_player2[12][0].append(2)
        board_player2[12][0].append(2)
        board_player2[12][0].append(2)
        board_player2[12][0].append(2)
        board_player2[12][0].append(2)

        board_player2[23][0].append(2)
        board_player2[23][0].append(2)

        return board_player2

    def init_board(self):
        board_player1 = self.init_board_player1()
        board_player2 = self.init_board_player2()
        board = [board_player1, board_player2]
        return board

    def color_coosing(self):
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        while b == a or (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
            b = random.randint(1, 9)

        if a == 1:
            path_a = "assets/blue.png"
        elif a == 2:
            path_a = "assets/light-blue.png"
        elif a == 3:
            path_a = "assets/grey.png"
        elif a == 4:
            path_a = "assets/black.png"
        elif a == 5:
            path_a = "assets/brown.png"
        elif a == 6:
            path_a = "assets/green.png"
        elif a == 7:
            path_a = "assets/purple.png"
        elif a == 8:
            path_a = "assets/red.png"
        else:
            path_a = "assets/white.png"

        if b == 1:
            path_b = "assets/blue.png"
        elif b == 2:
            path_b = "assets/light-blue.png"
        elif b == 3:
            path_b = "assets/grey.png"
        elif b == 4:
            path_b = "assets/black.png"
        elif b == 5:
            path_b = "assets/brown.png"
        elif b == 6:
            path_b = "assets/green.png"
        elif b == 7:
            path_b = "assets/purple.png"
        elif b == 8:
            path_b = "assets/red.png"
        else:
            path_b = "assets/white.png"

        color_path = [path_a, path_b]
        return color_path