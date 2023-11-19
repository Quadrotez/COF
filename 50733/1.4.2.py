# cell – Width of cell in a symbols
# cells – Number of cell in a string
# row – Heght of the cell in a string
# rows – Number of strings


cell = int(input())
cells = int(input())
row = int(input())
rows = int(input())

print((('*' + ('-') * cell) * cells + '*\n') + ((('|' + (' ' * cell)) * cells + '|\n')) * row + (
            ('*' + (cell * '-') + ('+' + '-' * cell) * (cells - 1) + '*\n') + (
                ('|' + (' ' * cell)) * cells + '|\n') * row) * (rows - 1) + ('*' + ('-') * cell) + (
                  '*' + ('-') * cell) * (cells - 1) + '*')


