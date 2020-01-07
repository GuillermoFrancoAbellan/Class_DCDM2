import matplotlib.pyplot as plt
import numpy as np



files = ['/Users/gfranco/class_public/output/test3_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))

fig, ax = plt.subplots()

curve = data[0]

ax.set_xlim([-50,1200])


H02=curve[4619, 3]**2 #Hubble constant squared, in units of Mpc^{-2} (i.e., c=1)
 
ax.plot(curve[:, 0], abs(curve[:, 14])/H02,label=r'$\rho_1 \ (CLASS) $')
#massive daughter seems to be computed correctly, unlike the massless daughter, which shows an ugly peak
ax.plot(curve[:, 0], abs(curve[:, 15])/H02,label=r'$ \rho_2 \ (CLASS) $')

#ax.set_yscale('log')

ax.legend(loc='best', fontsize=12)

ax.set_xlabel('z', fontsize=15)
ax.set_ylabel(r'$\rho/ \rho_{crit}$', fontsize=15)
plt.show()

#%%



