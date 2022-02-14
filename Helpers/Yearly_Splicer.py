import pandas as pd
import datetime

def yearly_splicer(energy_data):
	first_year = energy_data.index[0].year
	last_year = energy_data.index[-1].year

	year_list = range(first_year, last_year + 1, 1)

	yearly_data = pd.DataFrame()

	dates_stripped = []
	dates_stripped_leap = []
	leap_years = [2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]

	for dates in energy_data.index:
		if dates.year == 2010:
			dates_stripped.append(dates.strftime("%m-%d--%H-%M"))


	for years in year_list:
		if years not in leap_years and years != 2021:
			yearly_data[years] = pd.Series(data=energy_data[str(years)].values, index=dates_stripped)

	return yearly_data
