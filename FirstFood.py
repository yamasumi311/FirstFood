import os

from functions import add_food, view_list

baby_name = input('Enter baby name: ')
file_name = baby_name
# check if file is already exists
if os.path.exists(baby_name):
    # open existing file
    with open(file_name, 'r') as file:
        # retrieve items into items array
        items = file.readlines()
    print('Do you want to add food? or view list?')
    choice = input('Enter "a" to add food or "b" to view list: ')
    while choice != 'a' and choice != 'b':
        print('Invalid input')
        choice = input('Enter "a" to add food or "b" to view list: ')
        if choice == 'a':
            add_food('y')
        elif choice == 'b':
            view_list(items)
else:  # if file is not exists
    items = []  # create an empty array
    add_food('y')


print(f'{baby_name} has had {len(items)} foods!!')
print(f'List of food {baby_name} tried:')
for index, item in enumerate(items):
    print(f'{index + 1}: {item}')

print(f'{100 - len(items)} more foods until 100!')

if len(items) == 100:
    print(f'Hooray!! {baby_name} has tried 100 foods!!')


with open(file_name, 'a') as file:
    for item in items:
        file.write(str(item) + '\n')

