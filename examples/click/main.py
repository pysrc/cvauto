from cvauto.position import KeyType
import cvauto.auto as auto
keys = []
keys.append(KeyType("5.png"))
keys.append(KeyType("+.png"))
keys.append(KeyType("7.png"))
keys.append(KeyType("=.png"))

a = auto.Auto()

for i in keys:
    a.click(i)
