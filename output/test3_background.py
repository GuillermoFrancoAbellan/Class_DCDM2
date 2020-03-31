import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/guillermo/class_DCDM2/output/test3_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['test3_background']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'p_wdm2_a', u'p_wdm2_b']
tex_names = ['p_wdm2_a', 'p_wdm2_b']
x_axis = 'z'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 17]))
ax.loglog(curve[:, 0], abs(curve[:, 18]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('z', fontsize=16)
plt.show()