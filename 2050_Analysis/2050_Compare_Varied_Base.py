import pandas as pd
from matplotlib import pyplot as plt

import_demand = pd.read_csv("C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/2050 Averages or Data/Demand Data.csv", parse_dates=True, index_col="Unnamed: 0")
import_wind_average = pd.read_csv("C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/2050 Averages or Data/Wind Average Year Data.csv", index_col="Unnamed: 0")

wind_average = import_wind_average["Average"]

combined_leading_the_way = import_demand["combined_leading_the_way"]
combined_consumer_transformation = import_demand["combined_consumer_transformation"]
combined_system_transformation = import_demand["combined_system_transformation"]
combined_steady_progression = import_demand["combined_steady_progression"]

wind_average = pd.Series(data=wind_average.values, index=combined_leading_the_way.index)

# Input in GW
installed_capacity = range(10, 55, 5)
wind_capacity = 100
average_annual_utilisation = 27.97757747317708 / 100
baseline_generation = pd.Series(index=installed_capacity)

for capacity in installed_capacity:
	baseline_generation[capacity] = capacity * 24

# Outputs annual total expected in GWh/day
average_annual_generation = (wind_capacity * 8760) * average_annual_utilisation
applied_wind_average = pd.Series(data=((wind_average.values / 100) * average_annual_generation), index=wind_average.index)

balance_leading = pd.DataFrame()
balance_c_transformation = pd.DataFrame()
balance_s_transformation = pd.DataFrame()
balance_steady = pd.DataFrame()

for capacity in installed_capacity:
	balance_leading[capacity] = applied_wind_average + baseline_generation[capacity] - combined_leading_the_way
	balance_c_transformation[capacity] = applied_wind_average + baseline_generation[capacity] - combined_consumer_transformation
	balance_s_transformation[capacity] = applied_wind_average + baseline_generation[capacity] - combined_system_transformation
	balance_steady[capacity] = applied_wind_average + baseline_generation[capacity] - combined_steady_progression

storage_leading = pd.DataFrame()
storage_c_transformation = pd.DataFrame()
storage_s_transformation = pd.DataFrame()
storage_steady = pd.DataFrame()

wasted_leading = pd.DataFrame()
wasted_c_transformation = pd.DataFrame()
wasted_s_transformation = pd.DataFrame()
wasted_steady = pd.DataFrame()

previous_date = "blank"
end_date = balance_leading[20].index[-1]
counter = 0

electrolysis_efficiency = 7 / 10 	# 70% Efficient
combustion_efficiency = 10 / 6 		# 60% Efficient but >100% as it takes more storage

