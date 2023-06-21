# # A python script conveted to notebook / book

#+
import numpy as np
x = np.linspace(-1,1,100)
y = x**3

#+
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(x,y,'.-')

