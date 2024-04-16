from random import choice, randint

import pygame

WIDTH = 1000
HEIGHT = 866
FPS = 60
WHITE = "#ecf0f1"
BLACK = "#121212"
RED = "#e74c3c"
BLUE = "#3498db"
YELLOW = "#f1c40f"
GREEN = "#2ecc71"
PURPLE = "#9b59b6"
ORANGE = "#e67e22"
AQUA = "#12CBC4"
PINK = "#FDA7DF"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


startPointsTri = [(WIDTH // 2, 0), (0, HEIGHT), (WIDTH, HEIGHT)]
startPointsSqu = [
    (0, 0),
    (WIDTH, 0),
    (0, WIDTH),
    (WIDTH, WIDTH),
]
startPointsCar = [
    (0, 0),
    (WIDTH, 0),
    (0, WIDTH),
    (WIDTH, WIDTH),
    (WIDTH // 2, 0),
    (WIDTH // 2, WIDTH),
    (0, WIDTH // 2),
    (WIDTH, WIDTH // 2),
]
startPointsPen = [
    (WIDTH // 2, 0),
    (0, WIDTH * 0.363),
    (WIDTH, WIDTH * 0.363),
    (WIDTH * 0.191, WIDTH * 0.951),
    (WIDTH - WIDTH * 0.191, WIDTH * 0.951),
]


def makePointTri(prevPoint):
    targetPoint = randint(0, 2)
    color = WHITE
    match targetPoint:
        case 0:
            target = startPointsTri[0]
            color = RED
        case 1:
            target = startPointsTri[1]
            color = BLUE
        case 2:
            target = startPointsTri[2]
            color = YELLOW

    xDist = target[0] - prevPoint[0]
    yDist = target[1] - prevPoint[1]

    return (prevPoint[0] + xDist // 2, prevPoint[1] + yDist // 2), color


def makePointSqu(prevPoint, lastTarget):
    targetPoint = lastTarget
    while targetPoint == lastTarget:
        targetPoint = randint(0, 3)

    color = WHITE
    match targetPoint:
        case 0:
            target = startPointsSqu[0]
            color = RED
        case 1:
            target = startPointsSqu[1]
            color = BLUE
        case 2:
            target = startPointsSqu[2]
            color = YELLOW
        case 3:
            target = startPointsSqu[3]
            color = GREEN

    # color = choice([RED, BLUE, YELLOW])

    xDist = target[0] - prevPoint[0]
    yDist = target[1] - prevPoint[1]

    return (prevPoint[0] + xDist // 2, prevPoint[1] + yDist // 2), color, targetPoint


def makePointCar(prevPoint):
    targetPoint = randint(0, 7)

    color = WHITE
    match targetPoint:
        case 0:
            target = startPointsCar[0]
            color = RED
        case 1:
            target = startPointsCar[1]
            color = BLUE
        case 2:
            target = startPointsCar[2]
            color = YELLOW
        case 3:
            target = startPointsCar[3]
            color = GREEN
        case 4:
            target = startPointsCar[4]
            color = PURPLE
        case 5:
            target = startPointsCar[5]
            color = ORANGE
        case 6:
            target = startPointsCar[6]
            color = AQUA
        case 7:
            target = startPointsCar[7]
            color = PINK

    # color = choice([RED, BLUE, YELLOW])

    xDist = target[0] - prevPoint[0]
    yDist = target[1] - prevPoint[1]

    return (prevPoint[0] + xDist * 2 / 3, prevPoint[1] + yDist * 2 / 3), color


def makePointPen(prevPoint, lastTarget):
    targetPoint = lastTarget
    while targetPoint == lastTarget:
        targetPoint = randint(0, 4)

    color = WHITE
    match targetPoint:
        case 0:
            target = startPointsPen[0]
            color = RED
        case 1:
            target = startPointsPen[1]
            color = BLUE
        case 2:
            target = startPointsPen[2]
            color = YELLOW
        case 3:
            target = startPointsPen[3]
            color = GREEN
        case 4:
            target = startPointsPen[4]
            color = PURPLE

    # color = choice([RED, BLUE, YELLOW])

    xDist = target[0] - prevPoint[0]
    yDist = target[1] - prevPoint[1]

    r = 0.5
    return (prevPoint[0] + xDist * r, prevPoint[1] + yDist * r), color, targetPoint


def makePointSta(prevPoint, lastTarget, twoInRow):
    if twoInRow:
        print("2")
        twoInRow = False
        targetPoint = randint(0, 4)
        left = targetPoint - 1
        if left < 0:
            left = 4
        right = targetPoint + 1
        if right > 4:
            right = 0
        while left == lastTarget or right == lastTarget:
            targetPoint = randint(0, 4)
            left = targetPoint - 1
            if left < 0:
                left = 4
            right = targetPoint + 1
            if right > 4:
                right = 0
    else:
        targetPoint = randint(0, 4)
        twoInRow = False
        if targetPoint == lastTarget:
            twoInRow = True

    color = WHITE
    match targetPoint:
        case 0:
            target = startPointsPen[0]
            color = RED
        case 1:
            target = startPointsPen[1]
            color = BLUE
        case 2:
            target = startPointsPen[2]
            color = YELLOW
        case 3:
            target = startPointsPen[3]
            color = GREEN
        case 4:
            target = startPointsPen[4]
            color = PURPLE

    # color = choice([RED, BLUE, YELLOW])

    xDist = target[0] - prevPoint[0]
    yDist = target[1] - prevPoint[1]

    r = 0.5
    return (
        (prevPoint[0] + xDist * r, prevPoint[1] + yDist * r),
        color,
        targetPoint,
        twoInRow,
    )


def main(screen):
    run = True
    screen.fill(BLACK)
    shape = "Tri"
    prevPoint = (WIDTH // 4, HEIGHT // 2)
    lastTarget = 0
    twoInRow = False
    pointColor = WHITE
    # for point in startPoints:
    #     pygame.draw.circle(screen, RED, point, 10)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    shape = "Tri"
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    screen.fill(BLACK)
                elif event.key == pygame.K_2:
                    shape = "Squ"
                    screen = pygame.display.set_mode((WIDTH, WIDTH))
                    screen.fill(BLACK)
                elif event.key == pygame.K_3:
                    shape = "Car"
                    screen = pygame.display.set_mode((WIDTH, WIDTH))
                    screen.fill(BLACK)
                elif event.key == pygame.K_4:
                    shape = "Pen"
                    screen = pygame.display.set_mode((WIDTH, WIDTH))
                    screen.fill(BLACK)
                elif event.key == pygame.K_5:
                    shape = "Sta"
                    screen = pygame.display.set_mode((WIDTH, WIDTH * 0.951))
                    screen.fill(BLACK)

        if shape == "Tri":
            prevPoint, pointColor = makePointTri(prevPoint)
        elif shape == "Squ":
            prevPoint, pointColor, lastTarget = makePointSqu(prevPoint, lastTarget)
        elif shape == "Car":
            prevPoint, pointColor = makePointCar(prevPoint)
        elif shape == "Pen":
            prevPoint, pointColor, lastTarget = makePointPen(prevPoint, lastTarget)
        elif shape == "Sta":
            prevPoint, pointColor, lastTarget, twoInRow = makePointSta(
                prevPoint, lastTarget, twoInRow
            )

        pygame.draw.circle(screen, pointColor, (prevPoint), 1)
        pygame.display.update()
        # clock.tick(FPS)


main(screen)
