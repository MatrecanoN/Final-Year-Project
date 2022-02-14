from matplotlib import pyplot as plt
from Wind_PreProcessing import pre_processing as wind_pre_processing
from Helpers.Yearly_Splicer import yearly_splicer

wind_data = wind_pre_processing()
wind_data_weekly_rolling_average = wind_data.rolling(4383, min_periods=1).mean()
annual_data = yearly_splicer(wind_data_weekly_rolling_average)

years_graphed = []
for years in annual_data:
	plt.plot(annual_data[years])
	years_graphed.append(years)

plt.xticks(["01-01--00-00", "02-01--00-00", "03-01--00-00", "04-01--00-00", "05-01--00-00", "06-01--00-00", "07-01--00-00", "08-01--00-00", "09-01--00-00", "10-01--00-00", "11-01--00-00", "12-01--00-00", "12-31--23-30"], ["Jan 1", "Feb 1", "Mar 1", "Apr 1", "May 1", "Jun 1", "Jul 1", "Aug 1", "Sep 1", "Oct 1", "Nov 1", "Dec 1", "Dec 31"], fontsize=15)
plt.legend(years_graphed, fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel("Date", fontsize=20)
plt.ylabel("Wind Generation Utilisation (%)", fontsize=20)
plt.title("Wind Generation Utilisation by Date in Non-Leap Years", fontsize=20)
plt.grid()
plt.show()
