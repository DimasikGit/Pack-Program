stroke = int(input("Enter length:"))

user_list = []

lists = 0
while lists < stroke:
    string = "Enter element #" + str(lists + 1) + ": "
    user_list.append(input(string))
    lists += 1

print(user_list)