## 基于Opencv识别的GUI自动化操作

以下Demo均为win10下的计算器软件操作，其他软件同理


## click

点击操作示例（[Demo](examples/click)）

```python
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

```

![](examples/click/win10calc.gif)

## wait**

等待控件加载/消失示例([Demo](examples/wait))

```python
from cvauto.position import KeyType
from cvauto import auto
key = KeyType("7.png")
a = auto.Auto()
print(a.waitShow(key, delay=-1))
print(a.waitHide(key, delay=-1))
```

![](examples/wait/wait.gif)

## 关于点击位置

KeyType 有三个参数，分别为:

keysrc: 图标位置

dx: 实际点击位置离图标左上角位置的x方向相对像素长度

dy: 实际点击位置离图标左上角位置的y方向相对像素长度

默认情况下dx, dy为None，点击图标正中心

获取dx, dy可参考[这里](examples/preprocess)

```python
from cvauto import tools
t = tools.SelectPoint("7.png")
t.go()

```

