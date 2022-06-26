# -*- coding: utf-8 -*-
"""
    @Author:    Niko
    @Date:      20220625
    @Tips:      包
"""

if __name__ == '__main__':
    # from demo01 import *
    # login.login_handler("", "")
    # user.test_user()

    from demo01 import user
    user.test_user()

    from demo01.user import test_user
    test_user()
