# pip install sympy
from sympy import *

# 计算屏幕尺寸长宽(cm)
sizes = [13.3,14.0,15.6,16.0,17.3]

# 长宽比例
ratios = [{"key":"16/9", "value":16/9},{"key":"16/10", "value":16/10},{"key":"3/2", "value":3/2} ]

# 1英寸 = 2.54 cm
toCm = 2.54

# 开始计算
for size in sizes:
    diagonal = size*toCm
    for ratio in ratios:
        x = Symbol('x')
        result = solve(x**2 + (x*ratio["value"])**2 - diagonal**2, x)
        width = result[-1]
        print("{}寸{}笔记本 长为{}cm 宽为{}cm".format(size, ratio["key"], round(width*ratio["value"],2), round(width,2)))
