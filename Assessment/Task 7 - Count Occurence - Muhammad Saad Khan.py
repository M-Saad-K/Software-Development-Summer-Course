"""
@ Author: Muhammad Saad Khan
@ Title: Task 7 - Count Occurence - Muhammad Saad Khan
@ Version: Python 3.12.4 v2025.8.0 - Microsoft
@ Date: 2025 - 07- 08

This is an altered version of the Task 6 Program

Description:

TThe program reads 15 student's name, coursework mark and prelim mark from separate files and then calculates and displays their percentage and grade
It will also count the number of A passes achieved and display who has the highest percentage in the class
"""
# I will declare this A_Counter var as global outside of any func - to find how many A's have been passed
A_Counter = 0

# This list is important, as it will contain all the percentages, and will be used to find the max
Per_List = []

# Function for STEP 2 - Calculate and store the percentage of the candidate in a variable called "per"
def Calc():

    # That has been intialised here as global, so that the global value is alter inside this func
    global Per_List
    
    # Declaring per as an global value, and intialing it to a zero float
    global per
    per = 0.0

    # Calculating the percentage using the coMark and preMark and storing it in per
    per = (((coMark + preMark)*100)/150)  

    # Rounding the percentage to two decimal places and storing it in per
    per = round(per, 2)

    # Add the current percentage to the list
    Per_List.append(per)

# END OF FUNCTION

# Function for Step 3 - Determine the grade of the candidate using the "per" variable, and store the result in "grade" variable
def Grader():

    # This will be our index to find out how many A passes have been achieved - it has been declared global to alter its value
    global A_Counter

    # Declaring grade to a global variable, and intialising it to an empty string
    global grade
    grade = " "

    # Determining if awarded an A
    """ There will be a Count Occurence Standard Algorithm Inclemented used to find out how many A passes have been achieved in the class"""
    if per >= 70:

        # IF "per" is greater than or equal to 70%
        grade = "A"

        # How this will work is that when a A pass is detected -> the A_Counter will increment by 1
        # Through this, after each person's percentage is iterated, all the A passes would've incremented the A_Counter by 1
        # After the loop is completed, A_Counter will contain the number of times the A grade has been passes through
        # Therefore telling the number of A grades achieved.
        # This is the count occurence standard algorithm.

        # Iterate the A_Counter by 1 each time a A grade is called
        A_Counter = A_Counter + 1 
    
    # Determining if awarded a B
    elif per >= 60:

        # ELSE IF "per" is greater than or equal to 60%
        grade = "B"
    
    # Determining if awarded a C
    elif per >= 50:

        # ELSE IF "per" is greater than or equal to 50%
        grade = "C"
    
    # Determining if awarded a D
    elif per >= 45:
        
        # ELSE IF "per" is greater than or equal to 45%
        grade = "D"
    
    # ELSE "grade" = "No Grade Awarded"
    else: grade = "No Grade Awarded"

# END OF FUNCTION 

# This is a function for finding out the who has achieved the highest grade
def Max():

    """We will use a Finding Max Standard Alogrithm"""
    # How the Find Max Alogrithm works is by first intialising a var, that will hold the max value, to the first value of the list you want to find the max value of
    # Next you'll iterate through each element in that list, and check if the current element is larger than the one contained in the var
    # If so, then the var will be altered to that greater current element.
    # This will repeat until only the largest value is stored inside of the var. 
    # This is the Find Max Algorithm

    # We have intialised the max var to the first value in the list
    max = Per_List[0]

    # Iterate through the length of the list
    for x in range(len(Per_List)):

        # IF the current value of the list is greater than the current max
        if (Per_List[x] > max):

            # Store that greater percentage value in Max
            max = Per_List[x]

            # Store the person you have the greater percentage value in Max_Name
            Max_Name = NameArray[x]

    # After the loop -> print the person who has the greatest score and their score
    print(f"The person who has achieved the highest percentage is {Max_Name} with {max}% overall")

