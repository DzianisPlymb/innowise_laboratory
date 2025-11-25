def generate_profile(currentAge):
    if currentAge < 0:
        return "Not born"
    if currentAge >= 0 and currentAge <= 12:
        return "Child"
    if currentAge >= 13 and currentAge <= 19:
        return "Teenager"
    elif currentAge >= 20:
        return "Adult"


def main():

    user_profile = {}

    user_name = input("""Enter your dull name: """) or "Unknown"
    user_profile["Name"] = user_name

    birth_year = int(input("Enter your birth day: ")) or 2000
    current_age = 2025 - birth_year
    user_profile["Age"] = current_age

    life_stage = generate_profile(current_age)
    user_profile["Life Stage"] = life_stage

    hobbies = []
    count = 0
    while(True):
        hobbie = input("Enter a favorite hobby or type \"stop\" to finish: ")
        if hobbie == "stop":
            break
        else:
            hobbies.append(hobbie)
            count += 1

    print("---")


    for key, value in user_profile.items():
        print(f"{key}: {value}")

    if not hobbies:
        print("You didn`t mention any hobbies.")
    else:
        print(f"Favorite hobbies({count}): ")
        for hobby in hobbies:
            print(f"- {hobby}")

    print("---")

if __name__ == '__main__':
    main()