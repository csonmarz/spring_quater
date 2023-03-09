def multiplication(number1,number2): # functions hold the different statements and variables
    if number1 * number2 <= 1000:  # the if statemnts works as a bollean. In this case, if number1 and number 2 are LESS than or EQUAl to 1000, you multiply.
        return number1 *number2
    
    else: # Otherwise, the code will add the numbers if it goes over 1000
        return number1 + number2
    
mutiply = multiplication(84, 8) # In this line of code, we are calling the function and adding some values to give the prevoius if and else statments some numbers to work with 
print(mutiply) # print the statemnts to get the final answer 
    
