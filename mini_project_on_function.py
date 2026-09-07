#Receive an email from the user as input.

# Validate the email to ensure it meets required criteria (e.g., proper format, required fields present).

# If the email is invalid, log the error details to a file for future reference.

# If the email is valid, clean and structure the email data (e.g., remove unnecessary whitespace, standardize fields, extract key information).

# Log each step of the program's execution for monitoring and debugging purposes.

import sys
email = input("Please Enter your email: ")

def is_email_valid(email):
    checked="@" in email and "." in email
    if checked :
        return(email)
    else:
        if "@" not in email and "." not in email:
            with open (r"C:\Users\User\Desktop\hell.txt","a") as file:
                file.write("Your email is missing the required @ and . please enter a valid email \n\t")
            # return "Your email is missing the required @ and . please enter a valid email"
            sys.exit()
    
        elif "@" not in email:
            with open (r"C:\Users\User\Desktop\hell.txt","a") as file:
                            file.write("Your email is missing the required @ please enter a valid email")
            # return "Your email is missing the required . please enter a valid email \n\t"
            sys.exit()

        elif "." not in email:
              with open (r"C:\Users\User\Desktop\hell.txt","a") as file:
                                        file.write("Your email is missing the required . please enter a valid email")
            #   return "Your email is missing the required . please enter a valid email"
               
        else:
                sys.exit()
                return("Check again \n")
        
if is_email_valid(email):
        valid_mail = is_email_valid(email)
else:
        sys.exit()
        

def clean_mail(valid_mail):
        cleaned = valid_mail.lower().strip()
        name,domain = cleaned.split("@")
        return {"username" :name, "Domain":domain}
        
print(is_email_valid(email))
print(clean_mail(valid_mail))
