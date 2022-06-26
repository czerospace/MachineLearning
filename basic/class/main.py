# -*- coding: utf-8 -*-
"""
    @Author:    Niko
    @Date:      20220625
    @Tips:      面向对象，类
"""

from student import Student, TestStudent

# 创建实例对象

# student_obj = Student("测试1", 18, 20)
# print(student_obj.name, student_obj.age, student_obj.no)
# print(student_obj.instance_name, student_obj.instance_age, student_obj.instance_no)

# student_obj.store_student_info()
# student_obj.get_student_info(20)

# student_obj.get_student_count()

obj = TestStudent("学生信息录入", 18, 10)
print(obj.name, obj.age, obj.no)
obj.store_student_info()
