from FES_Isolator import block_data_packager
from matplotlib import pyplot as plt

# Insert target block from excel list
legend_labels = ["Residential Leading The Way", "Residential Consumer Transformation",
				"Residential System Transformation", "Residential Steady Progression", "I&C Leading The Way",
				"I&C Consumer Transformation", "I&C System Transformation", "I&C Steady Progression"]

block_target_residential = "Dem_BB004"
scenario_frame_residential = block_data_packager(block_target_residential)

block_target_IC = "Dem_BB005"
scenario_frame_IC = block_data_packager(block_target_IC)

plt.plot(scenario_frame_residential)
plt.plot(scenario_frame_IC)

plt.legend(legend_labels, fontsize=15)
plt.grid()
plt.ylabel("Heating Electrical Demand (GWh)", fontsize=20)
plt.xlabel("Date", fontsize=20)
plt.title("Future Energy Scenario Heat Pump Demands", fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.show()
