spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [item["name"]for item in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    x = []
    for item in spicy_foods:
        if item["heat_level"] > 5:
            x.append(item)
    return x

    pass

def print_spicy_foods(spicy_foods):
    # def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]

        heat_level_emoji = "🌶" * heat_level  # Generating heat level emojis

        output = f"{name} ({cuisine}) | Heat Level: {heat_level_emoji}"
        print(output)
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # def get_spicy_food_by_cuisine(spicy_foods,cuisine):
  for food in spicy_foods:
    if food["cuisine"] == cuisine:
      return food
    pass

def print_spiciest_foods(spicy_foods):
    for item in spicy_foods:
        if item["heat_level"]>5:
            name = item["name"]
            cuisine = item["cuisine"]
            heat_level = item["heat_level"]
            heat_level_emoji= "🌶" * heat_level
            out_put = f"{name} ({cuisine}) | Heat Level: {heat_level_emoji}"
            print(out_put)
    
    pass

def get_average_heat_level(spicy_foods):
    total_foods = 0
    num_of_foods = len(spicy_foods)
    for item in spicy_foods:
        heat_level= item["heat_level"]
        total_foods += heat_level
        average_heat= total_foods/num_of_foods      
    return average_heat

    pass
added_list = {
     "name": "Chiken_nuggets",
        "cuisine": "Chinese ",
        "heat_level": 4,
  }
def create_spicy_food(spicy_foods, spicy_food):
    all_list = spicy_foods
    all_list.append(spicy_food)
    return all_list


    pass
