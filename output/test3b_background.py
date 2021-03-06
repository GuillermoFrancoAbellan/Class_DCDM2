import matplotlib.pyplot as plt
import numpy as np



files = ['/Users/gfranco/class_DCDM2/output/test3_background.dat']
files2 = ['/Users/gfranco/class_DCDM2/output/test2_background.dat']
#Files = ['/home/guillermo/class_DCDM2/output/test3_background.dat']
data = []
data2 = []
for data_file in files:
    data.append(np.loadtxt(data_file))
    
for data_file2 in files2:
    data2.append(np.loadtxt(data_file2))

fig, ax = plt.subplots()

curve = data[0]
curve2 = data2[0]
ax.set_xlim([-50,5000])
ax.set_ylim([0,8000])
l=len(curve[:, 3])
l2=len(curve2[:, 3])
H02=curve[l-1, 3]**2 #Hubble constant squared, in units of Mpc^{-2} (i.e., c=1)
H02b=curve2[l2-1, 3]**2 #Hubble constant squared, in units of Mpc^{-2} (i.e., c=1)

ax.plot(curve[:, 0], abs(curve[:, 13])/H02,label=r'$\rm{DCDM} \ (CLASS_{v2}) $')
#ax.plot(curve[:, 0], abs(curve[:, 15])/H02,label=r'$\rm{massive} \ (CLASS_{v2}) $')
ax.plot(curve2[:, 0], abs(curve2[:, 13])/H02b,label=r'$\rm{DCDM} \ (CLASS_{v1}) $')

ax.set_title(r'$\Omega_{dcdm}^{ini}=0.24, \, \tau=35.5 \, \rm{Gyr}, \, \epsilon=0.4999, \, h=0.7$')
ax.legend(loc='best', fontsize=12)

ax.set_xlabel('z', fontsize=15)
ax.set_ylabel(r'$\rho (z)/ \rho_{c}^0$', fontsize=15)
plt.show()

#%%

files = ['/Users/gfranco/class_DCDM2/output/test3_background.dat']
#files = ['/home/guillermo/class_DCDM2/output/test3_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))

fig, ax = plt.subplots()

curve = data[0]
ax.set_xlim([1e-3,1])
#ax.set_ylim([0.32,0.35])
ax.plot(1/(1+curve[:, 0]),abs(curve[:, 16]),label=r'$w_2 \ (CLASS) $')
ax.set_title(r'$\Omega_{cdm}=0.24, \, \tau=35.5 \, \rm{Gyr}, \, \epsilon=0.166, \, h=0.7$')
ax.set_xscale('log')
ax.set_xlabel('a', fontsize=15)
ax.set_ylabel(r'$w$', fontsize=15)
ax.legend(loc='best', fontsize=12)
plt.show()
#%%
