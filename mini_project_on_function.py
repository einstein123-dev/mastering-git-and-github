email = input("Please Enter your email: ")

def is_email_valid(email):
    checked="@" in email and "." in email
    if checked :
        return("is valid")
    else:
        if "@" not in email and "." not in email:
            with open (r"C:\Users\User\Desktop\hell.txt","a") as file:
                file.write("Your email is missing the required @ and . please enter a valid email \n\t")
            return "Your email is missing the required @ and . please enter a valid email"
    
        elif "@" not in email:
            with open (r"C:\Users\User\Desktop\hell.txt","a") as file:
                            file.write("Your email is missing the required @ please enter a valid email")
            return "Your email is missing the required . please enter a valid email \n\t"

        elif "." not in email:
              with open (r"C:\Users\User\Desktop\hell.txt","a") as file:
                                        file.write("Your email is missing the required . please enter a valid email")
              return "Your email is missing the required . please enter a valid email"

        else:
                return("Check again \n")

              

        
print(is_email_valid(email))
