from matplotlib import pyplot as plt
from Demand_PreProcessing import pre_processing as demand_pre_processing


plt.plot(demand_pre_processing())
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.grid()
plt.xlabel("Date", fontsize=20)
plt.ylabel("Grid Power Demand (MW)", fontsize=20)
plt.title("GB Grid Demand by Date and Time", fontsize=20)

plt.show()
