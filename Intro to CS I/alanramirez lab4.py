# these statements below could be simplified to just 3 lines, but I decided to implement those conditionals you mentioned on zoom
temp = round(float(input("Please enter the current temperature in Fahrenheit: ")), 2)
if temp.is_integer() == True:
    temp = int(temp)
while True:
    hum = round(float(input("Please enter the current humidity percentage: ")), 2)
    if 0 <= hum <= 100:
        if hum.is_integer() == True:
            hum = int(hum)
        break
    else:
        print("Error, the humidity level entered is invalid.", end=(" "))
while True:
    wind = round(float(input("Please enter the current wind speed in mph: ")), 2)
    if wind >= 0:
        if wind.is_integer() == True:
            wind = int(wind)
        break
    else:
        print("Error, the wind speed entered is invalid.", end=(" "))
        
# td = temperature description
if temp < 32:
    td = "very cold"
elif 32 <= temp < 50:
    td = "cold"
elif 50 <= temp < 65:
    td = "cool"
elif 65 <= temp < 80:
    td = "moderate"
elif 80 <= temp < 95:
    td = "hot"
elif 95 <= temp:
    td = "very hot"
    
# hd = humidity description
if 0 <= hum < 45:
    hd = "comfortable"
elif 45 <= hum <= 65:
    hd = "muggy"
elif 65 < hum <= 100:
    hd = "oppressive"
    
# wd = wind speed description
if 0 <= wind < 1:
    wd = "calm"
elif 1 <= wind < 8:
    wd = "light-breeze"
elif 8 <= wind < 19:
    wd = "moderate-breeze"
elif 19 <= wind < 32:
    wd = "strong-breeze"
elif 32 <= wind < 47:
    wd = "moderate-gale"
elif 47 <= wind < 64:
    wd = "strong-gale"
elif 64 <= wind < 74:
    wd = "storm"
elif 75 <= wind:
    wd = "hurricane"

# final print statement
print("The temperature of {}°F today is {}, and the humidity is {} as it is {}%. There is also wind moving at {} mph, blowing with a {}-level force.".format(temp, td, hd, hum, wind, wd))