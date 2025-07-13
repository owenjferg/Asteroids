from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shottimer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def rotate(self, dt):
        turn = PLAYER_TURN_SPEED * dt 
        self.rotation += turn
        return self.rotation
    def update(self, dt, shots):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(shots)
        self.shottimer -= dt
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def shoot(self, shots):
        if self.shottimer <= 0:
            shot = Shot(self.position.x, self.position.y)
            velocity = pygame.Vector2(0, 1)
            velocity = velocity.rotate(self.rotation)
            velocity = velocity * PLAYER_SHOOT_SPEED
            shot.velocity = velocity 
            shots.add(shot)
            self.shottimer += PLAYER_SHOOT_COOLDOWN
        else:
            print("Shooting on cooldown")
