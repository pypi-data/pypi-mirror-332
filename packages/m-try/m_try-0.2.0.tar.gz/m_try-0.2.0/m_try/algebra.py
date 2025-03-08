# algebra.py - 处理代数运算
def solve_linear_equation(a, b):
    """ 解决线性方程 ax + b = 0，返回 x """
    if a == 0:
        raise ValueError("a 不能为 0")
    return -b / a