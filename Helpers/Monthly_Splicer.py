import pandas as pd
from dateutil.relativedelta import relativedelta


def monthly_splicer(energy_data, year):
	isolated_year_data = pd.Series(data=energy_data[str(year)].values, index=energy_data[str(year)].index)

	first_month = isolated_year_data.keys()[0].month
	last_month = isolated_year_data.keys()[-1].month
	month_list = range(first_month, last_month + 1, 1)

	monthly_data = {}
	monthly_data_data = {}
	monthly_data_index = {}

	for months in month_list:
		monthly_data_data[months] = []
		monthly_data_index[months] = []

	for index in isolated_year_data.index:
		month = index.month
		monthly_data_data[month].append(isolated_year_data[index])
		monthly_data_index[month].append(index - relativedelta(months=(index.month - 1)))

	for keys in monthly_data_data.keys():
		monthly_data[keys] = pd.Series(data=monthly_data_data[keys], index=monthly_data_index[keys])

	return monthly_data
