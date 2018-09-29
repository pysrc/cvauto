## 基于Opencv识别的GUI自动化操作

eg. 对于win10的计算器操作（详见examples/win10calc）

```python
import cvauto.auto as auto

a = auto.Auto()
a.click("5.png")
a.click("+.png")
a.click("7.png")
a.click("=.png")

```

![](examples/win10calc/win10calc.gif)

