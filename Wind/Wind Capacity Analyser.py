from matplotlib import pyplot as plt
import datetime
import pandas as pd
import numpy

data_input = pd.read_csv(
	"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Clean Grid Data.csv", delimiter=",")
wind_data = ((data_input["POWER_ELEXM_WIND_MW"] + data_input["POWER_NGEM_EMBEDDED_WIND_GENERATION_MW"]).tolist())
utc_date_time = (data_input["ELEXM_utc"]).tolist()

utc_date_time = [date_time.split("+", 1)[0] for date_time in utc_date_time]

date_time_actual = pd.to_datetime(utc_date_time, format="%Y-%m-%dT%H:%M:%S")
wind_data_series = pd.Series(data=wind_data, index=date_time_actual)
wind_capacity_data = pd.read_csv(
	"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Quarterly Wind Capacity Data.csv", delimiter=",")
wind_capacity_raw_data = []
wind_capacity_dates = []
combined_date_month = ""

installed_wind_capacity = pd.Series(index=wind_data_series.index)
for dates in wind_data_series.index:
	month = dates.month
	year = dates.year
	day = dates.day
	if month == 3 and day == 31:
		combined_date_month = str(year) + "-1"

	elif month == 6 and day == 30:
		combined_date_month = str(year) + "-2"

	elif month == 9 and day == 30:
		combined_date_month = str(year) + "-3"

	elif month == 12 and day == 31:
		combined_date_month = str(year) + "-4"

	else:
		combined_date_month = "Do Not Index"

	if combined_date_month in wind_capacity_data.columns:
		installed_wind_capacity[dates] = wind_capacity_data[combined_date_month].values[0]

first_date_data_date = installed_wind_capacity.iloc[0:].first_valid_index()
midnights = first_date_data_date
installed_wind_capacity.iloc[0] = installed_wind_capacity[midnights]
amount_to_add = 0

while midnights in installed_wind_capacity.index:
	time_minus_30 = midnights - datetime.timedelta(minutes=30)
	time_plus_30 = midnights + datetime.timedelta(minutes=30)

	if numpy.isnan(installed_wind_capacity[midnights]) and not numpy.isnan(installed_wind_capacity[time_minus_30]):
		current_index = installed_wind_capacity.index.get_loc(midnights)
		next_data_date = installed_wind_capacity.iloc[current_index:].first_valid_index()

		if next_data_date is not None:
			next_data = installed_wind_capacity[next_data_date]
			range_difference = next_data_date - midnights
			amount_to_add = (next_data - installed_wind_capacity[time_minus_30]) / (range_difference.days + 1)
			installed_wind_capacity[midnights] = amount_to_add + installed_wind_capacity[time_minus_30]

	elif not numpy.isnan(installed_wind_capacity[time_plus_30]):
		installed_wind_capacity[midnights] = installed_wind_capacity[time_plus_30]

	else:
		installed_wind_capacity[midnights] = installed_wind_capacity[
												midnights - datetime.timedelta(days=1)] + amount_to_add

	midnights += datetime.timedelta(days=1)

for dates in installed_wind_capacity.index:
	if numpy.isnan(installed_wind_capacity[dates]):
		installed_wind_capacity[dates] = installed_wind_capacity[dates - datetime.timedelta(minutes=30)]

plt.plot(installed_wind_capacity)
plt.show()

installed_wind_capacity.to_csv(
	"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Interpolated Wind Capacity Data.csv", index=False)
