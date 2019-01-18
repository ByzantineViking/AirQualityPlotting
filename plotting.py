import matplotlib.pyplot as plt
import numpy as ny 
import pandas as pd

tapiola = pd.read_csv("C:/Users/teemu/Documents/workspace/tapiola.csv")
lumi = tapiola["Lumensyvyys (cm)"]
sade = tapiola["Sateen intensiteetti (mm/h)"]
y = [lumi, sade]
labels = ["Lumensyvyys (cm)", "Sateen intensiteetti (mm/h)"]
x = pd.to_datetime({"year": tapiola["Vuosi"], "month": tapiola["Kk"], "day": tapiola["Pv"]})

def lines():
      for y_arr, label in zip(y, labels):
                 plt.plot(x, y_arr,label=label)

plt.setp(lines(), linewidth = 0.5)
plt.legend()
#plt.ylabel(labels[0])
plt.show()