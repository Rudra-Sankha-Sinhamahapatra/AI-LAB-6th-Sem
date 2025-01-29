
names = []


for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

print("List after adding 5 names:", names)


for i in range(2):
    name = input(f"Enter additional name {i+1}: ")
    names.append(name)

print("List after adding 7 names:", names)


print("The last 4 names in the list are:", names[-4:])
