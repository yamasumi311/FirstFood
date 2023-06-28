import json

# categories
empty_categories = {
    "Fruits": [],
    "Grains/Roots": [],
    "Vegetables": [],
    "Legumes": [],
    "Meat/Fish/Eggs": [],
    "Dairy": [],
    "Natural Seasonings": [],
    "Seeds/Nuts": []
}


categories_keys = empty_categories.keys()


def get_items_from_category(selected_category, categories):
    if selected_category in categories:
        return categories[selected_category]
    else:
        return []

def add_to_category(category, new_food, categories):
    for item in categories[category]:
        if item == new_food:
            return False
    return categories[category].append(new_food)

def remove_from_category(category, selected_food, categories):
    print(category)
    print(selected_food)
    print(categories)
    if category in categories:
        for food in categories[category]:
            if food == selected_food:
                return categories[category].remove(selected_food)
        return False
