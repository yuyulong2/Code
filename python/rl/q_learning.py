# -*-coding:utf-8-*-
import numpy as np

R = np.mat([[-1,-1,-1,-1,0,-1],
            [-1,-1,-1,0,-1,100],
            [-1,-1,-1,0,-1,-1],
            [-1,0,0,-1,0,-1],
            [0,-1,-1,0,-1,100],
            [-1,0,-1,-1,0,100]])
print(R)
print(R[0])
gamma = 0.8
Q = np.zeros((6,6))
for i in range(10):
    s = 0
    if s != 5:
        for i in R[s]:
            if i > 0:
                Q[s,i] = R[s,i]+gamma*max(Q[s,x] lambda x:for x in R[s])

