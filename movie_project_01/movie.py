class Movie:
    def __init__(self, dir, act, gen, real_yr, mov_name):
        self.director = dir
        self.actor = act
        self.genre = gen
        self.realese_year = real_yr
        self.movie_name = mov_name

    def __repr__(self):
        return f"director: {self.director}\n actor: {self.actor}\n genre: {self.genre}\n realese_year: {self.realese_year} \n movie_name : {self.movie_name}"





