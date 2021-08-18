from ursina import *
from ursina.curve import linear
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

class Player(FirstPersonController):
    def __init__(self, gun):
        super().__init__()
        self.gun = gun
        self.gun.parent = self.camera_pivot
        self.gun.position = self.position + self.forward + (1, 0, 0)

class Bullet(Entity):
    def __init__(self, gun):
        super().__init__()

        self.parent = gun
        self.model='cube'
        self.scale=.1
        self.world_parent = scene
        self.animate_position(self.position + (self.forward * 50), curve = linear, duration=1)

        destroy(self, delay=1)
        gun.blink(color.red)

class Gun(Entity):
    def __init__(self):
        super().__init__()
        self.model='cube'
        self.texture = 'white_cube'
        self.scale=.5
        self.bullet = Bullet(gun=self)

map1 = load_texture('fps shooter assets/map1.png')
Entity(model='plane', scale=150, collider='box',texture = map1)

gun = Gun()
bullet = Bullet(gun=gun)
player = Player(gun=gun)

def input(key):
    if key == 'left mouse down' and player.gun:
        Bullet(gun=gun)

app.run()