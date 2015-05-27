import time
import win32api, win32con


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def move_cursor(x, y):
    win32api.SetCursorPos((x,y))


def spam_clicks_with_delay(num_clicks, delay):
    for i in range(0, num_clicks):
        click()
        time.sleep(delay)
