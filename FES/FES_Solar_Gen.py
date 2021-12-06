from FES_Isolator import block_data_packager
from matplotlib import pyplot as plt

# Insert target block from excel list
legend_labels = ["Large Leading The Way", "Large Consumer Transformation",
				"Large System Transformation", "Large Steady Progression", "Small Leading The Way",
				"Small Consumer Transformation", "Small System Transformation", "Small Steady Progression"]

block_target_large = "Gen_BB012"
scenario_frame_large = block_data_packager(block_target_large)

block_target_small = "Gen_BB013"
scenario_frame_small = block_data_packager(block_target_small)

plt.plot(scenario_frame_large)
plt.plot(scenario_frame_small)
plt.legend(legend_labels)
plt.grid()

plt.show()
