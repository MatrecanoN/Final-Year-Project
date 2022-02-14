import pandas as pd
from matplotlib import pyplot as plt
from Wind_PreProcessing import pre_processing as wind_pre_processing
import datetime

wind_data_filtered = wind_pre_processing()
wind_data_filtered = wind_data_filtered * 100

years = range(2010, 2022, 1)
wind_data_weekly_rolling_average = wind_data_filtered.rolling(4383, min_periods=1).mean()
wind_data_annual_frame = pd.DataFrame(columns=years)

for dates in wind_data_weekly_rolling_average.index:
	date_text = dates.strftime("%m-%d--%H-%M")
	wind_data_annual_frame[dates.year] = wind_data_annual_frame[dates.year].append(
		pd.Series(data=wind_data_weekly_rolling_average[dates], index=[date_text]))
	print(dates)

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel("Date", fontsize=20)
plt.ylabel("% of Installed Capacity Utilisation", fontsize=20)
plt.grid()
plt.legend(["24 Hour Rolling Average", "7 Day Rolling Average", "365 Day Rolling Average"], fontsize=15)
plt.title("Wind Generation Utilisation by Date and Differing Rolling Average", fontsize=20)

plt.show()
