# categories
categories = {
    "Fruits": [],
    "Grains/Roots": [],
    "Vegetables": [],
    "Legumes": [],
    "Meat/Fish/Eggs": [],
    "Dairy": [],
    "Natural Seasonings": [],
    "Seeds/Nuts": []
}


categories_keys = categories.keys()


def get_items_from_category(selected_category, categories):
    if selected_category in categories:
        return categories[selected_category]
    else:
        return []

def add_to_category(category, new_food, categories):
    categories[category].append(new_food)
