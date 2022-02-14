from FES_Isolator import block_data_packager
import pandas as pd
from FES_Demand_Profile_Applied import electrical_demand_profiled
from matplotlib import pyplot as plt


def ev_demand_profile():
	b_leading_the_way_day, b_consumer_transformation_day, b_system_transformation_day, b_steady_progression_day = \
		electrical_demand_profiled()

	block_target_residential = "Dem_BB006"
	scenario_frame_residential = block_data_packager(block_target_residential)

	block_target_IC = "Dem_BB007"
	scenario_frame_IC = block_data_packager(block_target_IC)

	ev_combined_frame = scenario_frame_IC + scenario_frame_residential

	e_leading_the_way_day = pd.Series()
	e_consumer_transformation_day = pd.Series()
	e_system_transformation_day = pd.Series()
	e_steady_progression_day = pd.Series()

	leap_years = [2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]

	for dates in b_leading_the_way_day.index:
		if dates.year not in leap_years:
			e_leading_the_way_day[dates] = (ev_combined_frame["Leading The Way"][dates.year] / 8760) * 24
			e_consumer_transformation_day[dates] = (ev_combined_frame["Consumer Transformation"][dates.year] / 8760) * 24
			e_system_transformation_day[dates] = (ev_combined_frame["System Transformation"][dates.year] / 8760) * 24
			e_steady_progression_day[dates] = (ev_combined_frame["Steady Progression"][dates.year] / 8760) * 24

		else:
			e_leading_the_way_day[dates] = (ev_combined_frame["Leading The Way"][dates.year] / 8784) * 24
			e_consumer_transformation_day[dates] = (ev_combined_frame["Consumer Transformation"][dates.year] / 8784) * 24
			e_system_transformation_day[dates] = (ev_combined_frame["System Transformation"][dates.year] / 8784) * 24
			e_steady_progression_day[dates] = (ev_combined_frame["Steady Progression"][dates.year] / 8784) * 24

	return e_leading_the_way_day, e_consumer_transformation_day, e_system_transformation_day, e_steady_progression_day

"""e_leading_the_way_day, e_consumer_transformation_day, e_system_transformation_day, e_steady_progression_day = ev_demand_profile()

plt.plot(e_leading_the_way_day)
plt.plot(e_consumer_transformation_day)
plt.plot(e_system_transformation_day)
plt.plot(e_steady_progression_day)

legend = ["Leading the Way", "Consumer Transformation", "System Transformation", "Steady Progression"]
plt.legend(legend, fontsize=16)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel("Date", fontsize=20)
plt.ylabel("Power Demand (GWh / Day)", fontsize=20)
plt.title("Power Demand per Day from EV Usage", fontsize=20)
plt.grid()
print("stop")
"""