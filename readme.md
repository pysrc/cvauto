## 基于Opencv识别的GUI自动化操作

以下Demo均为win10下的计算器软件操作，其他软件同理


## click

点击操作示例（[Demo](examples/click)）

```python
import cvauto.auto as auto

a = auto.Auto()
a.click("5.png")
a.click("+.png")
a.click("7.png")
a.click("=.png")

```

![](examples/click/win10calc.gif)

## wait**

等待控件加载/消失示例([Demo](examples/wait))

```python
from cvauto import auto
a = auto.Auto()
print(a.waitShow("7.png", delay=-1))
print(a.waitHide("7.png", delay=-1))

```

![](examples/wait/wait.gif)
