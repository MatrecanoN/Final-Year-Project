from matplotlib import pyplot as plt
from Wind_PreProcessing import pre_processing as wind_pre_processing

wind_data_filtered = wind_pre_processing()
wind_data_filtered = wind_data_filtered * 100

wind_data_daily_rolling_average = wind_data_filtered.rolling(48, min_periods=1).mean()
wind_data_weekly_rolling_average = wind_data_filtered.rolling(4383, min_periods=1).mean()
wind_data_yearly_rolling_average = wind_data_filtered.rolling(17532, min_periods=1).mean()

"""plt.plot(wind_data_filtered, color="blue")"""
plt.plot(wind_data_daily_rolling_average, color="blue")
plt.plot(wind_data_weekly_rolling_average, color="yellow")
plt.plot(wind_data_yearly_rolling_average, color="orange")

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel("Date", fontsize=20)
plt.ylabel("% of Installed Capacity Utilisation", fontsize=20)
plt.grid()
plt.legend(["24 Hour Rolling Average", "7 Day Rolling Average", "365 Day Rolling Average"], fontsize=15)
plt.title("Wind Generation Utilisation by Date and Differing Rolling Average", fontsize=20)

plt.show()
