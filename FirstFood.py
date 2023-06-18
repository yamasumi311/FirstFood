# baby's name
baby_name = input('Enter baby name: ')
file_name = 'FoodList'

def add_items():
    # open FoodList file in append mode
    index = 0
    with open(file_name, 'a') as file:
        # write a new food to the file
        new_food = input('Enter new food: ')
        if check_items(new_food):
            index =+ 1
            file.write(f"{index}.{new_food}\n")
            return index, new_food
        return print('This item is already registered!')

# check items so that there is no duplication
def check_items(user_input):
    with open(file_name, 'r') as file:
        for i in file:
            item = i.pop()
            if item == user_input:
                return False
        return True

add_items()
# show how many foods have been tried
print(f'{baby_name} has had {index} foods!!')
