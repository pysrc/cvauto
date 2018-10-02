import cv2
from .position import Position
from .position import KeyType
from pyautogui import prompt
import numpy
import os


class SelectPoint(object):
    def __init__(self, keysrc: str):
        self._pos = Position()
        self._ico = cv2.imread(keysrc)
        self._key = KeyType(keysrc, 0, 0)
        self._im = self._pos.getScreenshot()
        self._posr = self._pos.getPosition(self._key)
        cv2.rectangle(self._im, (self._posr[0][0], self._posr[0][1]), (
            self._posr[0][0] + self._ico.shape[1], self._posr[0][1] + self._ico.shape[0]), (0, 0, 255), 1)

    def _click_event(self, event, x, y, flags, *param):
        if event == cv2.EVENT_LBUTTONDOWN:
            im2 = numpy.copy(self._im)
            cv2.circle(im2, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow(self._key.keysrc, im2)
            prompt("", "dx and dy", "dx = %d, dy = %d" % (
                x - self._posr[0][0], y - self._posr[0][1]))

    def go(self):
        cv2.imshow(self._key.keysrc, self._im)
        cv2.setMouseCallback(self._key.keysrc, self._click_event)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


class Generate(object):
    def __init__(self, keysrc: str):
        self._pos = Position()
        self._ico = cv2.imread(keysrc)
        self._key = KeyType(keysrc, 0, 0)
        self._im = self._pos.getScreenshot()
        self._posr = self._pos.getPosition(self._key)
        self._i = 0
        if not os.path.exists("keys.py"):
            with open("keys.py", 'a') as f:
                f.write("from cvauto.position import KeyType\n\nkeys = {}\n")
        else:
            from keys import keys
        cv2.rectangle(self._im, (self._posr[0][0], self._posr[0][1]), (
            self._posr[0][0] + self._ico.shape[1], self._posr[0][1] + self._ico.shape[0]), (0, 0, 255), 1)
        x, y = self._posr[0][0], self._posr[0][1]
        for key in keys:
            pos = (x + keys[key].dx, y + keys[key].dy)
            cv2.circle(self._im, pos, 5, (0, 0, 255), -1)
            cv2.putText(self._im, key, pos,
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

    def _click_event(self, event, x, y, flags, *param):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(self._im, (x, y), 5, (0, 0, 255), -1)
            k = prompt("Input key", "Key")
            if k == '':
                k = "key" + str(self._i)
                self._i += 1
            dx, dy = x - self._posr[0][0], y - self._posr[0][1]
            print(dx, dy)
            with open("keys.py", "a") as f:
                f.write(('keys["%s"] = KeyType("' + self._key.keysrc +
                         '", dx=%d, dy=%d)\n') % (k, dx, dy))
            cv2.putText(self._im, k, (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
            cv2.imshow(self._key.keysrc, self._im)

    def go(self):
        cv2.imshow(self._key.keysrc, self._im)
        cv2.setMouseCallback(self._key.keysrc, self._click_event)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
