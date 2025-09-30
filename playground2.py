"""
User can add movie
Remove movie (by name or index)
Search for movie (by name or director)
List all movies (with an index number)

Name
Director
Length (in mins)
Year
"""

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


def enter_movies():
    repeat = True
    while repeat:
        name = validate_string("\nEnter movie title: ", "Enter a valid movie title: ")
        director = validate_string("Enter director: ", "Enter a valid director: ")
        year = validate_int("Enter the year that the movie was released: ", "Enter a valid year for the movie: ")

        movies.append({"name": name.title(), "director": director.title(), "year": year})

        repeat = validate_quit("Do you want to enter another movie? (y/n):  ")


def remove_movie(movie_list):
    repeat = True
    while repeat:
        value = validate_input("What movie would you like to delete?: ", "Enter a valid movie title: ")

        # If input is an integer
        try:
            value = int(value)
            print_movie((movie_list[value - 1]))
            confirm = validate_quit("Do you want to delete this movie? (y/n):  ")
            if confirm:
                movie_list.pop(value - 1)

        # If input is a string
        except ValueError:
            for index, movie in enumerate(movie_list):
                if movie["name"] == value.title():
                    print_movie((movie_list[index]))
                    confirm = validate_quit("Do you want to delete this movie? (y/n):  ")
                    if confirm:
                        movie_list.pop(index)
        output_movies(movie_list)
        repeat = validate_quit("Do you want to delete another movie? (y/n):  ")


def search_movies(movie_list):
    searched_movies = []
    repeat = True
    while repeat:
        value = input("\n Search for a movie (by name or director): ").title()
        for movie in movie_list:
            if value in movie["name"]:
                searched_movies.append(movie)
            elif value in movie["director"]:
                searched_movies.append(movie)

        output_movies(searched_movies)
        repeat = validate_quit("Do you want to search for another movie? (y/n):  ")



def print_movie(movie):
    print(f"\n{'Name:':<10} {movie['name']}"
          f"\n{'Director:':<10} {movie['director']}"
          f"\n{'Year:':<10} {movie['year']}")


def output_movies(movie_list):
    print("\nMovie List:")
    for index, movie in enumerate(movie_list):
        print(f"\n{index + 1}. -----------------------------------")
        print_movie(movie)



def main():
    #enter_movies()
    output_movies(movies)
    #remove_movie(movies)
    search_movies(movies)



movies = [
    {
        "name": "The Shawshank Redemption",
        "director": "Frank Darabont",
        "year": 1994
    },
    {
        "name": "Inception",
        "director": "Christopher Nolan",
        "year": 2010
    },
    {
        "name": "Parasite",
        "director": "Bong Joon-ho",
        "year": 2019
    },
    {
        "name": "The Godfather",
        "director": "Francis Ford Coppola",
        "year": 1972
    },
    {
        "name": "Spirited Away",
        "director": "Hayao Miyazaki",
        "year": 2001
    },
    {
        "name": "Jaws",
        "director": "Steven Spielberg",
        "year": 1975
    },
    {
        "name": "Star Wars",
        "director": "George Lucas",
        "year": 1977
    },
    {
        "name": "Vanilla Sky",
        "director": "Cameron Crowe",
        "year": 2001
    },
    {
        "name": "The Mission",
        "director": "Rolan Joffe",
        "year": 1986
    },
    {
        "name": "Bridget Jones Diary",
        "director": "Sharron McGuire",
        "year": 2001
    }
]

if __name__ == "__main__":
    main()