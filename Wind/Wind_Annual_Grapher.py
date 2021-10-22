from matplotlib import pyplot as plt
from Wind_PreProcessing import pre_processing
from Helpers.Yearly_Splicer import yearly_splicer

wind_data = pre_processing()
annual_data = yearly_splicer(wind_data)

years_graphed = []

for years in annual_data:
	if 2015 < years < 2018:
		plt.plot(annual_data[years])
		years_graphed.append(years)

plt.legend(years_graphed)
plt.show()
