import arcade


WIDTH = 700
HEIGHT = 600


class Ball:
    def __init__(self, radius=20, velocity=70, initial_x=20):
        self.x_position = initial_x
        self.velocity = velocity
        self.radius = radius


def setup_my_game():
    global ball
    ball = Ball()


def draw_the_ball():
    arcade.draw_circle_filled(ball.x_position, HEIGHT // 2, ball.radius, arcade.color.GREEN)


def draw_some_text():
    arcade.draw_text("This is some text.", 10, HEIGHT // 2, arcade.color.BLACK, 20)


@arcade.override
def update(delta_time):
    ball.x_position += ball.velocity * delta_time

    # Did the ball hit the right side of the screen while moving right?
    if ball.x_position > WIDTH - ball.radius and ball.velocity > 0:
        ball.velocity *= -1

    # Did the ball hit the left side of the screen while moving left?
    if ball.x_position < ball.radius and ball.velocity < 0:
        ball.velocity *= -1


@arcade.override
def on_draw():
    arcade.start_render()
    draw_the_ball()
    draw_some_text()


@arcade.override
def on_key_press(key, key_modifiers):
    if key == arcade.key.SPACE:
        print("You pressed the space bar.")


if __name__ == "__main__":
    setup_my_game()
    arcade.decorator_run(WIDTH, HEIGHT, background_color=arcade.color.MAHOGANY)
