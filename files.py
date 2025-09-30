from validation import validate_confirm

# Reads text file of form Name, Director, Year
# Inputs file into list where each line in file is a dictionary
# def read_file(filename):
#     movie_list = []
#     with open(filename) as file:
#         for line in file:
#             line = line[:-1] # Removes the \n from the end of each line
#             name, director, year = line.split(",")
#             movie_list.append({"name": name, "director": director, "year": year})
#     return movie_list

def read_file(filename):
    movie_list = []
    try:
        with open(filename) as file:
            for line in file:
                line = line.strip()  # Removes \n and extra spaces
                parts = line.split(",")
                if len(parts) == 3:
                    name, director, year = parts
                    movie_list.append({"name": name, "director": director, "year": year})
                else:
                    print(f"Skipping malformed line: {line}")
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty movie list.")
    return movie_list

# Saves data from list of dictionaries to text file in form Name, Dictionary, Year
# Each dictionary is a single line in the file
def save_file(filename, movie_list):
    value = validate_confirm("Do you want to save these changes? (y/n):  ")
    if value:
        with open(filename, "w") as file:
            for movie in movie_list:
                name = movie["name"]
                director = movie["director"]
                year = movie["year"]
                line = f"{name},{director},{year}\n"
                file.write(line)
 