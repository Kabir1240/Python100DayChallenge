def band_name_generator():
    print("Welcome to the Band Name Generator.")
    city_name = input("What's the name of the city you grew up in?\n")
    pet_name = input("What's your pet's name?\n")
    band_name = city_name + " "  + pet_name
    print("Your band name could be " + band_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    band_name_generator()

