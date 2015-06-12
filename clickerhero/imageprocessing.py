import cv2
import numpy as np
from matplotlib import pyplot as plt


def capture_screenshot():
    return None


def locate_fish_in_screen_shot(screen_shot):
    screen_shot2 = screen_shot.copy()
    template = cv2.imread('img/Fish.png')

    template_width, template_height, template_depth  = template.shape

    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        screen_shot = screen_shot2.copy()
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(screen_shot,template,method)
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

img = cv2.imread('img/FishOnScreen.png')
locate_fish_in_screen_shot(img)