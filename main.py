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
    def __init__(self, gun, player=Entity()):
        super().__init__()

        self.parent = gun
        self.model='cube'
        self.scale=.1
        self.world_parent = scene
        self.rotation_x = 185
        self.animate_position(self.position + (self.forward * 200), curve = linear, duration=3)

        destroy(self, delay=3)
        gun.blink(color.red)

class Gun(Entity):
    def __init__(self, model='cube', rotation=(0, 0, 0), position=(0,0,0)):
        super().__init__()
        self.model=model
        self.texture = 'white_cube'
        self.scale=.5
        self.bullet = Bullet(gun=self)
        self.rotation = rotation
        self.position= position

map1 = load_texture('fps shooter assets/map1.png')
cottage1 = Entity(model=load_model('fps shooter assets/Cottage_FREE.obj'), collider='mesh', x=20)
Entity(model='plane', scale=150, collider='box',texture = map1)

gun = Gun(model='fps shooter assets/Gun.obj', rotation=(0, 160, 0), position=(0,0,10))
player = Player(gun=gun)
bullet = Bullet(gun=gun, player=player)

def input(key):
    if key == 'left mouse down' and player.gun:
        Bullet(gun=gun)

app.run()
