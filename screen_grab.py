from PIL import ImageGrab
from PIL import Image
import os
import time
import numpy as np


def screen_grab():
    box = (739, 201, 1368, 202)  # Text line
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')


def grab_textline():
    box = (739, 201, 1368, 202)  # Text line
    return ImageGrab.grab(box)


def process_textline(textline_image):
    tl = np.array(textline_image.convert('1')).squeeze()
    current_segment_len = 0
    white = True
    segments = []
    spaces = []
    char_index = 0
    for i in range(1, tl.size):
        if tl[i] != tl[i-1]:
            if white is True:
                if 12 <= current_segment_len <= 14:
                    spaces.append((char_index, i - current_segment_len, current_segment_len, True))
                    char_index += 1
                white = False
            else:
                segments.append((char_index, i - current_segment_len, current_segment_len, False))  # Index of segment start and length
                char_index += 1
                white = True
            current_segment_len = 0
        else:
            current_segment_len += 1
    word_length = char_index
    return segments, spaces, word_length


def define_boxes(segments):
    boxes = []
    for segment in segments:
        boxes.append((segment[1]-1, segment[0]))


def detect_newturn():
    pass


def main():
    tl = Image.open('tl_example2.png')
    segments, spaces, word_length = process_textline(tl)
    # screen_grab()
    print(segments)
    print(spaces)
    print(word_length)

if __name__ == '__main__':
    main()
