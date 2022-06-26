"""
    登陆相关功能
"""

content = "您好，这是login模块"


def login_handler(name: str, password: str):
    # 登陆的逻辑代码
    # 查库
    # 假设
    correct_username = "python"
    correct_password = "123"

    # 校验参数
    if not name or not password:
        print("参数校验失败")

    # 登陆逻辑
    if name == correct_username and password == correct_password:
        print("登陆成功")
    else:
        print("登陆失败,用户名或密码错误")
