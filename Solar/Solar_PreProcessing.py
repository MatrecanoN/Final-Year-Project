import pandas as pd


def pre_processing():
	data_input = pd.read_csv(
		"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Clean Grid Data.csv", delimiter=",")
	solar_data = ((data_input["POWER_NGEM_EMBEDDED_SOLAR_GENERATION_MW"]).tolist())
	utc_date_time = (data_input["ELEXM_utc"]).tolist()

	utc_date_time = [date_time.split("+", 1)[0] for date_time in utc_date_time]

	date_time_actual = pd.to_datetime(utc_date_time, format="%Y-%m-%dT%H:%M:%S")
	solar_data_series = pd.Series(data=solar_data, index=date_time_actual)

	installed_solar_capacity_raw = pd.read_csv(
		"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Interpolated Solar Capacity Data.csv",
		delimiter=",", squeeze=True)

	installed_solar_capacity = pd.Series(data=installed_solar_capacity_raw.tolist(), index=solar_data_series.index)

	solar_raw_data_filtered = []
	solar_data_filtered_dates = []

	for dates in solar_data_series.index:
		if dates in installed_solar_capacity.index:
			calculated_value = solar_data_series[dates] / installed_solar_capacity[dates]
			solar_raw_data_filtered.append(calculated_value)
			solar_data_filtered_dates.append(dates)

	solar_data_filtered = pd.Series(data=solar_raw_data_filtered, index=solar_data_filtered_dates)

	solar_data_filtered = solar_data_filtered.iloc[20214:217398]

	return solar_data_filtered
