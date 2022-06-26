# -*- coding: utf-8 -*-
"""
    @Author:    Niko
    @Date:      20220625
    @Tips:      列表的常用操作 append,count,extend,insert,pop,remove,sort,del,in,list
"""

# 思考: 如何创建一个包含 1-100 的数组
# append 在某位追加
tmp_list1 = []
for index in range(1, 101):
    tmp_list1.append(index)
print(tmp_list1)

# count 统计某个元素在列表中出现的次数
tmp_list2 = ["to", "be", "or", "not", "to", "be"]
print(tmp_list2.count("to"))

# insert 将某个值插入到列表中的某个位置:
tmp_list2.insert(0, "100")  # 将 "100" 插入到下标为 0 的位置
# 预期: ['100', 'to', 'be', 'or', 'not', 'to', 'be']
print(tmp_list2)

print("*"*20)
# pop 移除列表的最后一个元素,并返回该元素的值:
resp = tmp_list2.pop()
print(resp)
print(tmp_list2)

print("*"*20)
# remove 移除列表中第一个匹配的元素,不会返回这个被移除的元素
tmp_list2.remove("to")
# 预期: ['100', 'be', 'or', 'not', 'to']
print(tmp_list2)

print("*"*20)
# 排序
# sorted 函数不会改变原来列表的位置，返回一个排序后的值
# sort 方法将列表中的元素进行排序，会改变原来列表中的位置,没有返回值
print(sorted([100, 1, 99, 2]))

tmp_list3 = [100, 1, 99, 2]
# 默认从小到大排序
tmp_list3.sort()
print(tmp_list3)
# 从大到小
tmp_list3.sort(reverse=True)
print(tmp_list3)

print("*"*20)
# del 关键字: 根据下标删除元素:
print(tmp_list2)
del tmp_list2[0]  # 删除第一个元素
print(tmp_list2)

print("*"*20)
# 使用 in 判断列表中是否有某个元素
if "be" in tmp_list2:
    print("be 在 tmp_list2 中")
else:
    print("be 不在 tmp_list2 中")


print("*"*20)
# `list` 函数:将其他数据类型转换成列表:
tmp_str = "python"
new_list = list(tmp_str)
print(type(tmp_str))
print(type(new_list))
print(new_list)  # ['p', 'y', 't', 'h', 'o', 'n']


print("*"*20)
# 字符串转数组
tmp_str1 = "1~2~3~4~5"
print(tmp_str1)
print(type(tmp_str1))

tmp_list4 = tmp_str1.split("~")
print(type(tmp_list4))
print(tmp_list4)

print("*"*20)
# int 类型数组转字符串
tmp_list5 = [1, 2, 3, 4, 5]
res_str = ','.join(str(obj) for obj in tmp_list4)
print(res_str)
print(type(res_str))

print("*"*20)
# 字符 类型数组转字符串
tmp_lsit6 = ["a", "b", "c"]
print('.'.join(tmp_lsit6))  # 预期: a.b.c
