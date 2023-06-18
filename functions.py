def check_array_contains(newFood, items):
    """if new food is included in items, then return False
    """
    for item in items:
        if item == newFood:
            return False
    return True


def ask_more_items(answer):
    if answer == 'y':
        return True
    elif answer == 'n':
        return None
    else:
        return False
