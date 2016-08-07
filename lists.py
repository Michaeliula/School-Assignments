
#List of First and Last names and ages
firstNames = ['Mike', 'Bill', 'Rose', 'Shawna', 'Graham', 'John', 'Bobby']

lastNames = ['Iula', 'Smith', 'Rambula', 'Rambo', 'Chapman', 'Cleese', 'Orr']

ages = ['30', '5', '16', '21years', '22.6', '19', '-18']

#Allows user to enter a new first and last name and age
newfirstName = raw_input("Enter a first name:  ")
newlastName = raw_input("Enter a last name:  ")
newAge = raw_input("Enter an age:  ")

#appends the new information to the original lists
firstNames.append(newfirstName)
lastNames.append(newlastName)
ages.append(newAge)

#I used the below function from the functions assignment
def clean_age_data(Age):
    original = Age
    valid = True


    #If 'original' is less than 2 or the third character in original is a number, then 'valid' is set to false. "age" is also set to the string "False" so that the next step(age.isdigit) dosen't get an error.
    if len(original) < 2:
        valid = False
        age = "False"
    elif original[2:3].isdigit() == True:
        valid = False
        age = "False"
    #Otherwise, 'age' is set to the first 2 characters of 'original'
    else:
        age = original[0:2]


    #If 'age' is not a digit then 'valid' is set to false and program ends
    if age.isdigit() == False:
        vaild = False

    #If valid equals False then print invalid, otherwise print the corrected age.
    if valid == False:
        return 4
    else:
        return  age

# I set an index to -1 so I could iterate through the lists
index = -1
#This for loop goes through each index in the lists(As they are all the same length I used firstNames).
for name in firstNames:
    #add 1 to the index counter.
    index = index + 1
    #If the function returns 4 that means the age was invalid and should continue to the else condition.
    if clean_age_data(ages[index]) == 4:
        continue
    #Prints the first and last name index and the age once it has been run through the clean_age_data function
    else:
        print firstNames[index] +",", lastNames[index] + "," + clean_age_data(ages[index])
