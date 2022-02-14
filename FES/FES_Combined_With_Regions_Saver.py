from FES_Heat_Profile_Applied import heat_demand_profiled
from FES_Demand_Profile_Applied import electrical_demand_profiled
from FES_EV_Demand_Model_Applied import ev_demand_profile
import pandas as pd
from matplotlib import pyplot as plt

heat_max = 1.5863541573352165
heat_min = 0.5300951217192832

baseline_max = 1.1981087787650941
baseline_min = 0.8082864994032962

b_leading_the_way_day, b_consumer_transformation_day, b_system_transformation_day, b_steady_progression_day = \
	electrical_demand_profiled()

h_leading_the_way_day, h_consumer_transformation_day, h_system_transformation_day, h_steady_progression_day = \
	heat_demand_profiled()

e_leading_the_way_day, e_consumer_transformation_day, e_system_transformation_day, e_steady_progression_day = \
	ev_demand_profile()

combined_leading_the_way = b_leading_the_way_day + h_leading_the_way_day + e_leading_the_way_day
combined_consumer_transformation = b_consumer_transformation_day + h_consumer_transformation_day + e_consumer_transformation_day
combined_system_transformation = b_system_transformation_day + h_system_transformation_day + e_system_transformation_day
combined_steady_progression = b_steady_progression_day + h_steady_progression_day + e_steady_progression_day

b_leading_the_way_day_max = b_leading_the_way_day * baseline_max
b_consumer_transformation_day_max = b_consumer_transformation_day * baseline_max
b_system_transformation_day_max = b_system_transformation_day * baseline_max
b_steady_progression_day_max = b_steady_progression_day * baseline_max

b_leading_the_way_day_min = b_leading_the_way_day * baseline_min
b_consumer_transformation_day_min = b_consumer_transformation_day * baseline_min
b_system_transformation_day_min = b_system_transformation_day * baseline_min
b_steady_progression_day_min = b_steady_progression_day * baseline_min

h_leading_the_way_day_max = h_leading_the_way_day * heat_max
h_consumer_transformation_day_max = h_consumer_transformation_day * heat_max
h_system_transformation_day_max = h_system_transformation_day * heat_max
h_steady_progression_day_max = h_steady_progression_day * heat_max

h_leading_the_way_day_min = h_leading_the_way_day * heat_min
h_consumer_transformation_day_min = h_consumer_transformation_day * heat_min
h_system_transformation_day_min = h_system_transformation_day * heat_min
h_steady_progression_day_min = h_steady_progression_day * heat_min

c_leading_the_way_day_min = b_leading_the_way_day_min + h_leading_the_way_day_min + e_leading_the_way_day
c_consumer_transformation_day_min = b_consumer_transformation_day_min + h_consumer_transformation_day_min + e_consumer_transformation_day
c_system_transformation_day_min = b_system_transformation_day_min + h_system_transformation_day_min + e_system_transformation_day
c_steady_progression_day_min = b_steady_progression_day_min + h_steady_progression_day_min + e_steady_progression_day

c_leading_the_way_day_max = b_leading_the_way_day_max + h_leading_the_way_day_max + e_leading_the_way_day
c_consumer_transformation_day_max = b_consumer_transformation_day_max + h_consumer_transformation_day_max + e_consumer_transformation_day
c_system_transformation_day_max = b_system_transformation_day_max + h_system_transformation_day_max + e_system_transformation_day
c_steady_progression_day_max = b_steady_progression_day_max + h_steady_progression_day_max + e_steady_progression_day

print("STOP")
c_leading_the_way_day_min = c_leading_the_way_day_min.loc["2050-01-01":"2050-12-31"]
c_consumer_transformation_day_min = c_consumer_transformation_day_min.loc["2050-01-01":"2050-12-31"]
c_system_transformation_day_min = c_system_transformation_day_min.loc["2050-01-01":"2050-12-31"]
c_steady_progression_day_min = c_steady_progression_day_min.loc["2050-01-01":"2050-12-31"]

c_leading_the_way_day_max = c_leading_the_way_day_max.loc["2050-01-01":"2050-12-31"]
c_consumer_transformation_day_max = c_consumer_transformation_day_max.loc["2050-01-01":"2050-12-31"]
c_system_transformation_day_max = c_system_transformation_day_max.loc["2050-01-01":"2050-12-31"]
c_steady_progression_day_max = c_steady_progression_day_max.loc["2050-01-01":"2050-12-31"]

combined_leading_the_way = combined_leading_the_way.loc["2050-01-01":"2050-12-31"]
combined_consumer_transformation = combined_consumer_transformation.loc["2050-01-01":"2050-12-31"]
combined_system_transformation = combined_system_transformation.loc["2050-01-01":"2050-12-31"]
combined_steady_progression = combined_steady_progression.loc["2050-01-01":"2050-12-31"]

save_data = {"c_leading_the_way_day_min": c_leading_the_way_day_min, "c_consumer_transformation_day_min": c_consumer_transformation_day_min,
			"c_system_transformation_day_min": c_system_transformation_day_min, "c_steady_progression_day_min": c_steady_progression_day_min,
			 "c_leading_the_way_day_max": c_leading_the_way_day_max, "c_consumer_transformation_day_max": c_consumer_transformation_day_max,
			 "c_system_transformation_day_max": c_system_transformation_day_max, "c_steady_progression_day_max": c_steady_progression_day_max,
			 "combined_leading_the_way": combined_leading_the_way, "combined_consumer_transformation": combined_consumer_transformation,
			 "combined_system_transformation": combined_system_transformation, "combined_steady_progression": combined_steady_progression}

export = pd.DataFrame.from_dict(save_data)
print("STOP")