user_count = int(input("Enter user count : "))
user = [
    {
        "name":"farzin",
        "age": 21
    },
    {
        "name":"nima",
        "age": 45
    },
    {
        "name":"amir",
        "age": 67
    },
    {
      "name":"mostafa",
      "age": 97
    }]
for i in range(user_count):
    name = input("Enter user name : ")
    if name == user[0]["name"]:
        print(f"user name age is {user[0]['age']}")
    elif name == user[1]["name"]:
        print(f"user name age is {user[1]['age']}")
    elif name == user[2]["name"]:
        print(f"user name age is {user[2]['age']}")
    elif name == user[3]["name"]:
        print(f"user name age is {user[3]['age']}")
    else:
        print("there is no user with this given name!")
        break







