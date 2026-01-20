# Question -
# Write a Python program that takes two numbers and an operator (+, -, *, /)
# as input and uses conditional statements (if, elif, else) to perform the selected operation and
# display the result in the format:

#Answer -
a = int(input("enter 1st value :"))
b = int(input("enter 2nd value :"))
c = input("select operator (+,-,*,/) :").strip()

if (c == '+'):
    print(a,"+", b, "=",a+b)

elif(c == '-'):
    print(a,"-", b, "=",a-b)

elif(c == '*'):
    print(a,"*", b, "=",a*b)

elif(c == '/'):
    print(a,"/", b, "=",a/b)    

else:
    print("invalid operator")


# logic of arrangement -
# What each part means:
# Part Meaning
# a      -- first number
# "/"    -- operator symbol (text, not math)
# b      -- second number
# "="    -- separator meaning “result is coming”
# a / b  -- actual calculation