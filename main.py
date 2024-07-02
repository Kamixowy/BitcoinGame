import pygame
import c_floor
import c_player


pygame.init()

screen = pygame.display.set_mode((500, 540))
pygame.display.set_caption("BitcoinGame")

krok = 10
run = True
jump_allowed = True
clock = pygame.time.Clock()
floors = []
player = c_player.Player(0 ,400)

floors.append(c_floor.Floor(-25,500))
floors.append(c_floor.Floor(50,500))
floors.append(c_floor.Floor(100,450))
floors.append(c_floor.Floor(150,500))
floors.append(c_floor.Floor(200,500))

while run:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.move(-krok, floors)
    if keys[pygame.K_d]:
        player.move(krok, floors)
    if keys[pygame.K_SPACE]:
        if jump_allowed:
            player.jump()
            jump_allowed = False

    if player.on_ground:
        jump_allowed = True


    screen.fill((0, 0, 0))
    player.update(screen, floors)

    for floor in floors:
        floor.update(screen)

    pygame.display.update()