values = {
    'queen': 9,
    'rook': 5,
    'bishop': 3,
    'knight': 3,
    'pawn': 1,
}


def pieces_value(arr, s):
    score_white = 0
    score_black = 0
    for list_element in arr:
        for element in list_element:
            if element[0] == 'w' and not element[2:] == 'king':
                score_white += values[element[2:]]
            elif element[0] == 'b' and not element[2:] == 'king':
                score_black += values[element[2:]]
            else:
                continue

    if s == 'white' or s == 'w':
        return score_white
    if s == 'black' or s == 'b':
        return score_black


board1 = [['b-bishop', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', 'b-queen', ' ', ' ', ' ', ' ', 'w-queen'],
          [' ', 'b-king', ' ', 'b-pawn', 'w-rook', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', 'w-pawn', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', 'w-bishop', ' ', ' '],
          ['w-king', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', 'b-pawn', 'b-pawn', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

board2 = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', 'b-king', ' ', ' '],
          [' ', 'b-knight', ' ', ' ', 'w-pawn', ' ', ' ', ' '],
          [' ', ' ', 'w-bishop', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', 'w-pawn', ' ', ' ', ' ', 'w-pawn', ' ', ' '],
          [' ', ' ', ' ', ' ', 'b-pawn', ' ', ' ', ' '],
          [' ', 'w-rook', ' ', ' ', ' ', 'w-king', ' ', ' ']]

board3 = [[' ', ' ', ' ', ' ', 'b-king', ' ', ' ', ' '],
          [' ', 'b-bishop', ' ', ' ', 'b-pawn', 'b-pawn', ' ', ' '],
          [' ', ' ', ' ', ' ', 'b-knight', ' ', ' ', ' '],
          [' ', ' ', 'w-queen', ' ', ' ', ' ', ' ', ' '],
          [' ', 'w-bishop', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'b-rook'],
          [' ', 'w-pawn', 'w-pawn', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', 'w-king', ' ', ' ', ' ', ' ', ' ']]

# print(pieces_value(board1, 'white'), f'Dla białych, tablica 1')
# print(pieces_value(board1, 'black'), f'Dla czarnych, tablica 1')
print(pieces_value(board3, 'black'))
