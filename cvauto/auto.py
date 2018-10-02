from .position import Position
from .position import KeyType
import pyautogui
import time


class Auto(Position):
    def __init__(self):
        super(Auto, self).__init__()

    def _mouse(self, func, key: KeyType, min_sim=0.5, **kwargs):
        poss = self.getPosition(key)
        if poss is None or poss[1] < min_sim:
            return False
        func(*poss[0], **kwargs)
        return True

    def click(self, key: KeyType, min_sim=0.5, **kwargs):
        return self._mouse(pyautogui.click, key, min_sim, **kwargs)

    def doubleClick(self, key: KeyType, min_sim=0.5, **kwargs):
        return self._mouse(pyautogui.doubleClick, key, min_sim, **kwargs)

    def mouseDown(self, key: KeyType, min_sim=0.5, **kwargs):
        return self._mouse(pyautogui.mouseDown, key, min_sim, **kwargs)

    def mouseUp(self, key: KeyType, min_sim=0.5, **kwargs):
        return self._mouse(pyautogui.mouseUp, key, min_sim, **kwargs)

    def moveTo(self, key: KeyType, min_sim=0.5, **kwargs):
        return self._mouse(pyautogui.moveTo, key, min_sim, **kwargs)

    def middleClick(self, key: KeyType, min_sim=0.5, **kwargs):
        return self._mouse(pyautogui.middleClick, key, min_sim, **kwargs)

    def rightClick(self, key: KeyType, min_sim=0.5, **kwargs):
        return self._mouse(pyautogui.rightClick, key, min_sim, **kwargs)

    def tripleClick(self, key: KeyType, min_sim=0.5, **kwargs):
        return self._mouse(pyautogui.tripleClick, key, min_sim, **kwargs)

    def typewrite(self, key: KeyType, message="", min_sim=0.5, **kwargs):
        self.click(key, min_sim, **kwargs)
        pyautogui.typewrite(message, **kwargs)

    def isShow(self, key: KeyType, min_sim=0.5):
        """
            key对应的区域是否显示
        """
        poss = self.getPosition(key)
        if poss is None or poss[1] < min_sim:
            return False
        return True

    def waitShow(self, key: KeyType, min_sim=0.5, delay=10):
        """
            等待key区域显示，最多等待dalay秒，delay为-1时为一直等待
        """
        start = time.time()
        while delay == -1 or time.time() - start <= delay:
            if self.isShow(key, min_sim):
                return True
        return False

    def waitHide(self, key: KeyType, min_sim=0.5, delay=10):
        '''
            等待key消失
        '''
        start = time.time()
        while delay == -1 or time.time() - start <= delay:
            if not self.isShow(key, min_sim):
                return True
        return False
