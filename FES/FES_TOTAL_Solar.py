from FES_Isolator import block_data_packager
from matplotlib import pyplot as plt

# Insert target block from excel list
block_target_large = "Gen_BB012"
scenario_frame_large = block_data_packager(block_target_large)

block_target_small = "Gen_BB013"
scenario_frame_small = block_data_packager(block_target_small)

scenario_frame_collected = scenario_frame_large.append(scenario_frame_small)
scenario_frame_summed = scenario_frame_collected.groupby(level=0).sum()

plt.plot(scenario_frame_summed)
plt.legend(scenario_frame_summed.columns)
plt.grid()
plt.ylabel("Solar Installed Capacity (MW)")
plt.xlabel("Year")
plt.title("Future Energy Scenario Total Solar Generator Installed Capacity")

plt.show()
