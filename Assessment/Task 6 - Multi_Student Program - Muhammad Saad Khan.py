"""
@ Author: Muhammad Saad Khan
@ Title: Task 6 - Multi_Student Program - Muhammad Saad Khan
@ Version: Python 3.12.4 v2025.8.0 - Microsoft
@ Date: 2025 - 07- 08

This is an altered version of Task 5 to read a file with 15 students instead of just one

Description:

The program reads 15 student's name, coursework mark and prelim mark from separate files and then calculates and displays their percentage and grade
"""

# Function for STEP 2 - Calculate and store the percentage of the candidate in a variable called "per"
def Calc():
    
    # Declaring per as an global value, and intialing it to a zero float
    global per
    per = 0.0

    # Calculating the percentage using the coMark and preMark and storing it in per
    per = (((coMark + preMark)*100)/150)  

    # Rounding the percentage to two decimal places and storing it in per
    per = round(per, 2)

# END OF FUNCTION

# Function for Step 3 - Determine the grade of the candidate using the "per" variable, and store the result in "grade" variable
def Grader():

    # Declaring grade to a global variable, and intialising it to an empty string
    global grade
    grade = " "

    # Determining if awarded an A
    if per >= 70:

        # IF "per" is greater than or equal to 70%
        grade = "A"
    
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



""" MAIN STARTING CODE """

# Intialise variables for name, coMark and preMark
name = str(" ")
coMark = 0
preMark = 0

# Intialise the lists that will hold each line of the files
NameArray = []
coMarkArray = []
preMarkArray = []


# WHILE true - for consistent operation
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

    

    """ IMPORTANT CHANGE: I will add a for loop which will iterate through each line of the names.txt and intialise the current index value of names.txt, mark1.txt and mark2.txt to name, coMark and preMark respectiviely """
    
    # This for loop will iterate through each line in the names.txt
    # x will hold the index position
   
    for x in range(len(NameArray)):        

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

# Time to finish
exit() 
   