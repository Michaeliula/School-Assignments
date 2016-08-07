
/*
Instructions for the Assignment
Declare these list variables, each with seven values in the list:
firstNames : a list with seven string variables of first names. Make the first firstname be your own first name.
lastNames -  a list with seven string variables of last names. Make the first lastname be your own lastname.
ages - a list of strings (not integers!)  which will have in it: X,5, 16, 21years, 17.6, 19, -18, 917. Where instead of X put your actual age.

These lists must be in the same order. That is, the first name at index 0 should correspond to the last name at index 0 and the age at index 0; and so on. Each list is a list of strings so don’t forget the single quotes around each data value.

Read input from the user to accept another first name, last name, and age.  Add this data to the data lists of the program (make a total of 8 names with their age).

Write a for loop to go through the 8 names and print a CSV line with first name followed by last name followed by age,  for all names that have valid ages. If an age is not valid and can’t be fixed (e.g. a negative number can not be fixed, but “21years” should be fixed by removing the “years” and then using the 21), then do not print the data record.  Use your code from the Conditionals assignment to check for valid ages.
*/

For instance, the data:
First names: Tim, Bill, Sue, Eric, Latisha, Juan, Jen
Last names:  Hill, Smith, Jones, Wolfe, Williams, Gomez, Johnson
Ages: 5, 16, 21years, 17.6, 19, -18, 917
And the input from the user:
                        Casey
                        Fay
                        12
 Would yield output:
       Bill,Smith,16
       Sue,Jones,21
       Eric, Wolfe, 17
       Latisha, Williams,19
       Casey, Fay, 12

#My Solution:
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
