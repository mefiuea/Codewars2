values = {
    'queen': 9,
    'rook': 5,
    'bishop': 3,
    'knight': 3,
    'pawn': 1,
}
str = 'b-bishop'
x = str[2:]
print(x)
print(values[x], type(values[x]))