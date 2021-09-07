def main():
    movie_list = open('movies.txt', 'w')
    my_list = ["The Shawshank Redemption", "Urban Cowboy", "What We Do In The Shadows"]
    for x in my_list:
        movie_list.write(x + "\n")
    movie_list.close()

main() 
