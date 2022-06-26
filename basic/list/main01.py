# -*- coding: utf-8 -*-
"""
    @Author:    Niko
    @Date:      20220625
    @Tips:      数组
"""
# 如何定义一个空数组
tmp_array = []
print(tmp_array)
print(type(tmp_array))

# 定义一个数组
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num_list)

# 数组下标  第 n 个元素的下标 = n - 1 比如第一个元素的下标 = 1 - 1 = 0
print(num_list[0])
print(num_list[5])

# 不同类型的元素可以放在一个数组里，但是一般不这么用
# 要把相数据类型的元素放在一个数组里
tmp_array1 = [1, "2", True]
print(tmp_array1)

print(tmp_array1[0]+1)
# print(tmp_array1[1]+1) 会报错

# 分割线
print("*" * 20)

tmp_array2 = ["北京", "上海", "广州", "深圳"]
# 数组长度
print(len(tmp_array2))
# 数组遍历
for city_name in tmp_array2:
    print(city_name)
