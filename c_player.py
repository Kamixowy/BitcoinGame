import pygame


class Player:
    color = 'red'
    just_jump = False
    jump_Speed = -10


    def __init__(self, pos_x, pos_y):
        self.just_Speed = 0
        self.velocity_y = 0
        self.gravity_force = 0.5
        self.on_ground = False
        self.hitbox = pygame.Rect(pos_x, pos_y, 50, 50)

    def _draw(self, screen):
        pygame.draw.rect(screen, self.color, self.hitbox)

    def _move_in_direction_x(self, move_x, floor):
        self.hitbox.x += move_x
        for ob in floor:
            if self.hitbox.colliderect(ob.hitbox):
                if move_x > 0:
                    self.hitbox.right = ob.hitbox.left
                if move_x < 0:
                    self.hitbox.left = ob.hitbox.right
    def _move_in_direction_y(self, floor):
        self.hitbox.y += self.velocity_y
        for ob in floor:
            if self.hitbox.colliderect(ob.hitbox):
                if self.velocity_y > 0:  # Falling
                    self.hitbox.bottom = ob.hitbox.top
                    self.velocity_y = 0
                    self.on_ground = True  # Gracz jest na ziemi lub platformie
                elif self.velocity_y < 0:  # Jumping
                    self.hitbox.top = ob.hitbox.bottom
                    self.velocity_y = 0
    def move(self, move_x, floor):
        if move_x != 0:
            self._move_in_direction_x(move_x, floor)

    def apply_gravity(self, floor):
        self.velocity_y += self.gravity_force
        self.on_ground = False  # Zakłada, że gracz jest w powietrzu, dopóki nie zostanie to zweryfikowane
        self._move_in_direction_y(floor)

    def jump(self):
        if self.on_ground:
            self.velocity_y += self.jump_Speed
            self.on_ground = False

    def update(self, screen, floor):
        self.apply_gravity(floor)
        self._draw(screen)
