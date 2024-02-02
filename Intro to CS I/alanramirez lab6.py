import matplotlib.pyplot as plt

# Source: avg temp over past 30 yrs -https://www.currentresults.com/Weather/Nebraska/Places/omaha-temperatures-by-month-average.php
# Source: avg temp over year 2021 - https://www.weather.gov/oax/monthly_climate_records

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
avg_htemp30yr = [34, 39, 52, 64, 75, 84, 88, 86, 79, 66, 50, 38]
avg_ltemp30yr = [15, 19, 30, 41, 53, 63, 68, 66, 56, 43, 30, 20]
avg_htemp2021 = [36, 24, 64, 66, 70, 90, 88, 89, 83, 69, 56, 47]
avg_ltemp2021 = [21, 5, 33, 41, 50, 66, 68, 68, 59, 47, 33, 25]

plt.plot(months, avg_htemp30yr, color="red", label="Average High Temperature Since 1990")
plt.plot(months, avg_ltemp30yr, color="blue", label="Average Low Temperature Since 1990")
plt.plot(months, avg_htemp2021, color="orange", linestyle="--", label="Average High Temperature During 2021")
plt.plot(months, avg_ltemp2021, color="purple", linestyle="--", label="Average Low Temperature During 2021")

plt.title("Average Temperatures in Omaha in Fahrenheit")
plt.xlabel("Months")
plt.ylabel("Temperatures")
plt.legend()
plt.style.use('seaborn-whitegrid')
plt.grid(True)
plt.show()