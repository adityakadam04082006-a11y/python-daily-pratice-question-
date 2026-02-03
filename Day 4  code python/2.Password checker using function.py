 
# Q3️⃣ Password Checker
# Write a function check_password(pwd) that returns True if:
# length ≥ 8
# contains at least one digit
# contains at least one uppercase letter
# Else return False.
# 🧪 Example:
# Copy code
# Python
# check_password("Adi12345") → True

user_password = input("enter password - ")

def check_password(pwd):
    is_invalid= True
    if len(pwd) < 8:
        print("Error:password is too short(must be of 8+ characters)")
        is_invalid = False
    
    has_digits = False
    has_uppercase = False

    for char in pwd:
          if char .isdigit():
            has_digits = True
          elif char .isupper():
            has_uppercase = True
    
    if not has_digits:
     print("Error you forgot a number!(0-9)")
     is_invalid = False

    if not has_uppercase:
     print("Error: you forgot a captial letter!(A-z)") 
     is_invalid = False
     
    if is_invalid:
        print("Password accepted")
        return True
    else:
        print("Password not accepted")
        return False       

check_password(user_password) 
  

             
