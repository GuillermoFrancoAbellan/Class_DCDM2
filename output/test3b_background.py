import matplotlib.pyplot as plt
import numpy as np



files = ['/Users/gfranco/class_DCDM2/output/test3_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))

fig, ax = plt.subplots()

curve = data[0]

ax.set_xlim([-50,2100])

l=len(curve[:, 3])
H02=curve[l-1, 3]**2 #Hubble constant squared, in units of Mpc^{-2} (i.e., c=1)

ax.plot(curve[:, 0], abs(curve[:, 14])/H02,label=r'$\rho_1 \ (CLASS) $')
#massive daughter seems to be computed correctly, unlike the massless daughter, which shows an ugly peak
ax.plot(curve[:, 0], abs(curve[:, 15])/H02,label=r'$ \rho_2 \ (CLASS) $')
ax.set_title(r'$\Omega_{cdm}=0.24, \, \tau=35.5 \, \rm{Gyr}, \, \epsilon=0.499, \, h=0.7$')
#ax.set_yscale('log')

ax.legend(loc='best', fontsize=12)

ax.set_xlabel('z', fontsize=15)
ax.set_ylabel(r'$\rho/ \rho_{crit}$', fontsize=15)
plt.show()

#%%



