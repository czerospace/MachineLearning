# -*- coding: utf-8 -*-
"""
    @Author:    Niko
    @Date:      20220625
    @Tips:      函数
"""

# 定义一个函数


def test_hello_world():
    print("hello world")

# 调用函数


test_hello_world()


# 带参函数

def num_sum(a, b):
    return a + b


res = num_sum(1, 2)
print(res)

# 函数支持多返回值


def back_some(a, b):
    return a, b


tem_a, tem_b = back_some(1, 2)
print(tem_a, tem_b)


def print_something(content):
    print("拼接的值是->{}".format(content))


print_something("你好")


def sum_count():
    total_sum = 0
    for index in range(1, 101):
        total_sum += index
    print(total_sum)


sum_count()
