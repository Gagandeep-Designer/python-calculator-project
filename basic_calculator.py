# Things you should know to make this project:
# 1.variables
# 2.float
# 3.basic math
# 4.if/else if/ else 

# The user's inputs for the numbers and the operators
while True:
    num1=float(input("Enter Your First Number:-\n"))
    operator_type=input("Enter Operator\n")
    num2=float(input("Enter Your Second Number:-\n"))

    # if operator is(+,-,/,*,%,//,**) then print out number 1(+,-,/,*,%,//,**)number 2
    if operator_type=="+":
        print(num1+num2)
    elif operator_type=="-":
        print(num1-num2)
    elif operator_type=="/":
        print(num1/num2)
    elif operator_type=="*":
        print(num1*num2)
    elif operator_type=="//":
        print(num1//num2)
    elif operator_type=="%":
        print(num1%num2)
    elif operator_type=="**":
        print(num1**num2)

    # if the user didn't put any operator 
    else:
        print("Not a Valid Operator Try Again.....Please 👍")

