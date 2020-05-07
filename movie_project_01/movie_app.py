from movie_project_01.movie import Movie
from movie_project_01.movies_db import MoviesDb

mdb = MoviesDb()

balck_panther = Movie("j ross", "Chadwick Bosema", "action", 2008, "black panther")
# print(balck_panther)

inception = Movie("Christopher", "Leonardo  Dicaprio", "action", 2010, "inception")


# print(inception)

def input_movie_details_byconsole():
    movie_name = input("Movie Name: ")
    director_name = input("Director Name: ")
    release_year = int(input("Release Year: "))
    genre = input("genre (separated by comma): ")
    actors = input("Actors Names (separated by comma): ")

    movie_by_user = Movie(director_name, actors, genre, release_year, movie_name)

    return movie_by_user


movie_usr = input_movie_details_byconsole()
#mdb.add_movie(balck_panther)
#mdb.add_movie(inception)
#serch_result = mdb.find_movie_details_by_name("Black panther")
#mdb.add_movie(movie_usr)
#mdb.show_movies()
mdb.add_movie_to_db_txt_file(movie_usr)
#print(serch_result)