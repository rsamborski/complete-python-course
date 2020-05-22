# Super TURBO Indestructible App !!!

movies = []


# Adding new movie
def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


# Printing out single movie details
def print_movie(movie):
    print(f"{movie['title']} by {movie['director']} from {movie['year']}")


# Printing out list of all movies
def print_movies():
    for movie in movies:
        print_movie(movie)


# Finding movie by inputted attribute and search string
def find_movie():
    attribute = input("Enter the attribute by which you are looking for (title, director, year): ")
    search_string = input("What do you search for: ")
    for movie in movies:
        if movie[attribute].lower() == search_string.lower():
            print_movie(movie)

# Display user menu and handle input
def display_menu():
    MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            add_movie()
            pass
        elif selection == "l":
            print_movies()
            pass
        elif selection == "f":
            find_movie()
            pass
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


display_menu()
