import sys, pygame

gridWidth = 3
gridHeight = 2
cellSize = 100
padding = 50
borderSize = 2

def computeNumberPossibilities(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return computeNumberPossibilities(n - 1) + computeNumberPossibilities(n - 2)

def __findAllPossibilities(n, x, l, total):
    if x >= n:
        total.append(l)
        return

    __findAllPossibilities(n, x + 1, l + [("V", x)], total)

    if x != n - 1:
        __findAllPossibilities(n, x + 2, l + [("H", x)], total)

def findAllPossibilities(n):
    total = []
    __findAllPossibilities(n, 0, [], total)
    return total

def selectDomino(x, orientation):
    if orientation == "V":
        pygame.draw.rect(screen, selected, (2 + padding + x * cellSize, borderSize + padding + 0 * cellSize, cellSize - borderSize, 2 * cellSize - borderSize))
    elif orientation == "H":
        pygame.draw.rect(screen, selected, (borderSize + padding + x * cellSize, borderSize + padding + 0 * cellSize, 2 * cellSize - borderSize, cellSize - borderSize))
        pygame.draw.rect(screen, selected, (borderSize + padding + x * cellSize, borderSize + padding + 1 * cellSize, 2 * cellSize - borderSize, cellSize - borderSize))

def drawGrid():
    for x in range(padding, padding + gridWidth * cellSize, cellSize):
        for y in range(padding, padding + gridHeight * cellSize, cellSize):
            pygame.draw.line(screen, black, (x, y), (x + cellSize, y), borderSize) # top
            pygame.draw.line(screen, black, (x + cellSize, y), (x + cellSize, y + cellSize), borderSize) # right
            pygame.draw.line(screen, black, (x + cellSize, y + cellSize), (x, y + cellSize), borderSize) # bottom
            pygame.draw.line(screen, black, (x, y + cellSize), (x, y), borderSize) # left


print()
gridWidth = int(input("Enter the width of the 2*n grid: "))
print("Number of possibilities:", computeNumberPossibilities(gridWidth))
solutions = findAllPossibilities(gridWidth)
currentSolution = -1

width = gridWidth * cellSize + 2 * padding
height = 2 * padding + 2 * cellSize + 20
white = 255, 255, 255
black = 40, 40, 40
selected = 220, 220, 220
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Dominoes')

pygame.init()
pygame.font.init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            currentSolution += 1

    screen.fill(white)
    drawGrid()

    if currentSolution >= len(solutions):
        sys.exit()
    if currentSolution >= 0:
        for domino in solutions[currentSolution]:
            selectDomino(domino[1], domino[0])
    
    pygame.display.flip()