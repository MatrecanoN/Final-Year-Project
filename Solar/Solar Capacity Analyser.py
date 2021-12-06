from matplotlib import pyplot as plt
import datetime
import pandas as pd
import numpy

data_input = pd.read_csv(
	"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Clean Grid Data.csv", delimiter=",")
solar_data = ((data_input["POWER_NGEM_EMBEDDED_SOLAR_GENERATION_MW"]).tolist())  # Only integrated? Cant be right
utc_date_time = (data_input["ELEXM_utc"]).tolist()

utc_date_time = [date_time.split("+", 1)[0] for date_time in utc_date_time]

date_time_actual = pd.to_datetime(utc_date_time, format="%Y-%m-%dT%H:%M:%S")
solar_data_series = pd.Series(data=solar_data, index=date_time_actual)
solar_capacity_data = pd.read_csv(
	"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Quarterly Solar Capacity Data.csv", delimiter=",")
solar_capacity_raw_data = []
solar_capacity_dates = []
combined_date_month = ""

installed_solar_capacity = pd.Series(index=solar_data_series.index)
for dates in solar_data_series.index:
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

	if combined_date_month in solar_capacity_data.columns:
		installed_solar_capacity[dates] = solar_capacity_data[combined_date_month].values[0]

first_date_data_date = installed_solar_capacity.iloc[0:].first_valid_index()
midnights = first_date_data_date
installed_solar_capacity.iloc[0] = installed_solar_capacity[midnights]
amount_to_add = 0

while midnights in installed_solar_capacity.index:
	time_minus_30 = midnights - datetime.timedelta(minutes=30)
	time_plus_30 = midnights + datetime.timedelta(minutes=30)

	if numpy.isnan(installed_solar_capacity[midnights]) and not numpy.isnan(installed_solar_capacity[time_minus_30]):
		current_index = installed_solar_capacity.index.get_loc(midnights)
		next_data_date = installed_solar_capacity.iloc[current_index:].first_valid_index()

		if next_data_date is not None:
			next_data = installed_solar_capacity[next_data_date]
			range_difference = next_data_date - midnights
			amount_to_add = (next_data - installed_solar_capacity[time_minus_30]) / (range_difference.days + 1)
			installed_solar_capacity[midnights] = amount_to_add + installed_solar_capacity[time_minus_30]

	elif not numpy.isnan(installed_solar_capacity[time_plus_30]):
		installed_solar_capacity[midnights] = installed_solar_capacity[time_plus_30]

	else:
		installed_solar_capacity[midnights] = installed_solar_capacity[
												midnights - datetime.timedelta(days=1)] + amount_to_add

	midnights += datetime.timedelta(days=1)

for dates in installed_solar_capacity.index:
	if numpy.isnan(installed_solar_capacity[dates]):
		installed_solar_capacity[dates] = installed_solar_capacity[dates - datetime.timedelta(minutes=30)]

plt.plot(installed_solar_capacity)
plt.show()

installed_solar_capacity.to_csv(
	"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Interpolated Solar Capacity Data.csv", index=False)
