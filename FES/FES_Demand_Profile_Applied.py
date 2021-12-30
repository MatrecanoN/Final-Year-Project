import pandas as pd
from FES_Baseline_Demand import baseline_demand as baseline_demand
from datetime import datetime
from matplotlib import pyplot as plt

data_input_leap = pd.read_csv(
	"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Average Year Demand Data Leap.csv", delimiter=",",
	index_col=0, squeeze=True)

data_input_non_leap = pd.read_csv(
	"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Average Year Demand Data Non-Leap.csv", delimiter=",",
	index_col=0, squeeze=True)

leap_years = [2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]

demand_block = baseline_demand()
leading_the_way_annual = demand_block["Leading The Way"]
consumer_transformation_annual = demand_block["Consumer Transformation"]
system_transformation_annual = demand_block["System Transformation"]
steady_progression_annual = demand_block["Steady Progression"]

leading_the_way_day = pd.Series()
consumer_transformation_day = pd.Series()
system_transformation_day = pd.Series()
steady_progression_day = pd.Series()

for years in demand_block.index:
	if years not in leap_years:
		current_year_l = pd.Series(data=data_input_non_leap.values * leading_the_way_annual[years], index=data_input_non_leap.index + "-" + str(years))
		current_year_c = pd.Series(data=data_input_non_leap.values * consumer_transformation_annual[years], index=data_input_non_leap.index + "-" + str(years))
		current_year_sy = pd.Series(data=data_input_non_leap.values * system_transformation_annual[years], index=data_input_non_leap.index + "-" + str(years))
		current_year_st = pd.Series(data=data_input_non_leap.values * steady_progression_annual[years], index=data_input_non_leap.index + "-" + str(years))

	else:
		current_year_l = pd.Series(data=data_input_leap.values * leading_the_way_annual[years], index=data_input_leap.index + "-" + str(years))
		current_year_c = pd.Series(data=data_input_leap.values * consumer_transformation_annual[years], index=data_input_leap.index + "-" + str(years))
		current_year_sy = pd.Series(data=data_input_leap.values * system_transformation_annual[years], index=data_input_leap.index + "-" + str(years))
		current_year_st = pd.Series(data=data_input_leap.values * steady_progression_annual[years], index=data_input_leap.index + "-" + str(years))

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
consumer_transformation_day = pd.Series(data=consumer_transformation_day.values, index=consumer_transformation_index)
system_transformation_day = pd.Series(data=system_transformation_day.values, index=system_transformation_index)
steady_progression_day = pd.Series(data=steady_progression_day.values, index=steady_progression_index)

plt.plot(leading_the_way_day)
plt.plot(consumer_transformation_day)
plt.plot(system_transformation_day)
plt.plot(steady_progression_day)

plt.show()
