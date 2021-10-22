import pandas as pd


def yearly_splicer(energy_data):
	first_year = energy_data.index[0].year
	last_year = energy_data.index[-1].year

	year_list = range(first_year, last_year + 1, 1)

	yearly_data = {}
	year_length = {}
	for years in year_list:
		yearly_data[years] = pd.Series(data=energy_data[str(years)].values, index=range(len(energy_data[str(years)].index)))
		year_length[years] = len(yearly_data[years])

	return yearly_data
