def cakes(recipe, available):
    recipe_list = [element for element in recipe.keys()]
    available_list = [element for element in available.keys()]
    quantity_list = []
    if len(recipe_list) > len(available_list):
        return 0
    else:
        for element in recipe_list:
            if element not in available_list:
                return 0

    for r_element in recipe_list:
        for a_element in available_list:
            if r_element == a_element:
                quantity_list.append(available.get(a_element) // recipe.get(r_element))

    return min(quantity_list)


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

print(cakes(recipe, available))
