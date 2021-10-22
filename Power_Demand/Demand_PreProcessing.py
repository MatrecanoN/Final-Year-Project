import pandas as pd


def pre_processing():
	data_input = pd.read_csv(
		"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Clean Grid Data.csv", delimiter=",")

	utc_date_time = (data_input["ELEXM_utc"]).tolist()

	utc_date_time = [date_time.split("+", 1)[0] for date_time in utc_date_time]

	date_time_actual = pd.to_datetime(utc_date_time, format="%Y-%m-%dT%H:%M:%S")

	power_demand_raw = (data_input["POWER_ESPENI_MW"]).tolist()
	power_demand = pd.Series(data=power_demand_raw, index=date_time_actual)

	return power_demand
