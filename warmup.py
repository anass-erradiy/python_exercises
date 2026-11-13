prices = {
    "tomato": 8.0,
    "onion": 5.0,
    "olive oil": 70.0,
    "chicken": 35.0,
}

tagine = [
    ("chicken", 1200),
    ("onion", 400),
    ("tomato", 300),
    ("olive oil", 60),
]
def recipe_cost(recipe: list, prices: dict) -> float:
    """Total cost of a recipe in DH."""
    price = 0
    for ingedient in recipe : 
        recipe_name = ingedient[0]
        price = +ingedient[1]/1000 * prices[recipe_name]
    # TODO: loop over the recipe, convert grams to kg, multiply by price, sum up
    return price
    # pass

recipe_cost(tagine,prices)