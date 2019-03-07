import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    """ Draw a snow person """

    # Snow
    arcade.draw_circle_filled(x, y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y + 50, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y + 100, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(y - 15, y + 50, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(y + 15, y + 50, 5, arcade.color.BLACK)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    draw_grass()
    draw_snow_person(100,100)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()