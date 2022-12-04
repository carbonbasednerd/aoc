from itertools import product
from functools import reduce

def load_ingredients(file):
    ingredients = []
    data = open(file, 'r')
    for line in data:
        parsed_line = line.strip().split(" ")
        name = parsed_line[0].strip(':')
        capacity = int(parsed_line[2].strip(","))
        durability = int(parsed_line[4].strip(","))
        flavor = int(parsed_line[6].strip(","))
        texture = int(parsed_line[8].strip(","))
        calories = int(parsed_line[10])

        ingredients.append([name, capacity, durability, flavor, texture, calories])

    data.close()
    return ingredients

if __name__ == "__main__":
    ingredients = load_ingredients("data_15")

    best_score = 0
    best_calorie_score = 0
    total = 0
    ingredients_count = len(ingredients)
    individual_count = len(ingredients[0])
    # print(len(permutations(range(100), count)))
    # print(len(functools.reduce(lambda a: list(permutations(range(100), count))))
    for x in product(range(100), repeat=ingredients_count):
        total = 0
        for y in x:
           total += y

        if total == 100:
            sub_total = []
            for a in range(1, individual_count):
                temp_total = 0
                for b in range(0, ingredients_count):
                    temp_total += (ingredients[b][a]*x[b])

                if temp_total < 0:
                    sub_total.append(0)
                else:
                    sub_total.append(temp_total)

            calories = sub_total[-1]
            ingredient_score = reduce(lambda c, d: c*d, sub_total[0:-1])
            if ingredient_score > best_score:
                best_score = ingredient_score
            if calories == 500:
                if ingredient_score > best_calorie_score:
                    best_calorie_score = ingredient_score

    print(f"Best score : {best_score}")
    print(f"Best Calorie Score : {best_calorie_score}")


