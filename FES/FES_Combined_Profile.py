from FES_Heat_Profile_Applied import heat_demand_profiled
from FES_Demand_Profile_Applied import electrical_demand_profiled
from FES_EV_Demand_Model_Applied import ev_demand_profile
import pandas as pd
from matplotlib import pyplot as plt

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

plt.subplot(2, 2, 1)
plt.plot(combined_leading_the_way)
plt.grid()
plt.title("Leading the Way")
plt.xlabel("Date")
plt.ylabel("Demand (GWh / Day)")

plt.subplot(2, 2, 2)
plt.plot(combined_consumer_transformation)
plt.grid()
plt.title("Consumer Transformation")
plt.xlabel("Date")
plt.ylabel("Demand (GWh / Day)")

plt.subplot(2, 2, 3)
plt.plot(combined_system_transformation)
plt.grid()
plt.title("System Transformation")
plt.xlabel("Date")
plt.ylabel("Demand (GWh / Day)")

plt.subplot(2, 2, 4)
plt.plot(combined_steady_progression)
plt.grid()
plt.title("Steady Progression")
plt.xlabel("Date")
plt.ylabel("Demand (GWh / Day)")


plt.suptitle("FES Total Power Demand Predictions with Historic Seasonal Profile Applied", fontsize=20)
plt.subplots_adjust(hspace=0.5)

plt.show()
