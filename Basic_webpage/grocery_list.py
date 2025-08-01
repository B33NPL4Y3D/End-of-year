grocery_list = []

while True:
    item = input("Enter a grocery item or type'done' to finish: ")
    if item.lower() == 'done':
        print(grocery_list)
        break
    grocery_list.append(item)

print("\nYour grocery list: ")
for item in grocery_list:
    print("-", item)


delete_item = input("\nEnter an item to delete from your grocery listor type delete to remove")
if delete_item.lower() == in grocery_list: