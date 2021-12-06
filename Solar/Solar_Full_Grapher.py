from matplotlib import pyplot as plt
from Solar_PreProcessing import pre_processing as solar_pre_processing

solar_data_filtered = solar_pre_processing()

solar_data_daily_rolling_average = solar_data_filtered.rolling(48, min_periods=1).mean()
solar_data_weekly_rolling_average = solar_data_filtered.rolling(4383, min_periods=1).mean()
solar_data_yearly_rolling_average = solar_data_filtered.rolling(17532, min_periods=1).mean()

plt.plot(solar_data_filtered, color="blue")
plt.plot(solar_data_daily_rolling_average, color="black")
plt.plot(solar_data_weekly_rolling_average, color="red")
plt.plot(solar_data_yearly_rolling_average, color="orange")

plt.xlabel("Date and Time of Generation")
plt.ylabel("% of Installed Capacity Utilisation")
plt.grid()
plt.legend(["Raw Data", "24 Hour Rolling Average", "7 Day Rolling Average", "365 Day Rolling Average"])
plt.title("Total Solar Generation Utilisation by Data Entry (30 Minute Granular)")

plt.show()