# END OF FUNCTION 



""" MAIN STARTING CODE """

# Intialise variables for name, coMark and preMark
name = str(" ")
coMark = 0
preMark = 0

# Intialise the lists that will hold each line of the files
NameArray = []
coMarkArray = []
preMarkArray = []


# WHILE "name is equal to an empty string, and coMark and preMark are both equal to 0"
while True:

    """ FIRST I need to open the files for reading """

    # NamesArray will hold the reading of each file in names.txt
    NameReader = open("names.txt", "r")

    # coMarkArray will hold the reading of each file in mark1.txt
    coMarkReader = open("mark1.txt", "r")

    # preMark will hold the reading of the each file in mark2.txt
    preMarkReader = open("mark2.txt","r")

    # This will add append each line of the readers to their repective arrays
    for line in NameReader:

        # Strip the line of white space
        stripped = line.strip()

        # Append the current line to the respected array
        NameArray.append(stripped)

    for line in coMarkReader:

        # Strip the line of white space
        stripped = line.strip()

        # Append the current line to the respected array
        coMarkArray.append(stripped)

    for line in preMarkReader:

        # Strip the line of white space
        stripped = line.strip()

        # Append the current line to the respected array
        preMarkArray.append(stripped)

    

    """ IMPORTANT CHANGE: I will add for loop which will iterate through each line of the names.txt and intialise the current index value of names.txt, mark1.txt and mark2.txt to name, coMark and preMark respectiviely """
    
    # This for loop will iterate through each line in the names.txt
    # x will hold the index position
   
    for x in range(len(NameArray)):

        # Next we will need to append each value of the lines in the arrays
        

        # This will add the current index name to the "name" var
        name = NameArray[x]
        
        # This will add the current index mark to the "coMark" var -> the inputs would be taken as a string and then cast as a float inside respective variables
        coMark = float(coMarkArray[x])

        # This will add the current index mark to the "preMark" var -> the inputs would be taken as a string and then cast as a float inside respective variables
        preMark = float(preMarkArray[x])

        ### NOW EVERY FUNCTION AFTER THIS POINT, NEEDS TO BE INSIDE THE FOR LOOP ###

        # Take the userinput of the candidates's coursework mark out of 60 as an int 
        #coMark = int(input("Please Enter Candidate's Courswork Mark out of 60: "))

        # IF userinput is less than or equal to 60.
        if coMark <= 60:
        
            # THEN pass
            pass

        else:

            # ELSE print that this is an invalid mark
            print("This is an invalid mark")

            # CONTINUE to jump back to the start of the loop
            continue

    
        # Take the userinput of the candidates's prelim mark out of 90 as an int
        #preMark = int(input("Please Enter Your Prelim Mark out of 90: "))

        # IF userinput is less than or equal to 90
        if preMark <= 90:

            # THEN pass
            pass

            
            

        # ELSE print that this is an invalid mark
        else:

            print("This is an invalid mark")

            # Continue to jump back to the start of the loop
            continue 

        # END OF WHILE LOOP and Step 1
        # BEGIN ACTIVATING NEXT STEPS

        # Step 2 - Calculate and store the percentage of the candidate in a variable called "per".
        Calc()


        # Step 3 - Determine the grade of the candidate using the "per" variable, and store the result in "grade" variable.
        Grader()

        # Step 4 - Display both the candidate's name with the percentage and grade awarded to them.
        print(f"{name} has achieved {per}% overall, being awarded a grade of {grade} \n")
        # "Laika has achieved 75% overall, being awarded a grade of A"

        """ Always remeber to close a file """
        NameReader.close()
        coMarkReader.close()
        preMarkReader.close()

    
    # IF this statement is reached, the for loop has ended
    # BREAK the loop, Ending the while loop
    break

# This will print the number of A grades achieved
print("The number of A grades accomplished by the class is", A_Counter)


Max()


# Time to finish
exit() 
   