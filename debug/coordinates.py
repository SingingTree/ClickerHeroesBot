import clickerhero
import sys

def check_mouse_locations():
    clicker_heroes_handle = (clickerhero.get_clicker_heroes_window_handle())
    if clicker_heroes_handle == 0:
        print("Could not obtain handle for clicker hero window, exiting")
        sys.exit()
    game_area = clickerhero.get_game_area_rect(clicker_heroes_handle)
    x, y = clickerhero.get_clickstorm_pos(game_area)
    clickerhero.move_cursor(int(x), int(y))