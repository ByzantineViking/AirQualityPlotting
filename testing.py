import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

t = np.arange(0., 5., 0.2)
line1, line2, line3,  = plt.plot(t, t, 'r--', t, t**2, 'b:s', t, t**3, 'g-^')
line1.set_antialiased(False)
plt.setp(line3, linestyle = "steps")
plt.setp(line2,linewidth = 0.5)

plt.axis([0, 6, 0, 20])
plt.show()