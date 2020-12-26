
#simple audio signal and plot them. 

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [16,12]
plt.rcParams.update({'font.size': 18})

dt = 0.001
t = np.arange(0,1,dt)
f=np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t)
f_clean=f
f = f + 2.5*np.random.randn(len(t))

plt.plot(t,f,color='c',label='noise')
plt.plot(t,f_clean,color='r', label='clean')
plt.legend()
