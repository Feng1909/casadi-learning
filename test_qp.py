#!/usr/bin/env python
# -*- coding: utf-8 -*-

import casadi as ca
import casadi.tools as ca_tools
import numpy as np
import time
import math

if __name__ == '__main__':
    print("begin the test program.")
    t1 = time.time()
    x = ca.SX.sym('x')  # 定义一 维变量x
    y = ca.SX.sym('y')  # 定义一 维变量y

    f = x ** 2 + y ** 2  # 定义目标函数

    qp = {'x': ca.vertcat(x, y), 'f': f, 'g': x + y - 10}
    S = ca.qpsol('S', 'qpoases', qp)  # 加载求解器
    print(S)
    r = S(lbg=0)  # 加载约束条件并进行求解
    x_opt = r['x']
    print('x_opt:', x_opt)  # 显示求解结果
    t2 = time.time()
    print(t2-t1)
