# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 16:46:33 2021

@author: user
"""


import keras
import keras2onnx
import onnx
from keras.models import load_model
model = load_model('CNN_Mnist.h5')  
onnx_model = keras2onnx.convert_keras(model, model.name)
temp_model_file = 'CNN_Mnistmodel.onnx'
onnx.save_model(onnx_model, temp_model_file)
#版权声明：本文为CSDN博主「恋上萤火」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/weixin_43826596/article/details/101080633