"""
List of movies read in from file
User can add movies (name, director and year)
Remove movies (by name or index)
Search for movies (by name or director)
List all movies (with an index number)
User can save updated list to file
"""

from files import *
from movie import *
import validation as val

def main(movie_list):
    repeat = True
    print("\n----------- Welcome -----------")
    while repeat:
        choice = val.validate_choice()
        if choice == 1:
            enter_movies(movie_list)
        elif choice == 2:
            remove_movies(movie_list)
        elif choice == 3:
            search_movies(movie_list)
        else:
            output_movies(movie_list)

        repeat = val.validate_confirm("Do you want to do something else? (y/n): ")

    save_file("movie_list.txt", movie_list)


if __name__ == "__main__":
    main(read_file("movie_list.txt"))