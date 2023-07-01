print("Hello, World!") #The command *print* serves to show the *Hello, World!* in the terminal.
print("Please, choose a number.")
n1 = int(input("--> ")) #the command *input* serves to change the variable *n1* using the question *-->* you can change the question every time if you want!
print("Choose another number.")
n2 = int(input("--> "))  #the *int* variable serves to add value to the *n2* variable, there are several variables such as *int(), float(), bool() and str()* the *int* being to add the value of numbers
print("Going to be addition or subtraction?")
e1 = input("--> ")
if e1 == ("addition"): #if you put *addition* in *e1* it will show the *print* command in the terminal
    print(n1 + n2) #the *print* command will take the value of the two variables *n1* *n2* and will add the value of the variables, which will show the result in the terminal

if e1 == ("subtraction"): #if you put something other than *subtraction* it will not show anything in the terminal, because the *else* command was not applied.
    print(n1 - n2)
    
