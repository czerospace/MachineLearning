# -*- coding: utf-8 -*-
"""
    @Author:    Niko
    @Date:      20220625
    @Tips:      模块和包
"""

if __name__ == '__main__':
    # 第一种，直接导入
    import login
    login.login_handler("python", "123")

    # 第二种，按需导入
    from login import login_handler
    login_handler("python", "123456")

    # 第三种，全部导入
    from login import *
    login_handler("python", "123")
    print(content)
