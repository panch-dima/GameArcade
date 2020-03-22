import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SPRITE_SCALING = 2
MOVEMENT_SPEED = 1



class Player(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super(Player, self).__init__(filename, sprite_scaling)
        self.leave = 100
    def 



class MyGame(arcade.Window):
    """ Главный класс приложения. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.COOL_GREY)

    def setup(self):
        # Настроить игру здесь


        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.eat_list = arcade.SpriteList()
        self.walls_list = arcade.SpriteList()

        self.wall_sprite = arcade.Sprite("images/wall.png", SPRITE_SCALING)


        for i in range(100):
            self.eat_sprite = arcade.Sprite("images/eat.png", SPRITE_SCALING)
            self.eat_sprite.center_x = random.randint(0, SCREEN_HEIGHT)
            self.eat_sprite.center_y = random.randint(0, SCREEN_WIDTH)
            self.eat_list.append(self.eat_sprite)

        self.player_sprite = Player("images/player.png", SPRITE_SCALING)
        #self.player_sprite = arcade.Sprite("images/player.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50  # Стартовая позиция
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.walls_list)

    def on_key_press(self, key, modifiers):
        """Вызывается при нажатии пользователем клавиши"""

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Вызывается, когда пользователь отпускает клавишу"""

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.eat_list.draw()
        # Здесь код рисунка

    def update(self, delta_time):
        self.physics_engine.update()
        """ Здесь вся игровая логика и логика перемещения."""
        eat_hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.eat_list)

        for eat in eat_hit_list:
            eat.kill()
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()