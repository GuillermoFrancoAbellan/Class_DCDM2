import numpy as np
import itertools
from matplotlib import pyplot
import matplotlib.pyplot as plt
#%%
#plot densities of massive and massless daughters

files = ['/Users/gfranco/class_DCDM2/output/test3_background.dat']
#Files = ['/home/guillermo/class_DCDM2/output/test3_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))

fig, ax = plt.subplots()

curve = data[0]
ax.set_xlim([-50,4.5e7])
#ax.set_ylim([0,700])
l=len(curve[:, 3])
H02=curve[l-1, 3]**2 #Hubble constant squared, in units of Mpc^{-2} (i.e., c=1)

ax.plot(curve[:, 0], abs(curve[:, 14])/H02,label=r'$\rm{massless} \ (CLASS_{v2}) $')
ax.plot(curve[:, 0], abs(curve[:, 15])/H02,label=r'$ \rm{massive} \ (CLASS_{v2}) $')

ax.set_title(r'$\Omega_{dcdm}^{ini}=0.24, \, \tau=35.5 \, \rm{Gyr}, \, \epsilon=0.166, \, h=0.7$')
ax.legend(loc='best', fontsize=12)

ax.set_xlabel('z', fontsize=15)
ax.set_ylabel(r'$\rho (z)/ \rho_{c}^0$', fontsize=15)
plt.show()

#%%

#plot rho_2 for several values of parameter varepsilon
files1 = ['/Users/gfranco/class_DCDM2/output/test3eps005_background.dat']
files2 = ['/Users/gfranco/class_DCDM2/output/test3eps017_background.dat']
files3 = ['/Users/gfranco/class_DCDM2/output/test3eps035_background.dat']
files4 = ['/Users/gfranco/class_DCDM2/output/test3eps049_background.dat']

files1b = ['/Users/gfranco/class_DCDM2/output/test3eps005b_background.dat']
files2b = ['/Users/gfranco/class_DCDM2/output/test3eps017b_background.dat']
files3b = ['/Users/gfranco/class_DCDM2/output/test3eps035b_background.dat']
files4b = ['/Users/gfranco/class_DCDM2/output/test3eps049b_background.dat']

data1 = []
for data_file1 in files1:
    data1.append(np.loadtxt(data_file1))
data2 = []
for data_file2 in files2:
    data2.append(np.loadtxt(data_file2))
data3 = []
for data_file3 in files3:
    data3.append(np.loadtxt(data_file3))
data4 = []
for data_file4 in files4:
    data4.append(np.loadtxt(data_file4))
    
    
data1b = []
for data_file1b in files1b:
    data1b.append(np.loadtxt(data_file1b))
data2b = []
for data_file2b in files2b:
    data2b.append(np.loadtxt(data_file2b))
data3b = []
for data_file3b in files3b:
    data3b.append(np.loadtxt(data_file3b))
data4b = []
for data_file4b in files4b:
    data4b.append(np.loadtxt(data_file4b))
    
fig, ax = plt.subplots()

curve1 = data1[0]
curve2 = data2[0]
curve3 = data3[0]
curve4 = data4[0]

curve1b = data1b[0]
curve2b = data2b[0]
curve3b = data3b[0]
curve4b = data4b[0]

ax.set_xlim([1.0e-4,1.0e3])
ax.set_ylim([1.0e-3,0.15])

ax.plot(curve1[:, 0], abs(curve1[:, 15])/abs(curve1[:, 17]),'r',label=r'$ \epsilon=0.05 $')
ax.plot(curve2[:, 0], abs(curve2[:, 15])/abs(curve2[:, 17]),'g',label=r'$ \epsilon=0.17 $')
ax.plot(curve3[:, 0], abs(curve3[:, 15])/abs(curve3[:, 17]),'b',label=r'$ \epsilon=0.35 $')
ax.plot(curve4[:, 0], abs(curve4[:, 15])/abs(curve4[:, 17]),'k',label=r'$ \epsilon=0.49 $')

