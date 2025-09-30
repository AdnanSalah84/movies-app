list = []
movie_dict = dict(name="", length=0, director="", year=0)

while True:
    name = input("What is the name of the movie? ")
    if name == "":
        break
    while True:
        length = input(f"What is the length of {name} in minutes? ")
        if length.isdigit():
            break
        else:
            print(length + " is not a number.")
    while True:
        director = input(f"Who is the director of {name}? ")
        if director == "":
            print("This field cannot be blank")
            continue
        break
    while True:
        year = input(f"What year was {name} released? ")
        if year.isdigit():
            break
        else:
            print(year + f" is not a number. What year was {name} released? ")
    movie_dict = dict(name=name, length=length, director=director, year=year)
    list.append(movie_dict)

    while True:
        check = input("Do you want to add another movie? Enter yes or no: ")
        if check.lower() in ["no", "n"]:
            print("---------------Movie List---------------")
            for idx, movie in enumerate(list, start=1):
                print(f"{idx} \n")
                print(f"{'Name:':<20s} {movie['name']}")
                print(f"{'Length in minutes:':<20s} {movie['length']}")
                print(f"{'Director:':<20s} {movie['director']}")
                print(f"{'Year:':<20s} {movie['year']}")
                print("----------------------------------------")
            exit()
        elif check.lower() in ["yes", "y"]:
            break
        else:
            print(check + " is not a valid option. Please try again.")