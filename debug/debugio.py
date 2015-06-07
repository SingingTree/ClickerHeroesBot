import win32gui, win32con
import debug


debug_mouse_clickstorm_coord_check_hot_key_id = 101
debug_print_mouse_pos_hot_key_id = 110


def handle_msg(msg):
    if msg[2] == debug_print_mouse_pos_hot_key_id:
        print(win32gui.GetCursorPos())
    elif msg[2] == debug_mouse_clickstorm_coord_check_hot_key_id:
        debug.check_clickstorm_location()


def setup_debug_hotkeys():
    win32gui.RegisterHotKey(None, debug_mouse_clickstorm_coord_check_hot_key_id, win32con.MOD_ALT, 0x31) # 1 key
    win32gui.RegisterHotKey(None, debug_print_mouse_pos_hot_key_id, win32con.MOD_ALT, 0x50) # P key