# -*- coding: utf-8 -*-
"""
    @Author:    Niko
    @Date:      20220625
    @Tips:      面向对象，类
"""

# 定义一个 Student 的类


class Student:
    # 定义类变量
    name = "Niko"
    age = 18
    no = 1

    # 定义实例变量
    def __init__(self, name, age, no):
        # 实例变量
        print("这是实例变量")
        self.instance_name = name
        self.instance_age = age
        self.instance_no = no

    # 定义实例方法
    def store_student_info(self):
        print("{},{},{},学生信息存入数据库成功".format(
            self.instance_name, self.instance_age, self.instance_no))

    # 定义静态方法
    @staticmethod
    def get_student_info(no):
        print("学号为{}学生信息取出成功".format(no))

    # 定义类方法
    @classmethod
    def get_student_count(cls):
        print("类变量name={}注意不能调用实例变量".format(cls.name))


class TestStudent(Student):
    print("this is TestStudent")
    name = "yeguo"

    def store_student_info(self):
        print("{}".format(self.instance_name))
