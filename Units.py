import arcade

class Player(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super(Player, self).__init__(filename, sprite_scaling)
        self.leave = 100

    def update(self):
        pass

    def draw(self):
         draw_circle_outline(self.center_x, self.center_y, 18, arcade.color.RED, 3)


class Wolf(arcade.Sprite):
    def __init__(self, filename, prite_scaling):
        super(Player, self).__init__(filename, sprite_scaling)
        self.leave = 100

    def update(self):
        pass