from matplotlib import pyplot as plt
from Demand_PreProcessing import pre_processing as demand_pre_processing


plt.plot(demand_pre_processing())
plt.grid()
plt.xlabel("Date and Time of Data")
plt.ylabel("Grid Power Demand (MW)")
plt.title("UK Grid Demand by Date and Time")

plt.show()
