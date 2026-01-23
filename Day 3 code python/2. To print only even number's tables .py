# write a program in which print only even numbers tables


nums = input("enter numbers seperated by space :").split()

for n in nums:
    n = int(n)

    if (n%2 != 0 ):
        continue

    print("\nTables of",n)
    for i in range(1, 11):
        print(n,"x",i,"=",n*i)

        

# nums = input("enter the number :").split()

# for n in nums :
#     n = int(n)

#     if (n%2 != 0):
#         continue

#     print("\n table of",n)
#     for i in range (1,11):
#         print(n,"x",i,"=",i*n)




