from matplotlib import pyplot as plt
from Heat_Preprocessing import pre_processing as heat_pre_processing

# Comes in in KWh / Day
data = heat_pre_processing()

data = data / 1000000
rolling_average = data.rolling(365, min_periods=1).mean()

plt.plot(data)
plt.plot(rolling_average)
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel("Date", fontsize=20)
plt.ylabel("Grid Heat Demand (GWh / Day)", fontsize=20)
plt.title("GB Gas Grid Heat Demand by Date", fontsize=20)
plt.legend(["Daily Grid Heat Demand", "365-Day Rolling Average"], fontsize=14)

plt.show()
