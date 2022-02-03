import numpy as np
import cv2
import pytesseract
import pyautogui

img = pyautogui.screenshot()
img = cv2.cvtColor(np.array(img),
                   cv2.COLOR_RGB2BGR)

def draw_boxes_on_text(img):
    # Return raw information about the detected texts
    raw_data = pytesseract.image_to_data(img)

    for count, data in enumerate(raw_data.splitlines()):
        if count > 0:
            data = data.split()
            if len(data) == 12:
                x, y, w, h, content = int(data[6]), int(data[7]), int(data[8]), int(data[9]), data[11]
                cv2.rectangle(img, (x, y), ( w +x, h+ y), (0, 255, 0), 1)
                # cv2.putText(img, content, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255) , 1)
    return img


img = draw_boxes_on_text(img)

# Show the Output
cv2.imshow("Output", img)
cv2.waitKey(0)
# texts = pytesseract.image_to_string(img)
# print(texts)
exit()

import tkinter as tk
from random import seed, choice
from string import ascii_letters

seed(42)

colors = ('red', 'yellow', 'green', 'cyan', 'blue', 'magenta')


def do_stuff():
    s = ''.join([choice(ascii_letters) for i in range(10)])
    color = choice(colors)
    l.config(text=s, fg=color)
    root.after(100, do_stuff)


root = tk.Tk()
root.wm_overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.bind("<Button-1>", lambda evt: root.destroy())

l = tk.Label(text='', font=("Helvetica", 60))
l.pack(expand=True)

do_stuff()
root.mainloop()
exit()