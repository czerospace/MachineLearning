# -*- coding: utf-8 -*-
"""
    @Author:    Niko
    @Date:      20220625
    @Tips:      包的使用
"""

import requests

res = requests.get("https://www.baidu.com")
print(res)
print("*"*20)
print(res.content)
