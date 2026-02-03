# Q2 – Number Analyzer (function to classify number as positive/negative/zero and 
# even/odd)
num = int(input("enter number :"))
def analyze_num(n):
    if n == 0:
        result = ("Zero")

    elif(n > 0 and n %2 == 0):
        result = ("positive even")
    elif(n > 0 and n %2 != 0):
        result = ("positive odd")  
    elif(n < 0 and n %2 == 0):
        result = ("negative even")  
    else:
        result = ("negative odd")           

    return result
print(analyze_num(num))
