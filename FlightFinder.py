# Project Description:
# --------------------
# This program will upload a data file that contains information for flights from Providence,
# Rhode Island to Orlando, Florida. It will break the data up into: Airline, Flight Number,
# Departure Time, Arrival Time, and Price. It will then allow the user to seach through the data in
# certain ways. These ways will include: 1) Find all the flights on a particular airline
# 2)Find the cheapest flight, 3)Find all flights less than a specified price, 4) Find the
# shortest flight, 5) Find all flights that depart within a specified range, 6) Find the
# average price for a specified airline, and 7) Quit the program.
#
# For each option a function will be written to compute the answer. For example, if the user
# selects number 2) find the cheapest flight, a function will loop through the price values and
# find the lowest and return it



# ----------------

# Function to read the Airline, Flight Number, Departure Time, Arrival Time, and Price.
def getLists():
    fname = input("Enter name of data file: ")
    infile = open(fname,'r')
    #reads each line
    line = infile.readline()
 
    Airlines = []
    FlightNumbers = []
    DepartureTimes = []
    ArrivalTimes = []
    Prices = []
 
    while line != "":
        line = line.strip()
        #splits all the information at the comma
        Airline, FlightNumber, DepartureTime, ArrivalTime, Price = line.split(',')
        #The next 5 lines add to the above lists
        Airlines = Airlines + [Airline]
        FlightNumbers = FlightNumbers + [FlightNumber]
        DepartureTimes = DepartureTimes + [DepartureTime]
        ArrivalTimes = ArrivalTimes + [ArrivalTime]
        Prices = Prices + [Price]
        line = infile.readline()
 
    infile.close()
    return Airlines, FlightNumbers, DepartureTimes, ArrivalTimes, Prices
 
#Function if User selects 1 from the main function. It allows the user to search for all flights on a particular airline
def particularAirline(Airlines):

        airlinesIndex = []
        #While the above index is empty it will ask for an airline to search for, if the user dosn't enter an appropriate airline then it will ask again
        while airlinesIndex == []:
            airlineChoice = input("Please enter the name of an airline: ")
            #The following 3 lines checks if the user input matches any of the airlines. If it does match, it records the Index number in the airlinesIndex list.
            for i in range(len(Airlines)):
                if airlineChoice == Airlines[i]:
                    airlinesIndex.append(i)
        #Return the index numbers where the userinput matches an Airline
        return airlinesIndex
    
#Function that searches through all the airline prices and finds the index for the cheapest then returns that index number    
def cheapestFlight(Prices):
    cheapest=[]
    cheapestIndex = []
    for i in range(len(Prices)):
        #make a list of the prices without the $ symbol 
        cheapest.append(Prices[i].strip('$'))
        #finds the index position of the cheapest price then adds it to cheapest Index
        if min(cheapest) == cheapest[i]:
            cheapestIndex.append(i)
    #Returns the index position of the cheapest flight
    return cheapestIndex

#Function that finds all flights less than a specified price   
def cheaperThan(Prices):
    price =[]
    priceIndex = []
    specPrice = input("Specify a price without the $ symbol:  ")
    for i in range(len(Prices)):
        #makes a list of the prices without the $ symbol
        price.append(Prices[i].strip('$'))
        #compares the userinput with the prices, adds index position where the specified price is less than the airline price 
        if specPrice > price[i]:
            priceIndex.append(i)
    #Returns the index position 
    return priceIndex

#Function that finds the shortest flight
def shortestFlight(DepartureTimes, ArrivalTimes):
    depart = []
    arrive = []
    totalTimes = []
    shortestTimeIndex = []
    #Puts the depart and arrive times into 2 sperate lists with out the : symbol so math can be performed on them.
    for i in range(len(DepartureTimes)):
        depart.append(DepartureTimes[i].replace(":",""))
        arrive.append(ArrivalTimes[i].replace(":",""))
    #Subtracts the depatrue times from the arrival times then puts the result into the totalTimes list    
    for i in range(len(DepartureTimes)):
        totalTimes.append(int(arrive[i]) - int(depart[i]))
    #Finds the index position of the minimum time 
    for i in range(len(totalTimes)):
        if min(totalTimes) == totalTimes[i]:
            shortestTimeIndex.append(i)
    #Returns the index position of the shortest time        
    return shortestTimeIndex

#Function that lets the user select all flights within a specified departure time.    
def departingAt(DepartureTimes):
    
    earliest = input("Enter the earliest allowable departure time:  ")
    latest = input("Enter the latest allowable departure time:  ")
    departIndex =[]
    
    for i in range(len(DepartureTimes)):
        #If the earliest departure time entered by the user is greater than or equal to all the departure times
        #and the latest entered depature time is less than all the departure times then add its index position to the departIndex list
        if earliest <= DepartureTimes[i] and DepartureTimes[i] < latest:
            departIndex.append(i)
        
    #Return the index list of all values that meet the criteria
    return departIndex

