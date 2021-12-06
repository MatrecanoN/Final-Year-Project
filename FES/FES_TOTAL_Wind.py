from FES_Isolator import block_data_packager
from matplotlib import pyplot as plt

# Insert target block from excel list
block_target_off = "Gen_BB014"
scenario_frame_off = block_data_packager(block_target_off)

block_target_large_on = "Gen_BB015"
scenario_frame_large_on = block_data_packager(block_target_large_on)

block_target_small_on = "Gen_BB016"
scenario_frame_small_on = block_data_packager(block_target_small_on)

scenario_frame_collected = scenario_frame_large_on.append(scenario_frame_small_on).append(scenario_frame_off)
scenario_frame_summed = scenario_frame_collected.groupby(level=0).sum()

plt.plot(scenario_frame_summed)
plt.legend(scenario_frame_summed.columns)
plt.grid()

plt.show()
