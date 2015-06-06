import win32gui
import debug

debug_print_mouse_coord_check_hot_key_id = 101
debug_print_mouse_pos_hot_key_id = 102

def handle_msg(msg):
    if msg[2] == debug_print_mouse_pos_hot_key_id:
        print(win32gui.GetCursorPos())
    elif msg[2] == debug_print_mouse_coord_check_hot_key_id:
        debug.check_mouse_locations()

def setup_debug_hotkeys():
    win32gui.RegisterHotKey(None, debug_print_mouse_coord_check_hot_key_id, 0, 0x4D) # M key
    win32gui.RegisterHotKey(None, debug_print_mouse_pos_hot_key_id, 0, 0x50) # P key