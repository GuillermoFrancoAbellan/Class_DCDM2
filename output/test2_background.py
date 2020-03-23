import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/gfranco/class_DCDM2/output/test2_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['test2_background']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = ['H[1/Mpc]']
tex_names = ['H [1/Mpc]']
x_axis = 'z'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 3]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('z', fontsize=16)
plt.show()