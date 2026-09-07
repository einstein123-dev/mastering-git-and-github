#function shapes

def clean_name(name):
    return name.strip().title()

print(clean_name("  alice  ")) 

def calculate_volume(*args):
    volume = 1
    for arg in args:
        volume *= arg
    return volume
print(calculate_volume(4,8,9), "cm")

def calculate_area(*args):
    area =1
    for arg in args:
        area *= arg
    return area
print(calculate_area(45,2))

#action function
def write_log(messege):
    with open(r"C:\Users\User\Desktop\hello.txt","a") as file:
              file.write(messege)

    print("Done")
write_log("how are you doing")


#clean an email and split it into usernamr and domain

def cln_split_email(email):
     clean = email.strip().lower()
     name,domain = clean.split("@")
     return {"name":name,"domain":domain}

print(cln_split_email("richardeinstein40@gmail.com"))

def clean_data(email):
     clean = email.strip().lower()
     name,domain = clean.split("@")
     return {"username":name,"Domain":domain}
print(clean_data("einsteinamanfo@gmail.com"))
    
#check if email has a basic valid format


def email_validation(email):
     return ("@" in email and "." in email)

print(email_validation("richard@gmail"))
     


#example object cars

# car1 = {
#     "make": "Toyota",
#     "model": "Camry",
#     "year": 2020,
#     "color": "blue"
# }
# for key,value in car1.items():
#     print(f"{key}:{value}")