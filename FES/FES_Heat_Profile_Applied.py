from FES_Isolator import block_data_packager
from matplotlib import pyplot as plt
import pandas as pd
from datetime import datetime


def heat_demand_profiled():
	# Insert target block from excel list
	block_target_residential = "Dem_BB004"
	scenario_frame_residential = block_data_packager(block_target_residential)

	block_target_IC = "Dem_BB005"
	scenario_frame_IC = block_data_packager(block_target_IC)

	scenario_frame_combined = scenario_frame_IC + scenario_frame_residential

	data_input_leap = pd.read_csv(
		"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Average Year Heat Data Leap.csv", delimiter=",",
		index_col=0, squeeze=True)

	data_input_non_leap = pd.read_csv(
		"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Average Year Heat Data Non-Leap.csv",
		delimiter=",",
		index_col=0, squeeze=True)

	leap_years = [2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]

	leading_the_way_annual = scenario_frame_combined["Leading The Way"]
	consumer_transformation_annual = scenario_frame_combined["Consumer Transformation"]
	system_transformation_annual = scenario_frame_combined["System Transformation"]
	steady_progression_annual = scenario_frame_combined["Steady Progression"]

	leading_the_way_day = pd.Series()
	consumer_transformation_day = pd.Series()
	system_transformation_day = pd.Series()
	steady_progression_day = pd.Series()

	for years in scenario_frame_combined.index:
		if years not in leap_years:
			current_year_l = pd.Series(data=(data_input_non_leap.values / 100) * leading_the_way_annual[years],
									   index=data_input_non_leap.index + "-" + str(years))
			current_year_c = pd.Series(data=(data_input_non_leap.values / 100) * consumer_transformation_annual[years],
									   index=data_input_non_leap.index + "-" + str(years))
			current_year_sy = pd.Series(data=(data_input_non_leap.values / 100) * system_transformation_annual[years],
										index=data_input_non_leap.index + "-" + str(years))
			current_year_st = pd.Series(data=(data_input_non_leap.values / 100) * steady_progression_annual[years],
										index=data_input_non_leap.index + "-" + str(years))

		else:
			current_year_l = pd.Series(data=(data_input_leap.values / 100) * leading_the_way_annual[years],
									   index=data_input_leap.index + "-" + str(years))
			current_year_c = pd.Series(data=(data_input_leap.values / 100) * consumer_transformation_annual[years],
									   index=data_input_leap.index + "-" + str(years))
			current_year_sy = pd.Series(data=(data_input_leap.values / 100) * system_transformation_annual[years],
										index=data_input_leap.index + "-" + str(years))
			current_year_st = pd.Series(data=(data_input_leap.values / 100) * steady_progression_annual[years],
										index=data_input_leap.index + "-" + str(years))

		leading_the_way_day = leading_the_way_day.append(current_year_l)
		consumer_transformation_day = consumer_transformation_day.append(current_year_c)
		system_transformation_day = system_transformation_day.append(current_year_sy)
		steady_progression_day = steady_progression_day.append(current_year_st)

	leading_the_way_index = []
	consumer_transformation_index = []
	system_transformation_index = []
	steady_progression_index = []

	for count in range(0, len(leading_the_way_day.index), 1):
		leading_the_way_index.append(datetime.strptime(leading_the_way_day.index[count], "%m-%d-%Y"))
		consumer_transformation_index.append(datetime.strptime(consumer_transformation_day.index[count], "%m-%d-%Y"))
		system_transformation_index.append(datetime.strptime(system_transformation_day.index[count], "%m-%d-%Y"))
		steady_progression_index.append(datetime.strptime(steady_progression_day.index[count], "%m-%d-%Y"))

	leading_the_way_day = pd.Series(data=leading_the_way_day.values, index=leading_the_way_index)
	consumer_transformation_day = pd.Series(data=consumer_transformation_day.values,
											index=consumer_transformation_index)
	system_transformation_day = pd.Series(data=system_transformation_day.values, index=system_transformation_index)
	steady_progression_day = pd.Series(data=steady_progression_day.values, index=steady_progression_index)

	return leading_the_way_day, consumer_transformation_day, system_transformation_day, steady_progression_day


"""leading_the_way_day, consumer_transformation_day, system_transformation_day, steady_progression_day = heat_demand_profiled()
plt.subplot(2, 2, 1)
plt.plot(leading_the_way_day)
plt.grid()
plt.title("Leading the Way")
plt.xlabel("Date")
plt.ylabel("Demand (GWh / Day)")

plt.subplot(2, 2, 2)
plt.plot(consumer_transformation_day)
plt.grid()
plt.title("Consumer Transformation")
plt.xlabel("Date")
plt.ylabel("Demand (GWh / Day)")

plt.subplot(2, 2, 3)
plt.plot(system_transformation_day)
plt.grid()
plt.title("System Transformation")
plt.xlabel("Date")
plt.ylabel("Demand (GWh / Day)")

plt.subplot(2, 2, 4)
plt.plot(steady_progression_day)
plt.grid()
plt.title("Steady Progression")
plt.xlabel("Date")
plt.ylabel("Demand (GWh / Day)")


plt.suptitle("FES HP Power Demand Predictions with Historic Seasonal Profile Applied", fontsize=20)
plt.subplots_adjust(hspace=0.5)

plt.show()
"""