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

legend = ["Predicted Average Heat Demand", "Predicted Average Baseline Demand", "Predicted Average EV Demand",
		  "Range of Potential Heat Demand", "Range of Potential Baseline Demand"]

plt.subplot(2, 2, 1)
plt.fill_between(h_leading_the_way_day_max.index, h_leading_the_way_day_min.values, h_leading_the_way_day_max.values)
plt.fill_between(b_leading_the_way_day_max.index, b_leading_the_way_day_min.values, b_leading_the_way_day_max.values)

plt.plot(h_leading_the_way_day, color="black")
plt.plot(b_leading_the_way_day, color="red")
plt.plot(e_leading_the_way_day, color="green")

plt.title("Leading the Way")
plt.grid()
plt.xlabel("Date")
plt.ylabel("Demand (GWh / Day)")

plt.subplot(2, 2, 2)
plt.fill_between(h_consumer_transformation_day_min.index, h_consumer_transformation_day_min.values, h_consumer_transformation_day_max.values)
plt.fill_between(b_consumer_transformation_day_max.index, b_consumer_transformation_day_min.values, b_consumer_transformation_day_max.values)

plt.plot(h_consumer_transformation_day, color="black")
plt.plot(b_consumer_transformation_day, color="red")
plt.plot(e_consumer_transformation_day, color="green")

plt.title("Consumer Transformation")
plt.grid()
plt.xlabel("Date")
plt.ylabel("Demand (GWh / Day)")

plt.subplot(2, 2, 3)
plt.fill_between(h_system_transformation_day_min.index, h_system_transformation_day_min.values, h_system_transformation_day_max.values)
plt.fill_between(b_system_transformation_day_max.index, b_system_transformation_day_min.values, b_system_transformation_day_max.values)

plt.plot(h_system_transformation_day, color="black")
plt.plot(b_system_transformation_day, color="red")
plt.plot(e_system_transformation_day, color="green")

plt.title("System Transformation")
plt.grid()
plt.xlabel("Date")
plt.ylabel("Demand (GWh / Day)")

plt.subplot(2, 2, 4)
plt.fill_between(h_steady_progression_day_min.index, h_steady_progression_day_min.values, h_steady_progression_day_max.values)
plt.fill_between(b_steady_progression_day_max.index, b_steady_progression_day_min.values, b_steady_progression_day_max.values)

plt.plot(h_steady_progression_day, color="black")
plt.plot(b_steady_progression_day, color="red")
plt.plot(e_steady_progression_day, color="green")

plt.title("Steady Progression")
plt.grid()
plt.xlabel("Date")
plt.ylabel("Demand (GWh / Day)")

plt.figlegend(legend)
plt.suptitle("Individual Demand Profiles with Potential Ranges per Scenario", fontsize=20, x=0.40)
plt.subplots_adjust(hspace=0.5)

plt.show()
