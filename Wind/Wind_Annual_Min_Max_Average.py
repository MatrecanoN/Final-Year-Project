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
	annual_average_dict[years] = annual_data[years].mean()
	annual_min_dict[years] = annual_data[years].min()
	annual_max_dict[years] = annual_data[years].max()

annual_average = pd.Series(data=annual_average_dict.values(), index=annual_average_dict.keys())
annual_min = pd.Series(data=annual_min_dict.values(), index=annual_min_dict.keys())
annual_max = pd.Series(data=annual_max_dict.values(), index=annual_max_dict.keys())

plt.bar(annual_max.index, annual_max.values)
plt.plot(annual_average, color="black")
plt.bar(annual_min.index, annual_min.values, color="white")

plt.title(label="Low/High and Average of Wind Generation as % of Capacity")

plt.show()
