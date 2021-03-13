import inspect
import numpy
import turtle
import requests

source = inspect.getsource(requests.request) # 查看系统函数numpy加和函数sum的源代码
print(source)
