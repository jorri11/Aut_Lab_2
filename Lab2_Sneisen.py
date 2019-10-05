import numpy as np
import matplotlib.pyplot as plt
from collections import deque

def insertAndRotate(a,array = deque):
    array.appendleft(a)
    array.pop()
    #print(array)
def Modell(u,f):


    
    insertAndRotate(u,forsinkelse_que)
    u_t=forsinkelse_que[-1]
    
    dT_dt=(1/theta_t)*((T_env - T_t) + k_h*u_t)
    u_array[f] = u
    
    a = T_t+dT_dt*steg
    
    T_array[f] = T_t
    T_t=a
    return T_array[f]
t_start=0#[s]
t_stop=180#[s]
steg = 0.05#Tidssteg
N_sim=int((t_stop-t_start)/steg) +1 #Number of time-steps

t_array=np.linspace(t_start,t_stop, N_sim)#tidsarray

u = 5#[V]
theta_t = 23 #[s]
theta_d = 3#[s]
T_env = 20 # [degrees c]
T_init = T_env # [degrees c]
T_t =T_init
k_h =3.5 #[C/V]
T_array = np.zeros(N_sim)
f_array = np.arange(0,N_sim)
u_array = np.zeros(N_sim)
forsinkelse_que = deque()

for x in range(0,int(theta_d/steg)):
    forsinkelse_que.append(0.0)

print(forsinkelse_que)
for f in f_array:
    t=t_array[f]
    if t > 80:
        u=2.5
    Modell(u,t,T_t,f,T_array,u_array)
    """
    insertAndRotate(u,forsinkelse_que)
    u_t=forsinkelse_que[-1]
    
    dT_dt=(1/theta_t)*((T_env - T_t) + k_h*u_t)
    u_array[f] = u
    
    a = T_t+dT_dt*steg
    
    T_array[f] = T_t
    T_t=a
    """
    #print(T_t)
    
plt.close()
plt.subplot(2, 1, 1)
plt.title('Temperatur varmluftsprosess')
plt.xlabel('Tid[s]')
plt.ylabel('Temperatur [°C]')
plt.plot(t_array, T_array,'b')
plt.subplot(2,1,2)
plt.ylim(0,5)
plt.title('Styresignal')
plt.xlabel('Tid[s]')
plt.ylabel('Spenning[V]')
plt.plot(t_array, u_array, 'r')
plt.subplots_adjust(hspace=0.5)
plt.show()