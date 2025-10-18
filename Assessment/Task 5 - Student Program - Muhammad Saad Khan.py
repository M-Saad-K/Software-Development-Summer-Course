"""
@ Author: Muhammad Saad Khan
@ Title: Task 5 - Student Program - Muhammad Saad Khan
@ Version: Python 3.12.4 v2025.8.0 - Microsoft
@ Date: 2025 - 07- 08

This is the fixed program the suits the brief of a Task 3 & 4 after testing it using the log

Description:

The program takes one student's name, coursework mark and prelim mark then calculates and displays their percentage and grade
"""

### THIS IS FOR MULTI-STUDENT ANALYSIS ###

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


# WHILE "name is equal to an empty string, and coMark and preMark are both equal to 0"
while True:


    # Take the userinput of the candidates's name
    name = input("Please Enter Candidate's Name: ")

    # IF it only contains numeric characters
    if (name.isdigit()): # is.digits function checks if name string contains only numeric characters
        
        # THEN print that this is a invalid name.
        print("Invalid Name") 

        # CONTINUE to jump back to the start of the loop
        continue

    else:

        # Do Nothing
        print("Name = ", name)


    # Take the userinput of the candidates's coursework mark out of 60 as an int 
    coMark = int(input("Please Enter Candidate's Courswork Mark out of 60: "))

    # IF userinput is less than or equal to 60.
    if coMark <=60:
        
        # THEN pass
        pass

    else:

        # ELSE print that this is an invalid mark
        print("This is an invalid mark")

        # CONTINUE to jump back to the start of the loop
        continue

    
    # Take the userinput of the candidates's prelim mark out of 90 as an int
    preMark = int(input("Please Enter Your Prelim Mark out of 90: "))

    # IF userinput is less than or equal to 90
    if preMark <= 90:

        # THEN pass
        print("preMark = ", preMark)
        print(type(preMark))

        # BREAK the loop, Ending the while and moving to the next section
        break

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
print(f"{name} has achieved {per}% overall, being awarded a grade of {grade}")
# "Laika has achieved 75% overall, being awarded a grade of A"


    






