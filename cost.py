"""Recipe cost calculator: day one skeleton.

Fill in each TODO, one step at a time. Run the file often:
    python cost.py
Commit to git after every step that works.
"""

# ---------------------------------------------------------------
# STEP 1: Ingredients
# Prices are in DH per kg (or per liter).
# ---------------------------------------------------------------
prices = {
    "tomato": 8.0,
    "onion": 5.0,
    "olive oil": 70.0,
    "chicken": 35.0,
}


def add_ingredient(prices: dict, name: str, price_per_kg: float) -> None:
    """Add or update an ingredient price."""
    prices[name.lower] = price_per_kg
    # TODO: put the price in the dict (lowercase the name!)
    # pass

def get_price(prices: dict, name: str) -> float:
    """Return the price per kg. Raise a clear error if it doesn't exist."""
    try : 
        return prices[name.lower]
    except KeyError : 
        print("Item doesn't exist !")
    # TODO: look it up; if missing, raise KeyError with a helpful message
    # pass


# ---------------------------------------------------------------
# STEP 2: Recipe cost
# A recipe is a list of (ingredient_name, grams) tuples.
# ---------------------------------------------------------------
salad = [
    ("tomato", 400),
    ("onion", 150),
    ("olive oil", 30),
]


def recipe_cost(recipe: list, prices: dict) -> float:
    """Total cost of a recipe in DH."""
    price = 0
    for ingedient in recipe : 
        recipe_name = ingedient[0].lower()
        print(recipe_name)
        price += ingedient[1]/1000 * prices[recipe_name]
    # TODO: loop over the recipe, convert grams to kg, multiply by price, sum up
    return price
    # pass


# ---------------------------------------------------------------
# STEP 3: Per portion and selling price
# ---------------------------------------------------------------
def cost_per_portion(total_cost: float, portions: int) -> float:
    # TODO
    return total_cost/portions
    # pass


def selling_price(cost_per_portion: float, target_food_cost: float = 0.30) -> float:
    """If food cost should be 30% of the price, price = cost / 0.30."""
    # TODO
    return cost_per_portion/target_food_cost
    pass


def main() -> None:
    total = recipe_cost(salad, prices)
    per_portion = cost_per_portion(total, portions=4)
    price = selling_price(per_portion)

    print(f"Total cost:        {total:.2f} DH")
    print(f"Cost per portion:  {per_portion:.2f} DH")
    print(f"Suggested price:   {price:.2f} DH")


if __name__ == "__main__":
    main()

# ---------------------------------------------------------------
# STEP 4 (later): save/load prices and recipes with the json module
# STEP 5 (later): turn main() into a CLI with argparse
# ---------------------------------------------------------------