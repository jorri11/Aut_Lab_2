import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from queues import insertAndRotate
""" def insertAndRotate(a,array = deque):
    array.appendleft(a)
    array.rotate()
    array.popleft()
    print(array)
 """
t_start=0#s
t_stop=60#s
steg = 0.05
N_sim=int((t_stop-t_start)/steg) +1 #Number of time-steps

t_array=np.linspace(t_start,t_stop, N_sim)

#print(N_sim)
u = 3
theta_t = 23 #[s]
theta_d = 3
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
    #if f>50:
    #    u=0 
    
    t=t_array[f]
    if t > 40:
        u=0
    insertAndRotate(u,forsinkelse_que)
    u_t=forsinkelse_que[-1]
    
    dT_dt=(1/theta_t)*((T_env - T_t) + k_h*u_t)
    u_array[f] = u
    
    a = T_t+dT_dt*1
    
    #forsinkelse_que.append(T_t+dT_dt*theta_d)
    T_array[f] = T_t
    T_t=a
    #print(forsinkelse_que)
    
plt.close()
plt.subplot(2, 1, 1)
plt.title('Simulering av varmluftsprosess')
plt.xlabel('Tid[s]')
plt.ylabel('Temperatur [°C]')
plt.plot(t_array, T_array,'b')
plt.subplot(2,1,2)
plt.ylim(0,5)
plt.plot(t_array, u_array, 'r')
plt.subplots_adjust(hspace=0.5)
plt.show()


""" plt.close('all') # Closes all gures before plotting
fig_width_inch = 24/2.54
fig_height_inch = 18/2.54
plt.figure(num='Simulering av magasin',figsize=(fig_width_inch,fig_height_inch))
plt.subplot(2, 1, 1)
plt.grid(which='both', color='grey')
plt.ylim(0.9, 2.6)
#plt.title('Simulering av magasin)
plt.plot(t_array, h_array, 'b')
plt.legend(labels=('Nivå h [m]', ), # Note: Comma and space!
loc='upper left', handlelength=2, fontsize=12)
plt.subplot(2, 1, 2)
plt.grid(which='both', color='grey')
plt.ylim(1.9, 4.1)
plt.xlabel('t [s]')
plt.plot(t_array, F_i_array, 'r', t_array, F_u_array, 'g')
plt.legend(labels=('Innstrøm F_i [m3/s]','utstræ, F_u [m3/s]'),loc='upper left', handlelength = 2, fontsize = 12) """