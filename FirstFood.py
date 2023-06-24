import os
from functions import add_food, view_list, file_exists_in_folder, read_food_from_file, get_file_path
from categories import categories_keys, get_items_from_category

# TODO Program structure
# 1. Open file and read all data to an array
# 2. Menu - add new items, or print array to screen
#      - add items:
#       - choose category
# 3. Exit - write all data from array to file

# 1
baby_name = input('Enter baby name: ')

items = read_food_from_file(baby_name)

# 2
while True:
    print('Do you want to add food? or view list?')
    choice = input('Enter "a" to add food or "b" to view list or "x" to exit: ')
    if choice == 'a':
        add_food('y', items)
    elif choice == 'b':
        view_list(items, baby_name)
    elif choice == 'x':
        break
    else:
        print('Invalid input')

objects = []


# 3
file_path = get_file_path(baby_name)
with open(file_path, 'w') as file:
    for item in items:
        file.write(str(item) + '\n')


def choose_category(categories):
    while True:
        print(f'Choose category from: {categories_keys}')
        for category in categories_keys:
            print(category)
        selected_category = input("Enter the desired category: ")

        selected_items = get_items_from_category(selected_category, categories)
        print(f"Items in the '{selected_category}' category: ")
        for item in selected_items:
            print(item)
