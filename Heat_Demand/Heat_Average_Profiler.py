import pandas as pd
from Heat_Preprocessing import pre_processing as heat_pre_processing
from matplotlib import pyplot as plt

# Import data
data = heat_pre_processing()
previous_date_time = "blank"
current_year_total = 0
annual_total = {}

for dates in data.index:

	if previous_date_time == "blank":
		previous_date_time = dates

	if dates.year == previous_date_time.year:
		current_year_total += data[dates]
		if dates.year == 2019 and dates.month == 12 and dates.day == 31:
			annual_total[previous_date_time.year] = current_year_total
	else:
		annual_total[previous_date_time.year] = current_year_total
		current_year_total = data[dates]

	previous_date_time = dates

# Find annual percentage of data and average over all years
annual_percentage_per_day = pd.Series()
annual_percentage_per_day_leap = pd.Series()
# Next commentated out section is used to validate that day data = 100% of annual data
"""tester = pd.Series()
for dates in data.index:
	new_input = pd.Series(data=[data[dates]], index=[dates.year])
	tester = tester.append(new_input)

year_list = annual_total.keys()
storage = {}
tester = tester.groupby(level=0).sum()

for years in year_list:
	storage[years] = tester[years] / annual_total[years]
aaa = pd.Series(data=storage.values(), index=storage.keys())"""
leap_years = [2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]

for dates in data.index:
	current_percentage = data[dates] / annual_total[dates.year]
	new_percentage_data = pd.Series(data=current_percentage * 100, index=[dates.strftime("%m-%d")])
	if dates.year not in leap_years:
		annual_percentage_per_day = annual_percentage_per_day.append(new_percentage_data)
	else:
		annual_percentage_per_day_leap = annual_percentage_per_day_leap.append(new_percentage_data)

annual_percentage_per_day = annual_percentage_per_day.groupby(level=0).mean()
annual_percentage_per_day_leap = annual_percentage_per_day_leap.groupby(level=0).mean()

annual_percentage_per_day.to_csv(
	"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Average Year Heat Data Non-Leap.csv")

annual_percentage_per_day_leap.to_csv(
	"C:/Users/matre/PycharmProjects/Final Year Project/Data Sources/Average Year Heat Data Leap.csv")
