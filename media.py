import webbrowser


class Movie():
    """Create class Movie and define member"""
    
    VAILD_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        """Initialize title, storyline, image url, youtube url"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Show trailer by input youtube url"""
        webbrowser.open(self.trailer_youtube_url)
