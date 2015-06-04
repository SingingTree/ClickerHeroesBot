import win32gui


def get_game_area_rect(window_handle):
    window_left, window_top, window_right, window_bottom = win32gui.GetWindowRect(window_handle)
    client_left, client_top, client_right, client_bottom = win32gui.GetClientRect(window_handle)

    window_width = window_right - window_left
    client_width = client_right
    border_width = (window_width - client_width) / 2

    window_height = window_bottom - window_top
    client_height = client_bottom
    header_height = window_height - client_height - border_width

    client_rect_on_screen = (window_left + border_width, window_top + header_height,
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
    else:
        game_width = normalised_width * 16
        game_height = normalised_height * 9

    horizontal_letterbox_width = (client_width - game_width) / 2
    vertical_letterbox_height = (client_height - game_height) / 2

    game_screen_coords_rect = (client_rect_on_screen[0] + horizontal_letterbox_width,
                               client_rect_on_screen[1] + vertical_letterbox_height,
                               client_rect_on_screen[2] - horizontal_letterbox_width,
                               client_rect_on_screen[3] - vertical_letterbox_height)

    return game_screen_coords_rect


def get_clickstorm_pos(game_area_rect):
    clickstorm_witdh_ratio = 0.535
    clickstorm_height_ratio = 0.267
    game_width = game_area_rect[2] - game_area_rect[0]
    game_height = game_area_rect[3] - game_area_rect[1]

    monster_x = game_width * clickstorm_witdh_ratio + game_area_rect[0]
    monster_y = game_height * clickstorm_height_ratio + game_area_rect[1]

    return monster_x, monster_y


def get_monster_pos(game_area_rect):
    monster_witdh_ratio = 0.75
    monster_height_ratio = 0.55
    game_width = game_area_rect[2] - game_area_rect[0]
    game_height = game_area_rect[3] - game_area_rect[1]

    monster_x = game_width * monster_witdh_ratio + game_area_rect[0]
    monster_y = game_height * monster_height_ratio + game_area_rect[1]

    return monster_x, monster_y


def get_clicker_heroes_window_handle():
    return win32gui.FindWindow(None, "Clicker Heroes")
