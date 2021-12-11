# Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.

# The rules of the game are:

# Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
# Any live cell with more than three live neighbours dies, as if by overcrowding.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any dead cell with exactly three live neighbours becomes a live cell.
# Each cell's neighborhood is the 8 cells immediately around it (i.e. Moore Neighborhood). 
# The universe is infinite in both the x and y dimensions and all cells are initially dead - except

# of the living cells. (If there are no living cells, then return [[]].)

# For illustration purposes, 0 and 1 will be represented as ░░ and ▓▓ blocks respectively 
# (PHP, C: plain black and white squares). You can take advantage of the htmlize function to get a text 
# representation of the universe, e.g.:

# print(htmlize(cells))



def get_neighbours(x, y):
    return {(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)}

def get_generation(cells, generations):
    if not cells: return cells
    xm, ym, xM, yM = 0, 0, len(cells[0]) - 1, len(cells) - 1
    cells = {(x, y) for y, l in enumerate(cells) for x, c in enumerate(l) if c}
    for _ in range(generations):
        cells = {(x, y) for x in range(xm - 1, xM + 2) for y in range(ym - 1, yM + 2)
                    if 2 < len(cells & get_neighbours(x, y)) < 4 + ((x, y) in cells)}
        xm, ym = min(x for x, y in cells), min(y for x, y in cells)
        xM, yM = max(x for x, y in cells), max(y for x, y in cells)
    return [[int((x, y) in cells) for x in range(xm, xM + 1)] for y in range(ym, yM + 1)]

def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('<:LF:>')
    return ''.join(s)

start = [[1,0,0],
         [0,1,1],
         [1,1,0]]
end   = [[0,1,0],
         [0,0,1],
         [1,1,1]]
         
test.describe('Glider<:LF:>' + htmlize(start))
test.it('Glider 1')

resp = get_generation(start, 1)
test.expect(resp == end, 'Got<:LF:>' + htmlize(resp) + '<:LF:>instead of<:LF:>' + htmlize(end))