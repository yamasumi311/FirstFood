# baby's name
baby_name = input('Enter baby name: ')

# open FoodList file in append mode
file_name = 'FoodList'
index = 0
with open(file_name, 'a') as file:
    # write a new food to the file
    new_food = input('Enter new food: ')
    index =+ 1
    file.write(f"{index}.{new_food} + \n")

# show how many foods have been tried
print(f'{baby_name} has had {index} foods!!')
