principle = 0
rate = 0
time = 0

# prompt the user to type in a principle that is above 0

#while principle <= 0:
while True:
    principle = float(input("Enter the principle amount: "))
    #if principle <= 0:
    if principle < 0:
        #print("Principle can't be less than or equal to zero.")
        print("Principle can't be less than zero.")
    else:
        break

# while rate <= 0:
while True:
    rate = float(input("Enter the interest rate: "))
    #if rate <= 0:
    if rate < 0:
        #print("Interest rate can't be less than or equal to zero.")
         print("Interest rate can't be less than zero.")
    else:
        break

#while time <= 0:
while True:
    time = int(input("Enter the time in years: "))
    #if time <= 0:
    if time < 0:
        #print("Time can't be less than or equal to zero.")
         print("Time can't be less than zero.")
    else:
        break



#print(principle)
#print(rate)
#print(time)

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} year/s: ${total:.2f}")