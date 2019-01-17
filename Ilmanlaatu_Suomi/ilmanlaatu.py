
import numpy as np 
import matplotlib.pyplot as plt

import pandas

tampere = pandas.read_csv("Ilmanlaatu_Suomi/Tampere.csv")
counter1 = 0
for kk in tampere["Kk"]:
    if len(str(kk)) == 1:
        tampere.loc[counter1,  "Kk"] = "0" + str(kk)
    counter1 += 1

counter2 = 0
for pv in tampere["Pv"]:
    if len(str(pv)) == 1:
        tampere.loc[counter2, "Pv"] = "0" + str(pv)
    counter2 += 1
tampere["Date"] = tampere["Vuosi"].map(str) + "-" +  tampere["Kk"].map(str) + "-" + tampere["Pv"].map(str)
#tampere["date"] = tampere["Vuosi"].map(int) + "-" + tampere["Kk"] + "-" 
print(tampere)

print(type(tampere['Pienhiukkaset (ug/m3)'][2]))
#Column name, and indexed row number

#To use a different column as the DataFrame index,
#  add the index_col optional parameter:
#df = pandas.read_csv('hrdata.csv', index_col='Name')

y = tampere.loc[25000:30000]['Pienhiukkaset (ug/m3)']
x = tampere.loc[25000:30000]['Date']
plt.plot(x,y, label = 'Tampere')
plt.xlabel('Päivämäärä')
plt.ylabel('Pienhiukkaset (ug/m3)')
plt.title('Ilmansaasteet Tampere')
plt.legend()
plt.show()
