import os


def check_array_contains(newFood, items):
    """if new food is included in items, then return False
    """
    for item in items:
        if item == newFood:
            return False
    return True


def check_existing_file(baby_name):
    folder_path = '/data'
    filename = baby_name
    file_path = os.path.join(folder_path, filename)
    if os.path.exists(file_path):
        return True



# add new food in an array
def add_food(answer, items):
    while answer == 'y':
        new_food = input('Enter new food: ')
        if check_array_contains(new_food, items):
            items.append(new_food)
        else:
            print(f'{new_food} is already registered.')
        answer = input('Do you want to add more foods?(y or n): ')
        while answer != 'n' and answer != 'y':
            answer = input('Invalid input. Enter "y" to yes or "n" to no: ')


def view_list(items):
    for index, item in enumerate(items):
        print(f'{index + 1}: {item}')
