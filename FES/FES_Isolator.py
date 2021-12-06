import pandas as pd


def pre_processing(block_id, scenario):
	if block_id[0] == "D" and scenario[0] == "L":
		scenario = "Leading the Way"

	data_input = pd.read_csv("C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/FES-Block-Data.csv")

	isolated_scenario = data_input[data_input["FES Scenario"] == scenario]
	isolated_scenario_block = isolated_scenario[isolated_scenario["Building Block ID Number"] == block_id]

	counter = 0
	summed_values = []

	while counter < 30:
		if counter == 0:
			summed_values.append(sum(isolated_scenario_block["Baseline (2020)"]))
		else:
			year = str(2020 + counter)
			summed_values.append(sum(isolated_scenario_block[year]))

		counter += 1

	data_series = pd.Series(data=summed_values, index=range(2020, 2050, 1), name=scenario)

	return data_series


def block_data_packager(block_target):
	scenario_list = ["Leading The Way", "Consumer Transformation", "System Transformation", "Steady Progression"]

	scenario_frame = pd.DataFrame(index=range(2020, 2050, 1), columns=scenario_list)

	for scenarios in scenario_list:
		block_data = pre_processing(block_target, scenarios)

		scenario_frame[scenarios] = block_data

	return scenario_frame
