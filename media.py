import webbrowser


class Movie():
    """This class provides a way to store movies related information

    Attributes:
        title: movie name
        storyline: brief intro of the movie
        poster_image_url: poster image
        trailfer_youtube_url: url found from youtube
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Initialize class Movie(). Pass all the inputs to attributes"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Use default webbrowser to open up YouTube trailer"""
        webbrowser.open(self.trailer_youtube_url)
