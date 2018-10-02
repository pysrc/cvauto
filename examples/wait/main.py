from cvauto.position import KeyType
from cvauto import auto
key = KeyType("7.png")
a = auto.Auto()
print(a.waitShow(key, delay=-1))
print(a.waitHide(key, delay=-1))
