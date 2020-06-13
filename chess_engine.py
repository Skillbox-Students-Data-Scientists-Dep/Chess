# -*- coding: utf-8 -*-

# TODO: прописать ходы для всех фигур: как они могут ходить через условия
# TODO: прописать кнструкторы для всех фигур. Можно начать с короля. Наверно лучше создать одну фигуру полноценно,
# потом уже по подобию описать и другие фигуры тоже

# Сначала задаём константы. Нарисуем массив, который представляет собой шахматную доску:
BOARD = [[False] * 8 for _ in range(8)]
for y in range(8, 0, -1):
    for x in range(1, 9):
        BOARD[8 - y][x - 1] = {(x, y, 'white'): False} if (x + y) % 2 else {(x, y, 'black'): False}


# массив вида 8 х 8 представляет собой список словарей. Кажый список - это горизонтальная строка шахматной доски,
# столбец - вертикальная. Каждый словарь - это статус каждой клетки доски.
# обозначение клеток доски:
# {(x, y, color)}: is_empty - координаты клетки (x, y), color - цвет клетки, is_empty - свободна ли сейчас клетка,
# или на ней находится фигура (если пуста, то False, если нет - то какая фигура на ней стоит)


class Chessboard:
    """basic class Chessboard config"""

    def __init__(self):
        self = BOARD

    def __repr__(self):
        res = ''
        for _y in range(8):
            res += ''.join(map(str, BOARD[_y])) + "\n"  # Все точки будут скллены в одну строку и перенесены.
        #         # Так как два join объединяет только строки, а не объекты, приводим каждый элемент списка к строке.
        #         # Проще всего это сделать при помощи операции map, которая берет каждый элемент списка и применяет
        #      # к нему какую-либо функцию. В данном случае каждый объект передается функцией привидения к строке - str
        return res


class King(Chessboard):
    """child class the King Chess piece"""

    def __init__(self):
        pass

    def move(self):
        pass

    def attack(self):
        pass

    def under_check(self):
        pass

    def checkmate(self):
        pass


class Queen(Chessboard):
    """child class the Queen Chess piece"""

    def __init__(self):
        pass

    def move(self):
        pass

    def attack(self):
        pass


class Rook(Chessboard):
    """child class the Rook Chess piece"""

    def __init__(self):
        pass

    def move(self):
        pass

    def attack(self):
        pass


class Bishop(Chessboard):
    """child class the Bishop Chess piece"""

    def __init__(self):
        pass

    def move(self):
        pass

    def attack(self):
        pass


class Knight(Chessboard):
    """child class the Knight Chess piece"""

    def __init__(self):
        pass

    def move(self):
        pass

    def attack(self):
        pass


class Pawn(Chessboard):
    """child class the Pawn Chess piece"""

    def __init__(self):
        pass

    def move(self):
        pass

    def attack(self):
        pass

    def reward_choice(self):
        self.choice = input("Make your choice: Queen, Rook, Bishop or Knight: ").capitalize()
        if self.choice == "Queen":
            self = Queen()
        elif self.choice == "Rook":
            self = Rook()
        elif self.choice == "Bishop":
            self = Bishop()
        elif self.choice == "Knight":
            self = Knight()
