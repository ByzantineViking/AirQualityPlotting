
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas
import matplotlib.dates as mdates
helsinki = pandas.read_csv("Ilmanlaatu_Suomi/Tampere.csv")
helsinki["Date"] = pandas.to_datetime({'year': helsinki["Vuosi"], 'month': helsinki["Kk"],'day': helsinki["Pv"]})


print(helsinki["Date"])


y = helsinki.loc[25000:30000]['Pienhiukkaset (ug/m3)']
x = helsinki.loc[25000:30000]["Date"]
plt.plot(x, y, label='Pienhiukkasten määrä ilmakehässä')
plt.xlabel('Date')
plt.ylabel('Pienhiukkaset (ug/m3)')
plt.title('Ilmansaasteet Helsingissä')
plt.legend()


plt.show()
