import cv2
import numpy as np
from matplotlib import pyplot as plt


def pixel_differences(img, template):
    difference = 0.0
    for img_row, template_row in zip(img, template):
        for img_col, template_col in zip(img_row, template_row):
            normalised_template_alpha = template_col[3] / 255.0
            pixel_difference = abs(int(img_col[0]) - int(template_col[0]))
            pixel_difference += abs(int(img_col[1]) - int(template_col[1]))
            pixel_difference += abs(int(img_col[2]) - int(template_col[2]))
            # transparent parts of the tempalte aren't weighted as heavily
            pixel_difference *= normalised_template_alpha
            difference += pixel_difference
    return difference


#img = cv2.imread('img/FishOnScreen.png', cv2.IMREAD_UNCHANGED)
img = cv2.imread('img/FishOnScreen.png')

img2 = img.copy()
# template = cv2.imread('img/Fish.png', cv2.IMREAD_UNCHANGED)
template = cv2.imread('img/Fish.png')

img_width, img_height, img_depth = img.shape
template_width, template_height, template_depth  = template.shape
#
# min_pixel_difference = pixel_differences(img, template)
# min_difference_top_left = (0, 0)
# row = 0
# col = 1
# while(row + template_height < img_height):
#     while(col + template_width < img_width):
#         pixel_difference = pixel_differences(img[row:, col:], template)
#         if pixel_difference < min_pixel_difference:
#             min_pixel_difference = pixel_difference
#             min_difference_top_left = (col, row)
#         col += 1
#         print("process col")
#     row += 1
#
#
# img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
# template= cv2.cvtColor(template, cv2.COLOR_BGRA2RGBA)
#
# plt.imshow(img)
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + template_width, top_left[1] + template_height)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()
