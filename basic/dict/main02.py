# -*- coding: utf-8 -*-
"""
    @Author:    Niko
    @Date:      20220625
    @Tips:      字典的常用方法 clear get pop update
"""
# clear 清除字典中所有项
tmp_dict = {
    "user_name": "Niko",
    "age": 18
}
print(tmp_dict)
tmp_dict.clear()
print(tmp_dict)

print("*"*20)
# get 访问字典中 key 多赢的 value，这个方法不会抛出异常
tmp_dict = {
    "user_name": "Niko",
    "age": 18
}

print(tmp_dict.get("user_name"))
print(tmp_dict["user_name"])  # 如果 user_name 不存在 会抛出异常

# pop 将 key 和 value 从字典中删除，会返回这个 value
print("#"*20)
print(tmp_dict)
print(tmp_dict.pop("age"))
print(tmp_dict)

print("#"*20)
# update 用一个字典更新另一个字典，如果碰到相同的 key 则会覆盖
a = {
    "url": "http://www.baidu.com/",
    "title": "baidu"
}
b = {
    "url": "http://www.google.com/",
    "new_vaule": "google"
}

a.update(b)
print(a)
print(b)
