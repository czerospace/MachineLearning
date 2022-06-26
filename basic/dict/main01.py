# -*- coding: utf-8 -*-
"""
    @Author:    Niko
    @Date:      20220625
    @Tips:      字典
"""

# 定义空字典

student_dict = {}
print(student_dict)
print(type(student_dict))

# 定义一个字典
student_dict1 = {
    "user_name": "yeguo",
    "age": 18,
    "birthday": "1017"
}

# 取值
print(student_dict1["user_name"])
print(student_dict1["age"])
print(student_dict1["birthday"])

student_dict2 = {
    "user_name": "miaozong",
    "age": 17,
    "birthday": "1018"
}

student_dict3 = [student_dict1, student_dict2]

print(student_dict3)

# 取 dict 中 key 对应的 value
for obj in student_dict3:
    print(obj["user_name"])


print("*"*20)
# 修改字典里的值
student_dict1["age"] = 30
print(student_dict1)


print("*"*20)
# 检查 dict 中是否包含某个 key
if "user_name" in student_dict1:
    print("在")
else:
    print("不在")

# 字典的你一种声明方法

student_dict4 = dict(
    user_name="huige",
    age=18,
    birthday="1019"
)
print(type(student_dict4))
print(student_dict4)
