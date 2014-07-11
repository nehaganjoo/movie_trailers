import fresh_tomatoes

import media

toy_story = media.Movie("Toy Story", "A Story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=aVdO-cx-McA")
#print(avatar.storyline)
#avatar.show_trailer()

wake_up_sid = media.Movie("Wake up sid","A hindi drama about a boy who has no ambitions,just lives life happily",
                          "http://en.wikipedia.org/wiki/Wake_Up_Sid#mediaviewer/File:Wake_up_Sid.jpg",
                          "https://www.youtube.com/watch?v=oMnVstbgahQ")
#print(wake_up_sid.storyline)
#wake_up_sid.show_trailer()

movies =[toy_story, avatar, wake_up_sid]
fresh_tomatoes.open_movies_page(movies)
