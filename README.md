# SimplyFi_Python-Assignment
# Question 1: Python code for converting integer values to Indian currency notations without using any library
    # Approach: We have taken the user input which needs to be converted into Indian currency notation
    # Checking for the input is positive or negative
    # Checking the length of given input if it is less than 3 digit then return the value as it
    # If input is greater than 3 digit and less than equal to 5 digit then formating the output as desired
    # If input is greater than and equal to 6 digit, then we are doing the substring and removing the last three digits, then again doing the substring to get the 2 digits and running it untill there are no substring available more than 2 and appending it to the list
    # Reversing the list to get the desired output and joining the list on basic of ","
    # Formatting the output
# Question 2: You won’t get caught if you hide behind someone
    # We are takin the user inputs
    # Number of test cases
    # Number of persons and height of Ali and Gi-Hun
    # Height of the persons
    # Checking the Number persons equals the heights of the persons
    # Mapping the user inputs using the dictionary
    # Than iterating through the dictionary and comparing the height of Ali with the other persons between Ali and Gi-Hun using the condition x[0][1] < x[1][i] and using flag to count the persons and than appending to the output list
    # Than printing the list