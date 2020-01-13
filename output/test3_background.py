import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/gfranco/class_DCDM2/output/test3_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['test3_background']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = ['p_tot', 'p_tot_prime']
tex_names = ['(8\\pi G/3)p_tot', '(8\\pi G/3)p_tot_prime']
x_axis = 'z'
ylim = []
xlim = []
ax.plot(curve[:, 0], curve[:, 18])
ax.plot(curve[:, 0], curve[:, 19])

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('z', fontsize=16)
plt.show()