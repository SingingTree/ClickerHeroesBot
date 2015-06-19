import time
import win32api, win32con


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def click_message(window_handle, client_area_x, client_area_y):
    coordinates = (int(client_area_x) & 0xFFFF) + (int(client_area_y) << 16);
    win32api.SendMessage(window_handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, coordinates)
    win32api.SendMessage(window_handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, coordinates)


def move_cursor(x, y):
    win32api.SetCursorPos((x,y))


def spam_clicks_with_delay(num_clicks, delay):
    for i in range(0, num_clicks):
        click()
        time.sleep(delay)


def spam_click_messages_with_delay(window_handle, num_clicks, delay, client_area_x, client_area_y):
    for i in range(0, num_clicks):
        click_message(window_handle, client_area_x, client_area_y)
        time.sleep(delay)
