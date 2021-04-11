# -*-coding:utf-8-*-
import numpy as np

# V value值
# R reward
# P状态转移概率
# gamma 折扣值

# 问题是求Value值
# 概率转移矩阵
P = np.mat([[0.6,0.4,0,0,0,0,0],
        [0.4,0.2,0.4,0,0,0,0],
         [0,0.4,0.2,0.4,0,0,0],
         [0,0,0.4,0.2,0.4,0,0],
         [0,0,0,0.4,0.2,0.4,0],
         [0,0,0,0,0.4,0.2,0.4],
         [0,0,0,0,0,0.4,0.6]])
R = np.mat([[1,0,0,0,0,0,10]])
print(P)
print(R)
print(np.eye(7))
print(np.eye(7)-P)
# print(np.linalg.inv(np.eye(7)-P))
# print(np.matrix(np.eye(7)-P).I)
gamma = 0.1
# V = (np.eye(7)-P).I.dot(R)
# print(V)

def get_value(p,r,gamma):
 vold = np.mat([0,0,0,0,0,0,0]).T
 vnew = np.mat([0,0,0,0,0,0,1]).T
 epislon = 0.00000000001
 while np.sum(np.square(vold - vnew))>epislon:
  vold = vnew
  vnew = r + gamma*P.dot(vold)
 return vnew

print(get_value(P,R,gamma))