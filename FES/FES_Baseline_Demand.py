from FES_Isolator import block_data_packager
from matplotlib import pyplot as plt

# Insert target block from excel list
block_target = "Dem_BB008"
scenario_frame = block_data_packager(block_target)

plt.plot(scenario_frame)
plt.legend(scenario_frame.columns)
plt.grid()

plt.show()
