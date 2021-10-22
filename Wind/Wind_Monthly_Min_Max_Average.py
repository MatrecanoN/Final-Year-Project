from matplotlib import pyplot as plt
from Wind_PreProcessing import pre_processing
from Helpers.Monthly_Splicer import monthly_splicer
import pandas as pd

year_wanted = 2010

wind_data = pre_processing()
monthly_data = monthly_splicer(wind_data, year_wanted)

monthly_average_dict = {}
monthly_min_dict = {}
monthly_max_dict = {}

for months in monthly_data:
	monthly_average_dict[months] = monthly_data[months].mean()
	monthly_min_dict[months] = monthly_data[months].min()
	monthly_max_dict[months] = monthly_data[months].max()

monthly_average = pd.Series(data=monthly_average_dict.values(), index=monthly_average_dict.keys())
monthly_min = pd.Series(data=monthly_min_dict.values(), index=monthly_min_dict.keys())
monthly_max = pd.Series(data=monthly_max_dict.values(), index=monthly_max_dict.keys())

plt.bar(monthly_max.index, monthly_max.values)
plt.plot(monthly_average, color="black")
plt.bar(monthly_min.index, monthly_min.values, color="white")

plt.title(label="Year: {YEAR}".format(YEAR=year_wanted))

plt.show()
