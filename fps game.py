from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
map1 = load_texture('fps shooter assets/map1.png')
Entity(model='plane', scale=150, collider='box',texture = map1)
FirstPersonController()
app.run()
