import clickerhero
import cv2
import numpy
import pyscreenshot
from matplotlib import pyplot as plt
import time


def capture_screen_shot_of_region((left, top, right, bottom)):
    im = pyscreenshot.grab((left, top, right, bottom))
    return im


def convert_screen_shot_to_numpy_array(screen_shot):
    im = screen_shot.convert("RGB")
    return numpy.array(im)

def locate_fish_in_screen_shot(screen_shot):
    screen_shot2 = screen_shot.copy()
    screen_shot_height, _, _ = screen_shot.shape

    # Fish template is for 1920 * 1029 res, need to find the scale it should be sized to
    template_scale = screen_shot_height / 1029.0

    template = cv2.imread('img/Fish.png')
    template = cv2.resize(template, (0, 0), fx=template_scale, fy=template_scale)  # scale template
    template_height, template_width, _  = template.shape

    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        screen_shot = screen_shot2.copy()
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(screen_shot, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + template_width, top_left[1] + template_height)

        cv2.rectangle(screen_shot,top_left, bottom_right, 255, 2)

        plt.subplot(121),plt.imshow(res,cmap = 'gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(screen_shot,cmap = 'gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)

        plt.show()

time.sleep(1)
img = cv2.imread('img/FishOnScreen2.png')
im = capture_screen_shot_of_region(clickerhero.get_game_area_rect(clickerhero.get_clicker_heroes_window_handle()))
im = convert_screen_shot_to_numpy_array(im)
im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
locate_fish_in_screen_shot(im)