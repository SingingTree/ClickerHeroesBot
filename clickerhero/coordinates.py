import win32gui


def get_clicker_heroes_window_handle():
    return win32gui.FindWindow(None, "Clicker Heroes")


def get_active_game_area(window_handle):
    window_left, window_top, window_right, window_bottom = win32gui.GetWindowRect(window_handle)
    client_left, client_top, client_right, client_bottom = win32gui.GetClientRect(window_handle)

    window_width = window_right - window_left
    client_width = client_right
    border_width = (window_width - client_width) / 2

    window_height = window_bottom - window_top
    client_height = client_bottom
    header_height = window_height - client_height - border_width

    print(border_width)
    print(header_height)

    client_area_on_screen = (window_left + border_width, window_top + header_height,
                             window_right - border_width, window_bottom - border_width)

    # 16 : 9 ratio is used by the game, and will be letter-boxed to maintain it
    # lets figure out the actual game area on screen
    normalised_width = client_width / 16
    normalised_height = client_height / 9

    if normalised_width >  normalised_height:
        game_width = normalised_height * 16
        game_height = normalised_height * 9
    elif normalised_height > normalised_width:
        game_width = normalised_width * 16
        game_height = normalised_width * 9

    horizontal_letterbox_width = (client_width - game_width) / 2
    vertical_letterbox_height = (client_height - game_height) / 2

    game_area_on_screen = (client_area_on_screen[0] + horizontal_letterbox_width,
                           client_area_on_screen[1] + vertical_letterbox_height,
                           client_area_on_screen[2] - horizontal_letterbox_width,
                           client_area_on_screen[3] - horizontal_letterbox_width)

    return game_area_on_screen
