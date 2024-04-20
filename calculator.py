print("Welcome to the calculator")

print("Enter the numbers below" )
x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
    
def add(x,y):
    return x + y
    
def sub(x,y):
    return x - y
    
def mult(x,y):
    return x * y
    
def div(x,y):
    return x / y
    
operate = input("What operation would you like to perform (mult, add, sub, div): ")
if operate == "add":
        print(x, "+", y,  "= " , add(x,y))
elif operate == "sub":
        print(x, "-", y, "= " , sub(x,y))
elif operate == "mult":
        print(x, "*", y, "= " , mult(x,y))
elif operate == "div":
        print(x ,"/", y ,"= ", div(x,y))
else:
        print("Invalid Operation. Try again")
        
