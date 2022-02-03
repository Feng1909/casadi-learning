from casadi import *
import numpy as np

'''constant'''
# mass
m = 240
# gravity
g = 9.8
# friction coefficient
mu_x1 = 1
mu_x2 = 1
mu_x3 = 1
mu_x4 = 1
mu_y1 = 1
mu_y2 = 1
mu_y3 = 1
mu_y4 = 1
# 轮胎与质心的连线与车子前向的夹角
theta_1 = np.pi/4
theta_2 = np.pi/4
theta_3 = np.pi/4
theta_4 = np.pi/4
# Tire params
# Longitudinal
Bx = 14.78
Cx = 1.33
Dx = 2.339
Ex = 0.3623
# Lateral
By = 9.882
Cy = 1.111
Dy = -2.559
Ey = 0.2949

'''formula'''
lambda_1 = SX.sym('l1')
lambda_2 = SX.sym('l2')
lambda_3 = SX.sym('l3')
lambda_4 = SX.sym('l4')

F_x1 = mu_x1 * m*g/4 * Dx * sin(Cx*arctan(Bx*lambda_1 - Ex*(Bx - arctan(Bx*lambda_1))))
F_x2 = mu_x2 * m*g/4 * Dx * sin(Cx*arctan(Bx*lambda_2 - Ex*(Bx - arctan(Bx*lambda_2))))
F_x3 = mu_x3 * m*g/4 * Dx * sin(Cx*arctan(Bx*lambda_3 - Ex*(Bx - arctan(Bx*lambda_3))))
F_x4 = mu_x4 * m*g/4 * Dx * sin(Cx*arctan(Bx*lambda_4 - Ex*(Bx - arctan(Bx*lambda_4))))
F_y1 = mu_y1 * m*g/4 * Dy * sin(Cy*arctan(By*lambda_1 - Ey*(By - arctan(By*lambda_1))))
F_y2 = mu_y2 * m*g/4 * Dy * sin(Cy*arctan(By*lambda_2 - Ey*(By - arctan(By*lambda_2))))
F_y3 = mu_y3 * m*g/4 * Dy * sin(Cy*arctan(By*lambda_3 - Ey*(By - arctan(By*lambda_3))))
F_y4 = mu_y4 * m*g/4 * Dy * sin(Cy*arctan(By*lambda_4 - Ey*(By - arctan(By*lambda_4))))

delta_1 = 0
delta_2 = 0
delta_3 = 0
delta_4 = 0

M_1 = -F_x1*cos(delta_1)*sin(theta_1) + F_y1*sin(delta_1)*sin(theta_1) + F_x1*sin(delta_1)*cos(theta_1)+F_y1*cos(delta_1)*cos(theta_1)
M_2 = -F_x2*cos(delta_2)*sin(theta_2) + F_y1*sin(delta_2)*sin(theta_2) + F_x1*sin(delta_2)*cos(theta_2)+F_y1*cos(delta_2)*cos(theta_2)
M_3 = -F_x3*cos(delta_3)*sin(theta_3) + F_y1*sin(delta_3)*sin(theta_3) + F_x1*sin(delta_3)*cos(theta_3)+F_y1*cos(delta_3)*cos(theta_3)
M_4 = -F_x4*cos(delta_4)*sin(theta_4) + F_y1*sin(delta_4)*sin(theta_4) + F_x1*sin(delta_4)*cos(theta_4)+F_y1*cos(delta_4)*cos(theta_4)

M = M_1 + M_2 + M_3 + M_4

G = lambda_1 + lambda_2 + lambda_3 + lambda_4

nlp = {'x': vertcat(lambda_1, lambda_2, lambda_3, lambda_4), 'f': M, 'g': G}

S = qpsol('S', 'qpoases', nlp)
print(S)
# r = S(x0=[2.5, 3.0, 0.75, 0], \
#       lbg=0, ubg=100)
# x_opt = r['x']
# r = S(lbg=0, ubg=100)
r = S(ubg=1)
# print('x_opt: ', x_opt)

# S.generate_dependencies("nlp.c")