"""
    @Author:    Niko
    @Date:      20220625
    @Tips:      字典的遍历
"""
a = {
    "url": "http://www.baidu.com/",
    "title": "baidu",
    "ip": "192.168.1.1"
}

print("#割#"*10)
# 方式1
for obj in a:
    print(a.get(obj))

print("#割#"*10)
# 方式2 通过内置的 values 方法
# 缺点:拿不到 key
for value in a.values():
    print(value)

print("#割#"*10)
# 方式3 通过 内置的 keys 方法
for key in a.keys():
    print(a.get(key))

print("#割#"*10)
# 方式4 同时获取 key value
for key, value in a.items():
    print(key, value)