for capacity in installed_capacity:
	for dates in balance_leading.index:
		if previous_date == "blank":
			storage_leading_series = pd.Series()
			storage_c_transformation_series = pd.Series()
			storage_s_transformation_series = pd.Series()
			storage_steady_series = pd.Series()

			wasted_leading_series = pd.Series()
			wasted_c_transformation_series = pd.Series()
			wasted_s_transformation_series = pd.Series()
			wasted_steady_series = pd.Series()

			counter += 1
			print(counter)

			if balance_leading[capacity][dates] < 0:
				storage_leading_series = storage_leading_series.append(
					pd.Series(data=balance_leading[capacity][dates] * combustion_efficiency, index=[dates]))
			else:
				storage_leading_series = storage_leading_series.append(
					pd.Series(data=balance_leading[capacity][dates] * electrolysis_efficiency, index=[dates]))

			if balance_c_transformation[capacity][dates] < 0:
				storage_c_transformation_series = storage_c_transformation_series.append(
					pd.Series(data=balance_c_transformation[capacity][dates] * combustion_efficiency, index=[dates]))
			else:
				storage_c_transformation_series = storage_c_transformation_series.append(
					pd.Series(data=balance_c_transformation[capacity][dates] * electrolysis_efficiency, index=[dates]))

			if balance_s_transformation[capacity][dates] < 0:
				storage_s_transformation_series = storage_s_transformation_series.append(
					pd.Series(data=balance_s_transformation[capacity][dates] * combustion_efficiency, index=[dates]))
			else:
				storage_s_transformation_series = storage_s_transformation_series.append(
					pd.Series(data=balance_s_transformation[capacity][dates] * electrolysis_efficiency, index=[dates]))

			if balance_steady[capacity][dates] < 0:
				storage_steady_series = storage_steady_series.append(
					pd.Series(data=balance_steady[capacity][dates] * combustion_efficiency, index=[dates]))
			else:
				storage_steady_series = storage_steady_series.append(
					pd.Series(data=balance_steady[capacity][dates] * electrolysis_efficiency, index=[dates]))

			if storage_leading_series[dates] > 0:
				wasted_leading_series[dates] = storage_leading_series[dates]
				storage_leading_series[dates] = 0
			else:
				wasted_leading_series[dates] = 0

			if storage_c_transformation_series[dates] > 0:
				wasted_c_transformation_series[dates] = storage_c_transformation_series[dates]
				storage_c_transformation_series[dates] = 0
			else:
				wasted_c_transformation_series[dates] = 0

			if storage_s_transformation_series[dates] > 0:
				wasted_s_transformation_series[dates] = storage_s_transformation_series[dates]
				storage_s_transformation_series[dates] = 0
			else:
				wasted_s_transformation_series[dates] = 0

			if storage_steady_series[dates] > 0:
				wasted_steady_series[dates] = storage_steady_series[dates]
				storage_steady_series[dates] = 0
			else:
				wasted_steady_series[dates] = 0

		else:
			if balance_leading[capacity][dates] < 0:
				storage_leading_series = storage_leading_series.append(
					pd.Series(data=storage_leading_series[previous_date] + (balance_leading[capacity][dates] *
																			combustion_efficiency), index=[dates]))
			else:
				storage_leading_series = storage_leading_series.append(
					pd.Series(data=storage_leading_series[previous_date] + (balance_leading[capacity][dates] *
																			electrolysis_efficiency), index=[dates]))

			if balance_c_transformation[capacity][dates] < 0:
				storage_c_transformation_series = storage_c_transformation_series.append(
					pd.Series(data=storage_c_transformation_series[previous_date] + (
							balance_c_transformation[capacity][dates] * combustion_efficiency), index=[dates]))
			else:
				storage_c_transformation_series = storage_c_transformation_series.append(
					pd.Series(data=storage_c_transformation_series[previous_date] + (
							balance_c_transformation[capacity][dates] * electrolysis_efficiency), index=[dates]))

			if balance_s_transformation[capacity][dates] < 0:
				storage_s_transformation_series = storage_s_transformation_series.append(
					pd.Series(data=storage_s_transformation_series[previous_date] + (
						balance_s_transformation[capacity][dates] * combustion_efficiency), index=[dates]))
			else:
				storage_s_transformation_series = storage_s_transformation_series.append(
					pd.Series(data=storage_s_transformation_series[previous_date] + (
							balance_s_transformation[capacity][dates] * electrolysis_efficiency), index=[dates]))

			if balance_steady[capacity][dates] < 0:
				storage_steady_series = storage_steady_series.append(
					pd.Series(data=storage_steady_series[previous_date] + (
							balance_steady[capacity][dates] * combustion_efficiency), index=[dates]))
			else:
				storage_steady_series = storage_steady_series.append(
					pd.Series(data=storage_steady_series[previous_date] + (
							balance_steady[capacity][dates] * electrolysis_efficiency), index=[dates]))

			if storage_leading_series[dates] > 0:
				wasted_leading_series[dates] = storage_leading_series[dates] + wasted_leading_series[previous_date]
				storage_leading_series[dates] = 0
			else:
				wasted_leading_series[dates] = wasted_leading_series[previous_date]

			if storage_c_transformation_series[dates] > 0:
				wasted_c_transformation_series[dates] = storage_c_transformation_series[dates] + wasted_c_transformation_series[previous_date]
				storage_c_transformation_series[dates] = 0
			else:
				wasted_c_transformation_series[dates] = wasted_c_transformation_series[previous_date]

			if storage_s_transformation_series[dates] > 0:
				wasted_s_transformation_series[dates] = storage_s_transformation_series[dates] + wasted_s_transformation_series[previous_date]
				storage_s_transformation_series[dates] = 0
			else:
				wasted_s_transformation_series[dates] = wasted_s_transformation_series[previous_date]

			if storage_steady_series[dates] > 0:
				wasted_steady_series[dates] = storage_steady_series[dates] + wasted_steady_series[previous_date]
				storage_steady_series[dates] = 0
			else:
				wasted_steady_series[dates] = wasted_steady_series[previous_date]

		previous_date = dates

		if dates == end_date:
			previous_date = "blank"

	storage_leading[capacity] = storage_leading_series
	storage_c_transformation[capacity] = storage_c_transformation_series
	storage_s_transformation[capacity] = storage_s_transformation_series
	storage_steady[capacity] = storage_steady_series

	wasted_leading[capacity] = wasted_leading_series
	wasted_c_transformation[capacity] = wasted_c_transformation_series
	wasted_s_transformation[capacity] = wasted_s_transformation_series
	wasted_steady[capacity] = wasted_steady_series


storage_leading_min = (storage_leading.min() * -1)
storage_c_transformation_min = (storage_c_transformation.min() * -1)
storage_s_transformation_min = (storage_s_transformation.min() * -1)
storage_steady_min = (storage_steady.min() * -1)

for index in storage_leading_min.index:
	if storage_leading_min[index] < 0:
		storage_leading_min[index] = 0

	if storage_c_transformation_min[index] < 0:
		storage_c_transformation_min[index] = 0

	if storage_s_transformation_min[index] < 0:
		storage_s_transformation_min[index] = 0

	if storage_steady_min[index] < 0:
		storage_steady_min[index] = 0

legend = ["Leading the Way", "Consumer Transformation", "System Transformation", "Steady Progression", "Salt Cavern Storage Maximum"]
plt.plot(storage_leading_min)
plt.plot(storage_c_transformation_min)
plt.plot(storage_s_transformation_min)
plt.plot(storage_steady_min)

plt.legend(legend)
plt.grid()

plt.show()
