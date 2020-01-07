import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/gfranco/class_public/output/test3_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['test3_background']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = ['rho_dcdm2', 'rho_tot']
tex_names = ['(8\\pi G/3)rho_dcdm2', '(8\\pi G/3)rho_tot']
x_axis = 'z'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 13]))
ax.loglog(curve[:, 0], abs(curve[:, 16]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('z', fontsize=16)
plt.show()