import os
import random
import arcade

WIDTH = 800
HEIGHT = 600


class MyTestWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.WHITE)

        # create the canvas
        canvas = arcade.Canvas(width=100, height=150, bg_color=arcade.color.RED)

        # Draw green boxes, bottom left on the canvas
        canvas.draw_xywh_rectangle_filled(0, 0, 5, 5, arcade.color.GREEN)
        canvas.draw_xywh_rectangle_filled(10, 10, 5, 5, arcade.color.GREEN)
        canvas.draw_xywh_rectangle_filled(20, 0, 5, 5, arcade.color.GREEN)

        # Draw ball on top right of canvas
        canvas.draw_circle_filled(canvas.width-30, canvas.height-30, 30, arcade.color.BLUE)

        # get the canvas as an arcade.Texture
        primitive_texture = canvas.texture

        # create a list of sprites that use the primitive shape texture
        self.sprites = arcade.SpriteList()
        for _ in range(100):
            x = random.randrange(0, WIDTH)
            y = random.randrange(0, HEIGHT)
            dx = random.randrange(-2, 2)
            dy = random.randrange(-2, 2)
            sprite = arcade.Sprite(center_x=x, center_y=y)
            sprite.velocity = [dx, dy]

            # use the canvas texture as the sprite's texture
            sprite.texture = primitive_texture
            sprite.scale = 0.3
            self.sprites.append(sprite)

    def update(self, delta_time):
        self.sprites.update()

    def on_draw(self):
        arcade.start_render()
        self.sprites.draw()


def test_sprite():
    window = MyTestWindow(WIDTH, HEIGHT, "Test Text")
    window.test(frames=60)
    window.close()
