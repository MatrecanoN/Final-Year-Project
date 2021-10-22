from matplotlib import pyplot as plt
from Wind_PreProcessing import pre_processing as wind_pre_processing

wind_data_filtered = wind_pre_processing()

wind_data_daily_rolling_average = wind_data_filtered.rolling(48, min_periods=1).mean()
wind_data_weekly_rolling_average = wind_data_filtered.rolling(4383, min_periods=1).mean()
wind_data_yearly_rolling_average = wind_data_filtered.rolling(17532, min_periods=1).mean()

plt.plot(wind_data_filtered, color="blue")
plt.plot(wind_data_daily_rolling_average, color="black")
plt.plot(wind_data_weekly_rolling_average, color="red")
plt.plot(wind_data_yearly_rolling_average, color="yellow")

plt.xlabel("Date and Time of Generation")
plt.ylabel("% of Installed Capacity Utilisation")
plt.grid()

plt.show()
