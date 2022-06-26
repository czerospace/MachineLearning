"""
    @Author:    Niko
    @Date:      20220626
    @Tips:      PyMySQL链接数据库
"""
from pymysql.connections import Connection

# 第一步：创建链接
conn = Connection(host="192.168.51.3",port=3306,user="root",password="Jilin123456",database="homed_iusm")

# 第二步：获取游标
cursor = conn.cursor()
print('cursor object = {}'.format(cursor))

# 第三步：执行操作(SQL)
res = cursor.execute("select * from role;")
print("受影响行数:",res)
print("获取全部结果: {}".format(cursor._rows))

print("获取第1条结果: {}".format(cursor.fetchone()))
print("获取第2条结果: {}".format(cursor.fetchone()))
print("获取后3条结果: {}".format(cursor.fetchmany(3)))
print("获取剩余条结果: {}".format(cursor.fetchall()))
# 第五步：关闭链接
cursor.close()
conn.close() 