from cvauto.tools import Generate
import pyautogui

k = pyautogui.prompt("File", "Input file")
g = Generate(k)
g.go()