ax.plot(curve1b[:, 0], abs(curve1b[:, 15])/abs(curve1b[:, 17]),'r--',label=r'$ \epsilon=0.05 $')
ax.plot(curve2b[:, 0], abs(curve2b[:, 15])/abs(curve2b[:, 17]),'g--',label=r'$ \epsilon=0.17 $')
ax.plot(curve3b[:, 0], abs(curve3b[:, 15])/abs(curve3b[:, 17]),'b--',label=r'$ \epsilon=0.35 $')
ax.plot(curve4b[:, 0], abs(curve4b[:, 15])/abs(curve4b[:, 17]),'k--',label=r'$ \epsilon=0.49 $')

plt.xscale('log')
plt.yscale('log')


ax.set_title(r'$\Omega_{dcdm}^{ini}=0.24, \, \, \tau=35.5 \, \rm{Gyr}, \, \, h=0.7$')

lines = ax.get_lines()

legend1=pyplot.legend([lines[i] for i in [0,1,2,3]],[r'$ \epsilon=0.05 $',r'$ \epsilon=0.17 $',r'$ \epsilon=0.35 $',r'$ \epsilon=0.49 $'],title='Expression 1',loc=1,fontsize=12)
legend2=pyplot.legend([lines[i] for i in [4,5,6,7]],[r'$ \epsilon=0.05 $',r'$ \epsilon=0.17 $',r'$ \epsilon=0.35 $',r'$ \epsilon=0.49 $'],title='Expression 2',loc=3,fontsize=12)

ax.add_artist(legend1)
ax.add_artist(legend2)



ax.set_xlabel('z', fontsize=15)
ax.set_ylabel(r'$\rho_2(z)/ \rho_{tot}(z)$', fontsize=15)
plt.show()


#%%
#plot H(z) for several values of varepsilon

c=2.99792458e8   

files1 = ['/Users/gfranco/class_DCDM2/output/test3eps005_background.dat']
files2 = ['/Users/gfranco/class_DCDM2/output/test3eps017_background.dat']
files3 = ['/Users/gfranco/class_DCDM2/output/test3eps035_background.dat']
files4 = ['/Users/gfranco/class_DCDM2/output/test3eps049_background.dat']

data1 = []
for data_file1 in files1:
    data1.append(np.loadtxt(data_file1))
data2 = []
for data_file2 in files2:
    data2.append(np.loadtxt(data_file2))
data3 = []
for data_file3 in files3:
    data3.append(np.loadtxt(data_file3))
data4 = []
for data_file4 in files4:
    data4.append(np.loadtxt(data_file4))
    
fig, ax = plt.subplots()

curve1 = data1[0]
curve2 = data2[0]
curve3 = data3[0]
curve4 = data4[0]

ax.set_xlim([0,2.5])
ax.set_ylim([55,80])

plt.plot(curve1[:, 0], (c/1.e3)*abs(curve1[:,3])/(1.0+curve1[:, 0]),'r',label=r'$\epsilon=0.05$ ')
plt.plot(curve2[:, 0], (c/1.e3)*abs(curve2[:,3])/(1.0+curve2[:, 0]),'g',label=r'$\epsilon=0.17$ ')
plt.plot(curve3[:, 0], (c/1.e3)*abs(curve3[:,3])/(1.0+curve3[:, 0]),'b',label=r'$\epsilon=0.35$ ')
plt.plot(curve4[:, 0], (c/1.e3)*abs(curve4[:,3])/(1.0+curve4[:, 0]),'k',label=r'$\epsilon=0.49$ ')

ax.set_title(r'$\Omega_{dcdm}^{ini}=0.24, \, \, \tau=35.5 \, \rm{Gyr}, \, \, h=0.7$')
ax.legend(loc='best', fontsize=12)


ax.set_xlabel(r'$z$',fontsize=15)
ax.set_ylabel(r'$H(z)/(1+z)$',fontsize=15)
plt.show()

#%% Plot equation of state parameter for massive particle
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
