import ctypes
import win32gui, win32con
import time
import clickerhero


def bot_loop():
    clicker_heroes_handle = (clickerhero.get_clicker_heroes_window_handle())
    if clicker_heroes_handle == 0:
        print("Could not obtain handle for clicker hero window, exiting")
        return False
    _, _, (x, y) = win32gui.GetCursorInfo()
    print("Cursor: " + str(x) + " " + str(y))
    print("Window rect: " + str(win32gui.GetWindowRect(clicker_heroes_handle)))
    print("Game areas: " + str(clickerhero.get_active_game_area(clicker_heroes_handle)))
    return True


def check_for_input():
    keep_running = True
    status, msg = win32gui.PeekMessage(None, 0, 0, win32con.PM_REMOVE)
    while status > 0:
        if msg[1] == win32con.WM_HOTKEY:
            print("Got F11, quitting")
            keep_running = False
        win32gui.TranslateMessage(msg)
        win32gui.DispatchMessage(msg)
        if not keep_running:
            break
        status, msg = win32gui.PeekMessage(None, 0, 0, win32con.PM_REMOVE)

    return keep_running


def main():
    running = True
    win32gui.RegisterHotKey(None, 1, 0, win32con.VK_F11)
    try:
        while running:
            if not bot_loop():
                return
            if not check_for_input():
                return
            time.sleep(1)
    finally:
        ctypes.windll.user32.UnregisterHotKey(None, 1) #win32gui doesn't expose this
if __name__ == '__main__':
    main()