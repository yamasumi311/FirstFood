import os


def check_array_contains(newFood, items):
    """if new food is included in items, then return False
    """
    for item in items:
        if item == newFood:
            return False
    return True


def file_exists_in_folder(file_path):
    return os.path.exists(file_path)


def read_food_from_file(baby_name):
    items = []  # create an empty array
    file_name = baby_name
    file_path = get_file_path(file_name)
    # check if file is already exists
    if file_exists_in_folder(file_path):
        # open existing file
        with open(file_path, 'r') as file:
            # retrieve items into items array
            for line in file:
                items.append(line.strip())
    return items


def get_file_path(file_name):
    folder_path = 'data'
    file_path = os.path.join(folder_path, file_name)
    return file_path

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



def view_list(items, baby_name):
    print(f'{baby_name} has had {len(items)} foods!!')
    print(f'List of food {baby_name} tried:')
    for index, item in enumerate(items):
        print(f'{index + 1}: {item}')

    print(f'{100 - len(items)} more foods until 100!')

    if len(items) == 100:
        print(f'Hooray!! {baby_name} has tried 100 foods!!')


