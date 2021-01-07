import fresh_tomatoes 
import media
toy_story = media.Movie('Toy Story', 'A story of a boy and his toys that come to life', 'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg','https://www.youtube.com/watch?v=rNk1Wi8SvNc')

#print(toy_story.storyline)
#print(toy_story.poster_image)

avator = media.Movie('Avator','A marine on an alien planet','https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg','https://www.youtube.com/watch?v=5PSNL1qE6VY')

#print(avator.storyline)
#avator.show_trailer()

ironman = media.Movie('Ironman','A billionaire industrialist and genius inventor, Tony Stark (Robert Downey Jr.), is conducting weapons tests overseas','https://upload.wikimedia.org/wikipedia/en/4/47/Iron_Man_%28circa_2018%29.png','https://www.youtube.com/watch?v=8ugaeA-nMTc')
#ironman.show_trailer()

# Create list
movies = [toy_story, avator, ironman]
# Takes in array list of movies
#Execute html file movie list
#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

# Print predefined variables, you will see "This class provides a way to store movie related information"

print(media.Movie.__doc__)