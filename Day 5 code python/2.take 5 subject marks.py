def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "c"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"    

marks = []
subject = ["maths","english","science","history","geography"]    

print(".....enter marks of 5 subject.....")

for i in range(5):
    score = float(input(f"enter marks for {subject[i]}:")) 
    marks.append(score)

total_marks = sum(marks)   
avg = total_marks/len(marks)  

grade = calculate_grade(avg)

print(f"student report:")
print(f"total marks:   {total_marks:.2f},out of 500")
print(f"average: {avg: 2f}")
print(f"Final grade:{grade}")