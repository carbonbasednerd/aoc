def load_data(file):
    data = open(file, 'r')
    total_calories = []
    temp_calories = 0
    for line in data:
        stripped = line.strip()
        if stripped == "":
            total_calories.append(temp_calories)
            temp_calories = 0
        else:
            calories = int(stripped)
            temp_calories += calories

    data.close()
    return total_calories

if __name__ == "__main__":
    total_cal = load_data("data_1")
    total_cal.sort(reverse=True)
    print(f"Max : {total_cal[0]}")
    print(f"Top Three : {total_cal[0]+total_cal[1]+total_cal[2]}")