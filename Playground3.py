"""
User can add movie (name, director and year)
Remove movie (by name or index)
Search for movie (by name or director)
List all movies (with an index number)
"""
from movie_list import movies


def validate_int(question, validation):
    value = input(question)
    while True:
        try:
            int(value)
            return value
        except ValueError:
            value = input(validation)


def validate_string(question, validation):
    value = input(question)
    while True:
        if value.rstrip() == '':
            value = input(validation)
        else:
            return value


def validate_input(question, validation):
    value = input("\n" + question)
    while True:
        try:
            int(value)
            return value
        except ValueError:
            if value.rstrip() == '':
                value = input(validation)
            else:
                return value


def validate_quit(question):
    value = input("\n" + question).lower()
    while True:
        if value in ["y", "yes"]:
            return True
        elif value in ["n", "no", "quit", "exit"]:
            return False
        else:
            value = input("Enter either 'y' or 'n': ").lower()


def validate_choice():
    print(f"\nType:"
          f"\n1. to enter movies"
          f"\n2. to remove movies"
          f"\n3. to search movies"
          f"\n4. to list all movies")
    value = input("\nEnter your choice: ").lower()
    while True:
        if value in ["1", "one", "enter", "e", "ent"]:
            return 1
        elif value in ["2", "two", "remove", "delete", "r", "d", "rem", "del"]:
            return 2
        elif value in ["3", "three", "search", "se", "s"]:
            return 3
        elif value in ["4", "four", "list", "l", "ls"]:
            return 4
        else:
            value = input("Invalid option. Re-enter your choice: ")


def enter_movies(movie_list):
    repeat = True
    while repeat:
        name = validate_string("\nEnter movie title: ", "Enter a valid movie title: ")
        director = validate_string("Enter director: ", "Enter a valid director: ")
        year = validate_int("Enter the year that the movie was released: ", "Enter a valid year for the movie: ")

        movie_list.append({"name": name.title(), "director": director.title(), "year": int(year)})

        repeat = validate_quit("Do you want to enter another movie? (y/n):  ")


def remove_movie(movie_list):
    repeat = True
    while repeat:
        value = validate_input("What movie would you like to delete?: ", "Enter a valid movie title: ")

        # Since input can be int or string, this try/except block determines which before
        # deleting the movie
        try:
            value = int(value)
            print_movie((movie_list[value - 1]))
            confirm = validate_quit("Do you want to delete this movie? (y/n):  ")
            if confirm:
                movie_list.pop(value - 1)

        except ValueError:
            for index, movie in enumerate(movie_list):
                if movie["name"] == value.title():
                    print_movie((movie_list[index]))
                    confirm = validate_quit("Do you want to delete this movie? (y/n):  ")
                    if confirm:
                        movie_list.pop(index)

        repeat = validate_quit("Do you want to delete another movie? (y/n):  ")


def search_movies(movie_list):
    repeat = True
    while repeat:
        value = validate_string("\nSearch for a movie: ", "Enter a valid input: ").title()
        searched_movies = list(filter(lambda m: value in m["name"], movie_list))
        searched_movies += list(filter(lambda m: value in m["director"], movie_list))
        output_movies(searched_movies)

        repeat = validate_quit("Do you want to search for another movie? (y/n):  ")


def print_movie(movie):
    print(f"\n{'Name:':<10} {movie['name']}"
          f"\n{'Director:':<10} {movie['director']}"
          f"\n{'Year:':<10} {movie['year']}")


def output_movies(movie_list):
    movie_list.sort(key=lambda m: m["name"])

    print("\nMovie List:")
    for index, movie in enumerate(movie_list):
        print(f"\n{index + 1}. -----------------------------------")
        print_movie(movie)



def main(movie_list):
    repeat = True
    print("\nWelcome")
    while repeat:
        choice = validate_choice()
        if choice == 1:
            enter_movies(movie_list)
        elif choice == 2:
            remove_movie(movie_list)
        elif choice == 3:
            search_movies(movie_list)
        else:
            output_movies(movie_list)

        repeat = validate_quit("Do you want to do something else? (y/n): ")


if __name__ == "__main__":
    main(movies)