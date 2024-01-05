from Common.BaseUi import BasePage


class Moviespage(BasePage):
    def search_movies(self, movie_name):
        self.clean_text(self.search_bar)
        self.input_text(locator=self.search_bar,text=movie_name)
        self.keys_enter(self.search_bar)

    def get_title(self):
        return self.get_element_text(self.movie_title)
