# -*- coding: utf-8 -*-
"""
    @Author:    Niko
    @Date:      20220625
    @Tips:      函数-动态参数
"""


# *args

def test(*args):
    print(args)
    print(type(args))


def add(*args) -> int:
    total = 0
    for arg in args:
        total += arg
    print(total)
    return total


# kwargs
def test2(**kwargs):
    print(kwargs)
    print(type(kwargs))


def test3(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


if __name__ == '__main__':
    test(1, 2, 3)
    add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print("*"*20)
    test2(user_name="Niko", age=18)
    print("*"*20)
    tem_dict = dict(
        user_name='Niko',
        age=18,
        phone_no='18600000000'
    )
    test3(**tem_dict)
