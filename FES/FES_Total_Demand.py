from FES_Isolator import block_data_packager
from matplotlib import pyplot as plt

# Insert target block from excel list
block_target = "Dem_BB003"

scenario_frame = block_data_packager(block_target)

plt.plot(scenario_frame / 365)
plt.legend(scenario_frame.columns, fontsize=18)
plt.grid()
plt.ylabel("Total Demand (GWh / Day)", fontsize=20)
plt.xlabel("Date", fontsize=20)
plt.title("Future Energy Scenario Combined Demand Predictions - FES Data Only", fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.show()