#Function that finds the average price for a particular airline
def averagePrice(Airlines, Prices):
    addPrice = 0
    allPrices = []
    #Finds the index positions of a particular, specified airline
    airlineIndex = particularAirline(Airlines)
    #Puts all the prices without the $ symbol into a list
    for i in range(len(Prices)):
        allPrices.append(Prices[i].strip('$'))
    #Adds up all of a specified airlines prices and puts the total into addPrice    
    for i in airlineIndex:
        addPrice = addPrice + int(allPrices[i])
    #Gets the average by taking the total and dividing it by the length    
    addPrice = addPrice/len(airlineIndex)
    #Returns the average    
    return addPrice

def main():
    # The main function implements the pseudocode by using the functions defined above.
    # The getLists function stores the different values into the below categories
    Airlines, FlightNumbers, DepartureTimes, ArrivalTimes, Prices = getLists()
    #Print out the main menu
    print ("Please choose one of the following options:")
    print ("1 --Find all flights on a particular airline")
    print ("2 --Find the cheapest flight")
    print ("3 --Find all flights less than a specified price")
    print ("4 --Find the shortest flight")
    print ("5 --Find all flights that depart within a specified range")
    print ("6 --Find the average price for a specidied airline")
    print ("7 --Quit")
    #Allows user to pick an option from above
    choice = input("Pick a number from above  ")
    #The following provide different options depending on what the user entered for a number
    if choice == "1":
        #Stores the index positions for what airline was selected by using the particularAirline function
        airlinesIndex = particularAirline(Airlines)
        print ("The flights that meet your criteria are:")
        print(" ")
        print("AIRLINE   FLT#     DEPT      ARR       PRICE")
        print ("-----------------------------------------------------")
        #Prints the information from each list at the index positions provided in airlinesIndex
        for i in airlinesIndex:
            print (Airlines[i],"   ", FlightNumbers[i],"   ", DepartureTimes[i],"   ", ArrivalTimes[i],"   ", Prices[i])
        #Restarts the main function at the end
        main()
        
    elif choice == "2":
        cheapestIndex = cheapestFlight(Prices)
        for i in cheapestIndex:
            print ("The cheapest flight is:  ", Airlines[i], FlightNumbers[i], DepartureTimes[i], ArrivalTimes[i], Prices[i])
        main()
        
    elif choice == "3":
        priceIndex = cheaperThan(Prices)
        print ("The flights that meet your criteria are:")
        print(" ")
        print("AIRLINE   FLT#     DEPT      ARR       PRICE")
        print ("-----------------------------------------------------")
        #If the search provided no results then the priceIndex will be empty
        if priceIndex == []:
            print("No flights meet your criteria")
            print(" ")
        else:
            for i in priceIndex:
                print ( Airlines[i],"   ", FlightNumbers[i],"   ", DepartureTimes[i],"   ", ArrivalTimes[i],"   ", Prices[i])
        main()
        
    elif choice == "4":
        shortestTimeIndex = shortestFlight(DepartureTimes, ArrivalTimes)
        print ("The shortest flight is:")
        print(" ")
        print("AIRLINE   FLT#     DEPT      ARR       PRICE")
        print ("-----------------------------------------------------")
        for i in shortestTimeIndex:
            print ( Airlines[i],"   ", FlightNumbers[i],"   ", DepartureTimes[i],"   ", ArrivalTimes[i],"   ", Prices[i])
            print(" ")
        main()
         
    elif choice == "5":
        departIndex = departingAt(DepartureTimes)
        print ("The flights that meet your criteria are:")
        print(" ")
        print("AIRLINE   FLT#     DEPT      ARR       PRICE")
        print ("-----------------------------------------------------")
        for i in departIndex:
            print ( Airlines[i],"   ", FlightNumbers[i],"   ", DepartureTimes[i],"   ", ArrivalTimes[i],"   ", Prices[i])
        main()
        
    elif choice == "6":
        avPrice = averagePrice(Airlines, Prices)
        print ("The averge flight cost for your selected airline is:  $", avPrice)
        main()
     #Closes the program   
    elif choice == "7":
        exit()
     #If the user enters anything other than the 7 numbers they will get the following message and the program will start over   
    while choice != "1" or "2" or "3" or "4" or "5" or "6" or "7":
        print ("invalid choice")
        main()
        
