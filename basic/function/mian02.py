# -*- coding: utf-8 -*-
"""
    @Author:    Niko
    @Date:      20220625
    @Tips:      函数-指定函数参数类型和返回值类型
"""

# 指定 参数和返回值类型


def test(a: int, b: int) -> int:
    return a + b


# 无返回值，不写 或者 None
def test1() -> None:
    print(9527)


if __name__ == '__main__':
    print(test(1, 2))
    test1()
