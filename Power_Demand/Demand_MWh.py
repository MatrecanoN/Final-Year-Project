from matplotlib import pyplot as plt
from Demand_PreProcessing import pre_processing as demand_pre_processing
import pandas as pd
import datetime

# Imports data and puts in MWh
data = demand_pre_processing() * 0.5

# Combines into MWh / Day
previous_date_time = "blank"
data_sum = 0
accumulated_data = pd.Series()
current_year_total = 0
annual_total = {}

for dates in data.index:
	if previous_date_time == "blank":
		previous_date_time = dates

	if dates.year == previous_date_time.year:
		current_year_total += data[dates]
		if dates.year == 2021 and dates.month == 9 and dates.day == 8:
			annual_total[previous_date_time.year] = current_year_total
	else:
		annual_total[previous_date_time.year] = current_year_total
		current_year_total = data[dates]

	if dates.day == previous_date_time.day:
		data_sum += data[dates]
		previous_date_time = dates
		if dates.year == 2021 and dates.month == 9 and dates.day == 8 and dates.hour == 22 and dates.minute == 30:
			previous_date = datetime.date(year=previous_date_time.year, month=previous_date_time.month, day=previous_date_time.day)
			new_accumulated_data = pd.Series(data=data_sum, index=[previous_date])
			accumulated_data = accumulated_data.append(new_accumulated_data)
	else:
		previous_date = datetime.date(year=previous_date_time.year, month=previous_date_time.month, day=previous_date_time.day)
		new_accumulated_data = pd.Series(data=data_sum, index=[previous_date])
		accumulated_data = accumulated_data.append(new_accumulated_data)
		data_sum = data[dates]
		previous_date_time = dates

accumulated_data = accumulated_data.drop(accumulated_data.index[0]) * 0.001

power_usage_yearly_rolling_average = accumulated_data.rolling(365, min_periods=1).mean()

plt.plot(accumulated_data)
plt.plot(power_usage_yearly_rolling_average)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.grid()
plt.xlabel("Date", fontsize=20)
plt.ylabel("Grid Power Demand (GWh / Day)", fontsize=20)
plt.title("GB Grid Demand by Date", fontsize=20)
plt.legend(["Daily Power Demand", "365-Day Rolling Average"], fontsize=15)

plt.show()
