from FES_Isolator import block_data_packager
from matplotlib import pyplot as plt


def baseline_demand():
	# Insert target block from excel list
	block_target = "Dem_BB008"
	scenario_frame = block_data_packager(block_target)

	return scenario_frame


"""scenario_frame = baseline_demand()
plt.plot(scenario_frame)
plt.legend(scenario_frame.columns, fontsize=15)
plt.grid()
plt.ylabel("Total Baseline (Non-EV and Non-HP) Demand (GWh)", fontsize=15)
plt.xlabel("Date", fontsize=15)
plt.title("Future Energy Scenario Baseline Demands", fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.show()"""
