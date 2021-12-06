from matplotlib import pyplot as plt
from Solar_PreProcessing import pre_processing as wind_pre_processing
from Helpers.Monthly_Splicer import monthly_splicer
import pandas as pd
import numpy as np


wind_data = wind_pre_processing()

first_year = wind_data.index[0].year
last_year = wind_data.index[-1].year

year_list = range(first_year, last_year + 1, 1)
zero_to_one = [round((x * 0.1), 1) for x in range(0, 11, 2)]

for years in year_list:
	plt.subplot(4, 3, (years - first_year) + 1)
	monthly_data = monthly_splicer(wind_data, years)

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

	plt.xlabel("Month of Generation")
	plt.ylabel("% Generation")
	plt.title(label="Year: {YEAR}".format(YEAR=years))
	plt.xticks(range(1, 13, 1), range(1, 13, 1))
	plt.yticks(zero_to_one, zero_to_one)

plt.subplots_adjust(hspace=1)
plt.show()
