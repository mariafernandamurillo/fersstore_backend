#Some pythom recap

#How to create a function
#Use the reserved word: def
#It is different to js where we use function
def print_total():
    print("Your total is: 123")

#Execute the funtion
print_total()


#A function with an argument
def can_drink(age):
    #Instructions: print if the user can or not drink alcohol base on the age
    if (age < 18):
        print("You are a baby. Not drinking yet.")
    else:
        print("Go drink everything!")

#Again, call the function
can_drink(20) #Yes!
can_drink(11) #No :(


#Data structures: list.

def users():
    people = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 35},
        {'name': 'Dave', 'age': 40},
        {'name': 'Emily', 'age': 45},
        ]
    #print every dictionary 
    for each_user in people:
        print(each_user)

    #print only names
    for user in people:
        print(user["name"])
    
    #print name of users over 30 years old
    for each_user in people:
        if(each_user["age"] > 30):
            print(each_user["name"] + "_" + str(each_user["age"])) 

    #print the sum of all ages
    total = 0;
    for each_user in people:
        total += each_user["age"]
    
    print(f"total age is: {total}")


    #Find an specific user name and print it
    name = input("What user are you looking for?: ")
    found = False
    for each_user in people:
        if(name.lower() == each_user["name"].lower()):
            found = True
            print(each_user["name"] + "=>" + str(each_user["age"]))
        
    if not found:
        print("Not found!")

users()

