# Write a Python program that takes salary and years of service as input.
# If the years of service are 5 or more, give a 10% bonus on the salary and print the final salary.
# Otherwise, print the salary without bonus.


a = int(input("enter salary :"))
b = int(input("enter years of service :"))
bonus = a * 0.10

if(b >= 5):
    print(a+bonus)

else:
    print("no bounus")