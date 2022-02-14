from matplotlib import pyplot as plt
from Wind_PreProcessing import pre_processing as wind_pre_processing
from Helpers.Yearly_Splicer import yearly_splicer
import pandas as pd

wind_data = wind_pre_processing()
annual_data = yearly_splicer(wind_data)

annual_average_dict = {}
annual_min_dict = {}
annual_max_dict = {}

for years in annual_data:
	annual_average_dict[years] = annual_data[years].mean() * 100
	annual_min_dict[years] = annual_data[years].min() * 100
	annual_max_dict[years] = annual_data[years].max() * 100

annual_average = pd.Series(data=annual_average_dict.values(), index=annual_average_dict.keys())
annual_min = pd.Series(data=annual_min_dict.values(), index=annual_min_dict.keys())
annual_max = pd.Series(data=annual_max_dict.values(), index=annual_max_dict.keys())

plt.bar(annual_max.index, annual_max.values)
plt.plot(annual_average, color="black")
plt.bar(annual_min.index, annual_min.values, color="white")

plt.title(label="Low/High and Average of Wind Generation as % of Capacity", fontsize=20)
plt.xlabel("Year", fontsize=20)
plt.ylabel("% of Installed Capacity Utilisation", fontsize=20)
plt.legend(["Annual Average", "Annual Range of Recorded Generation"])
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.grid()
plt.show()
