# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

arrival = media.Movie("Arrival",
                      "When twelve mysterious spacecraft appear around the world, linguistics professor Louise Banks is tasked with interpreting the language of the apparent alien visitors.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTExMzU0ODcxNDheQTJeQWpwZ15BbWU4MDE1OTI4MzAy._V1_SY1000_CR0,0,640,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g")
#print(arrival.storyline)
#arrival.show_trailer()
interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=3WzHXI5HizQ")

no_country = media.Movie("No Country for Old Men",
                         "Violence and mayhem ensue after a hunter stumbles upon a drug deal gone wrong and more than two million dollars in cash near the Rio Grande.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA5Njk3MjM4OV5BMl5BanBnXkFtZTcwMTc5MTE1MQ@@._V1_.jpg",
                         "https://www.youtube.com/watch?v=aCjnUJjWb38")

sicario = media.Movie("Sicario",
                      "An idealistic FBI agent is enlisted by a government task force to aid in the escalating war against drugs at the border area between the U.S. and Mexico.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA5NjM3NTk1M15BMl5BanBnXkFtZTgwMzg1MzU2NjE@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=sR0SDT2GeFg")

the_good = media.Movie("The Good, the Bad and the Ugly",
                       "A bounty hunting scam joins two men in an uneasy alliance against a third in a race to find a fortune in gold buried in a remote cemetery.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE2MzE5MTE5NV5BMl5BanBnXkFtZTcwODI4ODUyMQ@@._V1_.jpg",
                       "https://www.youtube.com/watch?v=WCN5JJY_wiA")
                       
amelie = media.Movie("Le Fabuleux Destin d'Amélie Poulain",
                     "Amélie is an innocent and naive girl in Paris with her own sense of justice. She decides to help those around her and, along the way, discovers love.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BNzI1OWFiN2MtYWQzYi00YmRiLTg2YmEtMjljMjBiZjI0NWQ2XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SY1000_CR0,0,692,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=HUECWi5pX7o")

movies = [arrival, interstellar, no_country, sicario, the_good, amelie]
fresh_tomatoes.open_movies_page(movies)
