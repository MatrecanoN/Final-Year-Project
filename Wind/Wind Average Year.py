import pandas as pd
from Wind_PreProcessing import pre_processing as wind_pre_processing
import datetime
from matplotlib import pyplot as plt

# Import data
data = wind_pre_processing()

# Change data from 30 minute granular to daily average
current_date = datetime.date(year=2010, month=1, day=1)
end_date = datetime.date(year=2020, month=12, day=31)
accumulated_data = {}

while current_date <= end_date:
	date_string = "{year}-{month}-{day}".format(year=current_date.year, month=current_date.month, day=current_date.day)
	accumulated_data[current_date] = sum(data[date_string])
	current_date += datetime.timedelta(days=1)

# Finds average utilisation per day
accumulated_data = pd.Series(data=accumulated_data.values(), index=accumulated_data.keys())
accumulated_data = accumulated_data / 48

# Find annual percentage of data and average over all years
leap_years = [2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]
average_series = pd.Series()
average_series_leap = pd.Series()

for dates in accumulated_data.index:
	date_string = dates.strftime("%m-%d")
	new_entry = pd.Series(data=accumulated_data[dates], index=[date_string])

	if dates.year not in leap_years:
		average_series = average_series.append(new_entry)
	else:
		average_series_leap = average_series_leap.append(new_entry)

average_series = average_series * 100
average_series_leap = average_series_leap * 100

min_per_day_non_leap = average_series.groupby(level=0).min()
min_per_day_leap = average_series_leap.groupby(level=0).min()

max_per_day_non_leap = average_series.groupby(level=0).max()
max_per_day_leap = average_series_leap.groupby(level=0).max()

annual_percentage_per_day = average_series.groupby(level=0).mean()
annual_percentage_per_day_leap = average_series_leap.groupby(level=0).mean()

# Uncomment for non-leap years
"""min_series = min(min_per_day_non_leap / annual_percentage_per_day) * annual_percentage_per_day
max_series = max(max_per_day_non_leap / annual_percentage_per_day) * annual_percentage_per_day

ticks = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 364]
legend = ["Average recorded generation", "Region of potential generation"]
plt.xticks(ticks, fontsize=15)
plt.yticks()
plt.xlabel("Date", fontsize=20)
plt.ylabel("Wind Generation Percentage Utilisation per Day (%)", fontsize=18)
plt.title("Average Daily Wind Generation Utilisation with Range of Potential Values", fontsize=20)

plt.fill_between(min_series.index, min_series.values, max_series.values)
plt.plot(annual_percentage_per_day, color="black")
plt.grid()
plt.legend(legend, fontsize=12)

plt.show()"""

# Uncomment for leap years
min_series = min(min_per_day_leap / annual_percentage_per_day_leap) * annual_percentage_per_day_leap
max_series = max(max_per_day_leap / annual_percentage_per_day_leap) * annual_percentage_per_day_leap

ticks = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 365]
legend = ["Average recorded generation", "Region of potential generation"]
plt.xticks(ticks, fontsize=15)
plt.yticks()
plt.xlabel("Date", fontsize=20)
plt.ylabel("Wind Generation Percentage Utilisation per Day (%)", fontsize=18)
plt.title("Min/Max and Average Daily Wind Generation as a Percentage of Annual Total - Leap Year", fontsize=20)

plt.fill_between(min_series.index, min_series.values, max_series.values)
plt.plot(annual_percentage_per_day_leap, color="black")
plt.grid()
plt.legend(legend, fontsize=12)

plt.show()
