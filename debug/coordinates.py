import sys
import win32gui
import clickerhero


def check_clickstorm_location():
    clicker_heroes_handle = (clickerhero.get_clicker_heroes_window_handle())
    if clicker_heroes_handle == 0:
        print("Could not obtain handle for clicker hero window, exiting")
        sys.exit()
    game_area_rect = clickerhero.get_game_area_rect(clicker_heroes_handle)
    x, y = clickerhero.get_clickstorm_pos(game_area_rect)
    clickerhero.move_cursor(int(x), int(y))


def print_coordinate_debug():
    clicker_heroes_handle = (clickerhero.get_clicker_heroes_window_handle())
    if clicker_heroes_handle == 0:
        print("Could not obtain handle for clicker hero window, exiting")
        sys.exit()
    game_area_rect = clickerhero.get_game_area_rect(clicker_heroes_handle)
    mouse_pos =  win32gui.GetCursorPos()
    game_width = game_area_rect[2] - game_area_rect[0]
    game_height = game_area_rect[3] - game_area_rect[1]
    curosor_location_as_percentage_of_active_game_area = ((mouse_pos[0] - game_area_rect[0]) / float(game_width),
                                                          (mouse_pos[1] - game_area_rect[1]) / float(game_height))
    print("Cursor at: " + str(mouse_pos))
    print("Game active rect: " + str(game_area_rect))
    print("Cursor position as percentage of window size: " + str(curosor_location_as_percentage_of_active_game_area))
