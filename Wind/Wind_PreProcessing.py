import pandas as pd


def pre_processing():
	data_input = pd.read_csv(
		"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Clean Grid Data.csv", delimiter=",")
	wind_data = ((data_input["POWER_ELEXM_WIND_MW"] + data_input["POWER_NGEM_EMBEDDED_WIND_GENERATION_MW"]).tolist())
	utc_date_time = (data_input["ELEXM_utc"]).tolist()

	utc_date_time = [date_time.split("+", 1)[0] for date_time in utc_date_time]

	date_time_actual = pd.to_datetime(utc_date_time, format="%Y-%m-%dT%H:%M:%S")
	wind_data_series = pd.Series(data=wind_data, index=date_time_actual)

	installed_wind_capacity_raw = pd.read_csv(
		"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Interpolated Wind Capacity Data.csv", delimiter=",",
		squeeze=True)

	installed_wind_capacity = pd.Series(data=installed_wind_capacity_raw.tolist(), index=wind_data_series.index)

	power_demand_raw = (data_input["POWER_ESPENI_MW"]).tolist()
	power_demand = pd.Series(data=power_demand_raw, index=wind_data_series.index)
	power_demand_rolling = power_demand.rolling(17532, min_periods=1).mean()

	wind_raw_data_filtered = []
	wind_data_filtered_dates = []

	for dates in wind_data_series.index:
		if dates in installed_wind_capacity.index:
			calculated_value = wind_data_series[dates] / installed_wind_capacity[dates]
			wind_raw_data_filtered.append(calculated_value)
			wind_data_filtered_dates.append(dates)

	wind_data_filtered = pd.Series(data=wind_raw_data_filtered, index=wind_data_filtered_dates)

	wind_data_filtered = wind_data_filtered.iloc[20214:217398]

	return wind_data_filtered
