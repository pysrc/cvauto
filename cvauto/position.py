import cv2
import PIL
import numpy
from PIL import ImageGrab


class KeyType(object):
    def __init__(self, src: str, dx=None, dy=None):
        self.keysrc = src
        self.dx = dx
        self.dy = dy

    def __str__(self):
        return 'key: "%s", dx: %d, dy: %d' % (self.key, self.dx, self.dy)


class Position(object):
    def __init__(self):
        self._imap = {}  # 按钮/点击区域图标存放
        self._cache = {}  # 已经查找过的图像位置缓存
        self._use_cache = False  # 是否启用缓存，默认不启用

    def cacheSet(self, use=True):
        self._use_cache = use

    def getScreenshot(self):
        return cv2.cvtColor(numpy.asarray(
            ImageGrab.grab()), cv2.COLOR_RGB2BGR)

    def getPosition(self, key: KeyType, src=None, debug=False):
        '''
            返回图标在图像上的位置以及相似度
            @key Key类型
            @src 如果有，就从该图片上找位置
            @debug 如果为True则显示点击位置等信息
        '''
        keysrc, dx, dy = key.keysrc, key.dx, key.dy
        item = self._imap.get(keysrc)
        if item is None:
            self._imap[keysrc] = cv2.imread(keysrc)
            item = self._imap[keysrc]
        if self._use_cache:
            cacle_item = self._cache.get(keysrc)
            if cacle_item is not None:
                return cacle_item
        h, w = item.shape[0], item.shape[1]
        if dx is None:
            dx = w // 2
        if dy is None:
            dy = h // 2
        if src is not None:
            # 字符串就使用cv读
            if type(src) == str:
                src = cv2.imread(src)
            # Image对象就转换
            elif type(src) == PIL.Image.Image:
                src = cv2.cvtColor(numpy.asarray(src), cv2.COLOR_RGB2BGR)
        else:  # 取当前截图
            src = self.getScreenshot()
        img_match = cv2.minMaxLoc(
            cv2.matchTemplate(item, src, cv2.TM_CCOEFF_NORMED))
        x, y = img_match[3]
        pos = (x + dx, y + dy)
        if debug:
            print(img_match)
            cv2.rectangle(src, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.circle(src, pos, 5, (0, 0, 255), -1)
            cv2.imshow("res", src)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        sim = (img_match[1] - img_match[0]) / 2
        if self._use_cache:
            self._cache[keysrc] = (pos, sim)
        return (pos, sim)
