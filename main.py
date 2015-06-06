import ctypes
import win32gui, win32con
import time
import clickerhero
import debug

debug_mode = True

start_hot_key_id = 1
stop_hot_key_id = 2
quit_hot_key_id = 3

hold_steady_code = 0
start_code = 1
stop_code = 2
quit_code = 3

def spam_monster_clicks(game_area):
    monster_x, monster_y = clickerhero.get_monster_pos(game_area)
    clickerhero.move_cursor(int(monster_x), int(monster_y))
    clickerhero.spam_clicks_with_delay(50, 0.02)


def process_bot():
    clicker_heroes_handle = (clickerhero.get_clicker_heroes_window_handle())
    if clicker_heroes_handle == 0:
        print("Could not obtain handle for clicker hero window, exiting")
        return False
    _, _, (x, y) = win32gui.GetCursorInfo()
    game_area = clickerhero.get_game_area_rect(clicker_heroes_handle)
    spam_monster_clicks(game_area)
    # print(clickerhero.get_monster_click_pos(game_area))
    # print("Cursor: " + str(x) + " " + str(y))
    # print("Window rect: " + str(win32gui.GetWindowRect(clicker_heroes_handle)))
    # print("Game areas: " + str(clickerhero.get_active_game_area(clicker_heroes_handle)))
    return True


def check_for_input():
    status, msg = win32gui.PeekMessage(None, 0, 0, win32con.PM_REMOVE)
    while status > 0:
        if msg[1] == win32con.WM_HOTKEY:
            if msg[2] == start_hot_key_id:
                print("Got F6")
                return start_code
            elif msg[2] == stop_hot_key_id:
                print("Got F7")
                return stop_code
            elif msg[2] == quit_hot_key_id:
                print("Got F8, quitting")
                return quit_code
            else:
                if debug_mode:
                    debug.handle_msg(msg)
        win32gui.TranslateMessage(msg)
        win32gui.DispatchMessage(msg)
        status, msg = win32gui.PeekMessage(None, 0, 0, win32con.PM_REMOVE)
    return hold_steady_code


def main():
    program_start_time = time.clock()
    running = True
    paused = True
    win32gui.RegisterHotKey(None, start_hot_key_id, 0, win32con.VK_F6)
    win32gui.RegisterHotKey(None, stop_hot_key_id, 0, win32con.VK_F7)
    win32gui.RegisterHotKey(None, quit_hot_key_id, 0, win32con.VK_F8)
    # Register debug hotkeys
    if debug_mode:
        debug.setup_debug_hotkeys()
    try:
        while running:
            main_loop_start_clock = time.clock()
            if not paused:
                bot_loop_success = process_bot()
                if not bot_loop_success:
                    return
            input_result = check_for_input()
            if input_result == start_code:
                paused = False
            if input_result == stop_code:
                paused = True
            elif input_result == quit_code:
                return
            main_loop_end_clock = time.clock()
    finally:
        ctypes.windll.user32.UnregisterHotKey(None, start_hot_key_id)  # win32gui doesn't expose this
        ctypes.windll.user32.UnregisterHotKey(None, stop_hot_key_id)  # win32gui doesn't expose this
        ctypes.windll.user32.UnregisterHotKey(None, quit_hot_key_id)  # win32gui doesn't expose this
if __name__ == '__main__':
    main()
