# pip install sympy
from sympy import *

# 计算屏幕尺寸长宽(cm)
sizes = {
    13.3: "all",
    # mba 2022
    13.6: "16/10",
    14.0: "all",
    # mbp14
    14.2: "16/10",
    # yoga14pros 2022
    14.5: "16/10",
    # mbp15
    15.4: "16/10",
    15.6: "16/9",
    16.0: "all",
    # y9000x
    16.1: "16/10",
    # mbp16 2022
    16.2: "16/10",
    # lg-gram-17 2022
    17.2: "16/10",
    17.3: "16/9",
}

# 长宽比例
ratios = {
    "16/9": [16 / 9],
    "16/10": [16 / 10],
    "3/2": [3 / 2],
    "all": [16 / 9, 16 / 10, 3 / 2],
}
ratios_back = {16 / 9: "16/9", 16 / 10: "16/10", 3 / 2: "3/2"}

# 1英寸 = 2.54 cm
toCm = 2.54

# 开始计算
for size in sizes:
    diagonal = float(size) * toCm
    for ratio in ratios[sizes[size]]:
        x = Symbol("x")
        result = solve(x**2 + (x * ratio) ** 2 - diagonal**2, x)
        width = result[-1]
        print(
            "{}寸 比例{} 笔记本 长为{}cm 宽为{}cm".format(
                size, ratios_back[ratio], round(width * ratio, 2), round(width, 2)
            )
        )
