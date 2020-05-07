class MoviesDb:
    def __init__(self):
        self.movies_db = []

    def add_movie(self, m):
        self.movies_db.append(m)

    def show_movies(self):
        print(f"{len(self.movies_db)} movies stored in db and below are Details:: ")
        for m in self.movies_db:
            print(m)
            print()

    def find_movie_details_by_name(self,mn):
        for m in self.movies_db:
            if (m.movie_name).lower() == mn.lower():
                return m

    def add_movie_to_db_txt_file(self,mov_dt):
        f1 = open("movie_db.txt","w")
        f2 = f"{mov_dt.director},{mov_dt.actor},{mov_dt.genre},{mov_dt.realese_year},{mov_dt.movie_name}"

        f1.write(str(f2+"\n"))
        f1.close()













