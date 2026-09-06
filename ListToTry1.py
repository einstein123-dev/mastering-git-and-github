someOfMyFriends = ["Alice", "Bob", "Charlie", "David", "Eve"]

#printing each name in the list
for friend in someOfMyFriends:
    print(friend)

for friend in someOfMyFriends:
    print(f"Hello,{friend}! How are you doing !?")

print(f"Hello,{someOfMyFriends[0]}/ How are you doing !?")
print(f"Hello,{someOfMyFriends[1]}! How are you doing !?")
print(f"Hello,{someOfMyFriends[2]}/ How are you doing !?")
print(f"Hello,{someOfMyFriends[3]}/ How are you doing !?")
print(f"Hello,{someOfMyFriends[4]}! How are you doing !?")

#list of makes of motorcycles
motorcycles = ["Honda", "Yamaha", "Suzuki", "Kawasaki"]

for moto in motorcycles:
    print(f"I would like to own a {moto} motorcycle.")
#repalcing a name in the list
someOfMyFriends[0] = "Lawrencia"


#adding new friends to the list
someOfMyFriends.append("Frank")
print(someOfMyFriends)

#inserting a new friend at a specific position in the list
someOfMyFriends.insert(2, "Grace")
print(someOfMyFriends)

#removing a friend from the list using the del statement
del someOfMyFriends[3]
print(someOfMyFriends)

#list of possible dinner guests celebrities living and dead
dinnerGuests = ["Albert Einstein", "Marie Curie", "Isaac Newton", "Leonardo da Vinci", "Ada Lovelace", "Sarkodie","joe metella"]

message1 = f"Hello {dinnerGuests[5]}, I would like to invite you to dinner."
message2 = f"Hello {dinnerGuests[6]}, I would like to invite you to dinner."
print(message1)
print(message2)
unavailable_guest = dinnerGuests.pop(5)
dinnerGuests.insert(5, "Kofi Annan")
message3 = f"Hello {dinnerGuests[5]}, I would like to invite you to dinner."
print(message3)

print(dir(dinnerGuests))

def greet():
    for guest in dinnerGuests:
        print(f"Hello {guest}, I would like to invite you to dinner.")

greet()