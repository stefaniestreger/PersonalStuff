def add_movies(filename, movies):
    movie_file = open(filename, 'a')
    for x in movies:
        movie_file.write(x + "\n")
    movie_file.close()

file_name = 'movies.txt'
new_movies = ['The Green Mile', 'The Hunger Games', 'Under the Tuscan Sun']
add_movies(file_name, new_movies)