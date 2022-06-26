# -*- coding: utf-8 -*-
"""
    @Author:    Niko
    @Date:      20220625
    @Tips:      列表
"""

# 思考 ： test_array=[[1,2,3],[4,5,6],7,8,9] 输出所有数字
test_array = [[1, 2, 3], [4, 5, 6], 7, 8, 9]

for obj in test_array:
    if type(obj) == list:
        for second_obj in obj:
            print(second_obj)
    else:
        print(obj)

# 列表相加
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
# 预期: [1, 2, 3, 4, 5, 6]
print(c)

# 切片 包左不包右边
d = [7, 8, 9, 10]
# 预期: [7]
print(d[:1])
# 预期: [9,10]
print(d[2:])
