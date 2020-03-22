import arcade

class Player(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super(Player, self).__init__(filename, sprite_scaling)
        self.leave = 100
    def update(self):
        pass