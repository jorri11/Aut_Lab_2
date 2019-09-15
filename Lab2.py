import numpy as np
import matplotlib.pyplot as plt
from collections import deque

def insertAndRotate(a,array = deque):
    array.appendleft(a)
    array.rotate()
    return(array.popleft())
    #print(array)

t_start=0#s
t_stop=160#s
N_sim=int((t_stop-t_start)/3) +1 #Number of time-steps

t_array=np.linspace(t_start,t_stop, N_sim)

#print(N_sim)
steg = 120
u = 5
theta_t = 23 #[s]
theta_d = 3
T_env = 20 # [degrees c]
T_init = T_env # [degrees c]
T_t =T_init
k_h =5 #[C/V]
T_array = np.zeros(N_sim)
f_array = np.arange(0,N_sim)
u_array = np.zeros(N_sim)
forsinkelse_que = deque()

for x in range(0,10):
    forsinkelse_que.append(T_init)

print(forsinkelse_que)
for f in f_array:
    
    t=t_array[f]
    
    dT_dt=(1/theta_t)*((T_env - T_t) + k_h*u*(1))
    
    #h_kp1 = T_t+dT_dt*theta_d
    #forsinkelse_que.append(T_t+dT_dt*theta_d)
    insertAndRotate(T_t+dT_dt*theta_d,forsinkelse_que)
    T_array[f] = T_t
    T_t = forsinkelse_que.popleft()
    print(forsinkelse_que)
    
plt.close()    
plt.plot(T_array,'b')
plt.show()
