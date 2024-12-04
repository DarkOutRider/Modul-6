
import os
os.system("cls")

my_numbers = [1, 2, 3, 4, "hej"]

print(my_numbers)

for number in my_numbers:
    print(number)



print("Lista nummer 2:")

my_numbers = [1, 2, 3, 4, "hej"]
my_numbers.append("felix")

for number in my_numbers:
    print(number)



delete = input("Vilken vill du ta bort? ")
my_numbers.pop(int(delete))

for number in my_numbers:
    print(number)





items = ["kloss", "penna", "sudd", "spade"]
print(items)
print("antal saker i lista nummer 4:")
print(len(items))

print("lista nummer 5:")

items = ["kloss", "penna", "sudd", "spade"]
for item in items:
    print(item)

change = input("vilken vill du byta? ")
if change:
        new_item = input("skriv den nya saken: ")
        items[int(change)] = new_item

for item in items:
    print(item)





candy_bars = ["mars", "snickers", "break", "milky way"]

while True:
    os.system("cls")

    for bar in candy_bars:
        print(bar)
    position = input("vilken vill du välja? ")
    choice = input("\nvill du ändra (1), radera (2) eller lägga till (3)? ")

    if choice == "1":
        new_name = input("skriv nytt namn på chokladen")
        candy_bars[int(position)] = new_name

    if choice == "2":
        candy_bars.pop(int(position))
    
    if choice == "3":
        addition = input("vilken choklad vill du lägga till? ")
        candy_bars.append(addition)