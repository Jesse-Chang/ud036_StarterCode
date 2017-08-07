import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys",
						"http://upload.wifimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
					 "A story of avatar",
					 "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#avatar.show_trailer()

master = media.Movie("Master", "A story of Master", "https://upload.wikimedia.org/wikipedia/zh/c/c9/The_Grand_Masters_poster.jpg","https://www.youtube.com/watch?v=1g9W7xbR68Y")

FF8 = media.Movie("The Fate of the Furious", "A story of Cars", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMxODI2NDM5Nl5BMl5BanBnXkFtZTgwNjgzOTk1MTI@._V1_SY1000_CR0,0,631,1000_AL_.jpg", "http://www.imdb.com/videoplayer/vi1498461721?playlistId=tt4630562&ref_=tt_ov_vi")

Atomic_Blonde = media.Movie("Atomic Blonde", "A story of cold", "https://s.yimg.com/vu/movies/fp/mpost/69/22/6922.jpg", "https://www.youtube.com/watch?v=F8yc6AferkY")



Harry_Potter_01 = media.Movie("Harry Potter and the Sorcerer's Stone",
				   "Rescued from the outrageous neglect of his aunt and uncle, a young boy with a great destiny proves his worth while attending Hogwarts School of Witchcraft and Wizardry.",
				   "https://images-na.ssl-images-amazon.com/images/M/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_.jpg",
				   "https://www.youtube.com/watch?v=z86aFALzjgs")

Harry_Potter_02 = media.Movie("Harry Potter and the Chamber of Secrets",
							  "Harry ignores warnings not to return to Hogwarts, only to find the school plagued by a series of mysterious attacks and a strange voice haunting him.",
							  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTcxODgwMDkxNV5BMl5BanBnXkFtZTYwMDk2MDg3._V1_.jpg",
							  "https://www.youtube.com/watch?v=GQAxGb5njBk")

Harry_Potter_03 = media.Movie("Harry Potter and the Prisoner of Azkaban",
							  "It's Harry's third year at Hogwarts; not only does he have a new Defense Against the Dark Arts teacher, but there is also trouble brewing. Convicted murderer Sirius Black has escaped the Wizards' Prison and is coming after Harry.",
							  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY4NTIwODg0N15BMl5BanBnXkFtZTcwOTc0MjEzMw@@._V1_SY1000_CR0,0,676,1000_AL_.jpg",
							  "https://www.youtube.com/watch?v=-S79A0gIZSE")

Harry_Potter_04 = media.Movie("Harry Potter and the Goblet of Fire",
							  "A young wizard finds himself competing in a hazardous tournament between rival schools of magic, but he is distracted by recurring nightmares.",
							  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI1NDMyMjExOF5BMl5BanBnXkFtZTcwOTc4MjQzMQ@@._V1_.jpg",
							  "https://www.youtube.com/watch?v=_i0EN_YHdYA")

Harry_Potter_05 = media.Movie("Harry Potter and the Order of the Phoenix",
							  "With their warning about Lord Voldemort's return scoffed at, Harry and Dumbledore are targeted by the Wizard authorities as an authoritarian bureaucrat slowly seizes power at Hogwarts.",
							  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM0NTczMTUzOV5BMl5BanBnXkFtZTYwMzIxNTg3._V1_.jpg",
							  "https://www.youtube.com/watch?v=Niave1bUkHw")

Harry_Potter_06 = media.Movie("Harry Potter and the Half-Blood Prince",
							  "As Harry Potter begins his sixth year at Hogwarts, he discovers an old book marked as the property of the Half-Blood Prince and begins to learn more about Lord Voldemort's dark past.",
							  "https://images-na.ssl-images-amazon.com/images/M/MV5BNzU3NDg4NTAyNV5BMl5BanBnXkFtZTcwOTg2ODg1Mg@@._V1_SY1000_CR0,0,648,1000_AL_.jpg",
							  "https://www.youtube.com/watch?v=0gV8CdBxmjI")

Harry_Potter_07 = media.Movie("Harry Potter and the Deathly Hallows: Part 1",
							  "As Harry races against time and evil to destroy the Horcruxes, he uncovers the existence of three most powerful objects in the wizarding world: the Deathly Hallows.",
							  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ2OTE1Mjk0N15BMl5BanBnXkFtZTcwODE3MDAwNA@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
							  "https://www.youtube.com/watch?v=l4syK6Nwdcw")

Harry_Potter_08 = media.Movie("Harry Potter and the Deathly Hallows: Part 2",
							  "Harry, Ron and Hermione search for Voldemort's remaining Horcruxes in their effort to destroy the Dark Lord as the final battle rages on at Hogwarts.",
							  "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIyZGU4YzUtNDkzYi00ZDRhLTljYzctYTMxMDQ4M2E0Y2YxXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_SX667_CR0,0,667,999_AL_.jpg",
							  "https://www.youtube.com/watch?v=jgpJoKDzoZ4")

movies = [Harry_Potter_01, Harry_Potter_02, Harry_Potter_03, Harry_Potter_04, Harry_Potter_05,
          Harry_Potter_06, Harry_Potter_07, Harry_Potter_08]
fresh_tomatoes.open_movies_page(movies)