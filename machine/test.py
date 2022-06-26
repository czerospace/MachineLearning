"""
    @Author:    Niko
    @Date:      20220626
    @Tips:      测试是否识别到显卡
"""
import tensorflow as tf
print(tf.__version__)
tf.test.is_gpu_available()
