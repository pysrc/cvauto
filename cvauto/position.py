import cv2
import PIL
import numpy
from PIL import ImageGrab


class Position(object):
    def __init__(self):
        self._imap = {}  # 按钮/点击区域图标存放
        self._cache = {}  # 已经查找过的图像位置缓存
        self._use_cache = False  # 是否启用缓存，默认不启用

    def cacheSet(self, use=True):
        self._use_cache = use

    def getPosition(self, key: str, src=None, debug=False):
        '''
            返回图标在图像上的位置以及相似度
            @key 图标别名
            @src 如果有，就从该图片上找位置
            @debug 如果为True则显示点击位置等信息
        '''
        item = self._imap.get(key)
        if item is None:
            self._imap[key] = cv2.imread(key)
            item = self._imap[key]
        if self._use_cache:
            cacle_item = self._cache.get(key)
            if cacle_item is not None:
                return cacle_item
        if src is not None:
            # 字符串就使用cv读
            if type(src) == str:
                src = cv2.imread(src)
            # Image对象就转换
            elif type(src) == PIL.Image.Image:
                src = cv2.cvtColor(numpy.asarray(src), cv2.COLOR_RGB2BGR)
        else:  # 取当前截图
            src = cv2.cvtColor(numpy.asarray(
                ImageGrab.grab()), cv2.COLOR_RGB2BGR)
        img_match = cv2.minMaxLoc(
            cv2.matchTemplate(item, src, cv2.TM_CCOEFF_NORMED))
        x, y = img_match[3]
        h, w = item.shape[0], item.shape[1]
        if debug:
            print(img_match)
            cv2.rectangle(src, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(src, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.circle(
                src, (int(x + w * 0.5), int(y + h * 0.5)),
                5, (0, 0, 255), -1)
            cv2.imshow("res", src)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        pos = (int(x + w * 0.5),
               int(y + h * 0.5))
        sim = (img_match[1] - img_match[0]) / 2
        if self._use_cache:
            self._cache[key] = (pos, sim)
        return (pos, sim)
