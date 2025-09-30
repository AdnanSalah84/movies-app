import validation as val

# Allows the user to enter movies into a list of dictionaries
def enter_movies(movie_list):
    repeat = True
    while repeat:
        name = val.validate_string("\nEnter movie title: ", "Enter a valid movie title: ")
        director = val.validate_string("Enter director: ", "Enter a valid director: ")
        year = val.validate_int("Enter the year that the movie was released: ", "Enter a valid year for the movie: ")

        movie_list.append({"name": name.title(), "director": director.title(), "year": int(year)})

        repeat = val.validate_confirm("Do you want to enter another movie? (y/n):  ")

# Allows the user to remove movies from a lost of dictionaries
# Can remove using movie name or movie index
def remove_movies(movie_list):
    repeat = True
    while repeat:
        value = val.validate_input("What movie would you like to delete?: ", "Enter a valid movie title or index: ")

        # Since input can be int or string, this try/except block determines which before
        # deleting the movie
        try:
            value = int(value)
            if 1 <= value <= len(movie_list) + 1:
                print_movie((movie_list[value - 1]))
                confirm = val.validate_confirm("Do you want to delete this movie? (y/n):  ")
                if confirm:
                    movie_list.pop(value - 1)
            else:
                print("Invalid index", end="")
                continue

        except ValueError:
            if list(filter(lambda m: m["name"] == value, movie_list)):
                for index, movie in enumerate(movie_list):
                    if movie["name"] == value.title():
                        print_movie((movie_list[index]))
                        confirm = val.validate_confirm("Do you want to delete this movie? (y/n):  ")
                        if confirm:
                            movie_list.pop(index)
            else:
                print("Invalid movie name", end="")
                continue

        repeat = val.validate_confirm("Do you want to delete another movie? (y/n):  ")

# Allows user to search the list of dictionaries for movies using movie name or director name
# Allows for partial matches
def search_movies(movie_list):
    repeat = True
    while repeat:
        value = val.validate_string("\nSearch for a movie: ", "Enter a valid input: ").title()
        searched_movies = list(filter(lambda m: value in m["name"], movie_list))
        searched_movies += list(filter(lambda m: value in m["director"], movie_list))
        output_movies(searched_movies)

        repeat = val.validate_confirm("Do you want to search for another movie? (y/n):  ")

# Prints a single formatted movie
def print_movie(movie):
    print(f"\n{'Name:':<10} {movie['name']}"
          f"\n{'Director:':<10} {movie['director']}"
          f"\n{'Year:':<10} {movie['year']}")

# Prints a list of formatted movies
# Gives each movie an index
def output_movies(movie_list):
    movie_list.sort(key=lambda m: m["name"])

    print("\nMovie List:")
    for index, movie in enumerate(movie_list):
        print(f"\n{index + 1} -------------------------------")
        print_movie(movie)
 