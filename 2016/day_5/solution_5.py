import hashlib
import sys
import random
import string

# door_id = "abc"
door_id = "reyedfim"


def generate_movie_output(current_cracked):
    digits = random.choices(string.digits, k=4)
    letters = random.choices(string.ascii_uppercase, k=4)
    sample = random.sample(digits + letters, 8)
    result = ''.join(sample)
    display = ""
    for c in range(0, len(current_cracked)):
        if current_cracked[c] == "-":
            display += result[c]
        else:
            display += current_cracked[c]
    return display


if __name__ == "__main__":
    password = ["-", "-", "-", "-", "-", "-", "-", "-"]
    counter = 0
    found_pass = 0

    while found_pass < 8:
        hash_value = hashlib.md5(f"{door_id}{counter}".encode("utf-8")).hexdigest()
        if hash_value[0:5] == "00000":
            if hash_value[5].isnumeric() and int(hash_value[5]) in range(0, 8) and password[int(hash_value[5])] == "-":
                password[int(hash_value[5])] = hash_value[6]
                 # password[found_pass] = hash_value[5]  # part one bit
                found_pass += 1
        counter += 1

        movie_visual = generate_movie_output(password)

        sys.stdout.write(f"\b\b\b\b\b\b\b\b{movie_visual}")
        sys.stdout.flush()

    print("\nHacked!")
