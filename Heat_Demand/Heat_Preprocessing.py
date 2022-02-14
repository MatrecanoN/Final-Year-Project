import pandas as pd


def pre_processing():
	data_input = pd.read_csv(
		"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Heat Data.csv", delimiter=",")

	utc_date = (data_input["date"]).tolist()

	date_time_actual = pd.to_datetime(utc_date, format="%d/%m/%Y")

	heat_demand_raw = (data_input["GB_ldz_heat_from_natural_gas_kWh"]).tolist()
	heat_demand = pd.Series(data=heat_demand_raw, index=date_time_actual)

	return heat_demand
