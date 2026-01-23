# write multiple tables at once by using loops and also adjust limit 

nums = input("enter numbers and make it seperate by space :").split()
limit = int(input("enter the limit :"))

for n in nums :
    n =  int(n)
    print("\ntable of :",n)
    i = 1
    while i <= limit :
        print(n,"x",i,"=",n*i)
        i += 1




# nums = input("enter numbers and make it seperate by space :").split()


# for n in nums :
#     n =  int(n)
#     print("\ntable of :",n)
#     i = 1
#     while i <= 10 :
#         print(n,"x",i,"=",n*i)
#         i += 1

