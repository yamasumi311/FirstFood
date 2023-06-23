# categories
categories = {
    "Fruits": [],
    "Grains and Roots": [],
    "Vegetables": [],
    "Legumes": [],
    "Meat/Poultry/Egg/Fish": [],
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