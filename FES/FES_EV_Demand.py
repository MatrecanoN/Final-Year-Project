from FES_Isolator import block_data_packager
from matplotlib import pyplot as plt

# Insert target block from excel list
legend_labels = ["Residential Leading The Way", "Residential Consumer Transformation",
				"Residential System Transformation", "Residential Steady Progression", "I&C Leading The Way",
				"I&C Consumer Transformation", "I&C System Transformation", "I&C Steady Progression"]

block_target_residential = "Dem_BB006"
scenario_frame_residential = block_data_packager(block_target_residential)

block_target_IC = "Dem_BB007"
scenario_frame_IC = block_data_packager(block_target_IC)

plt.plot(scenario_frame_residential)
plt.plot(scenario_frame_IC)
plt.legend(legend_labels, fontsize=15)
plt.ylabel("Transport Electricity Demand (GWh)", fontsize=20)
plt.xlabel("Date", fontsize=20)
plt.grid()
plt.title("Future Energy Scenario Electric Vehicle Demands", fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.show()


