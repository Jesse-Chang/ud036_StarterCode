import media
import fresh_tomatoes

Harry_Potter_01 = media.Movie("Harry Potter and the Sorcerer's Stone",
                              "Rescued from the outrageous neglect of his"
                              " aunt and uncle, a young boy with a great"
                              " destiny proves his worth while attending"
                              " Hogwarts School of Witchcraft and Wizardry.",
                              "https://tinyurl.com/yb2os4mk",
                              "https://www.youtube.com/watch?v=z86aFALzjgs")

Harry_Potter_02 = media.Movie("Harry Potter and the Chamber of Secrets",
                              "Harry ignores warnings not to return to"
                              " Hogwarts, only to find the school plagued"
                              " by a series of mysterious"
                              " attacks and a strange voice haunting him.",
                              "https://tinyurl.com/yddd7pkk",
                              "https://www.youtube.com/watch?v=GQAxGb5njBk")

Harry_Potter_03 = media.Movie("Harry Potter and the Prisoner of Azkaban",
                              "It's Harry's third year at Hogwarts;"
                              " not only does he have a new Defense"
                              " Against the Dark Arts teacher, but"
                              " there is also trouble brewing."
                              " Convicted murderer Sirius"
                              " Black has escaped the Wizards' Prison and"
                              " is coming after Harry.",
                              "https://tinyurl.com/ybf6nssx",
                              "https://www.youtube.com/watch?v=-S79A0gIZSE")

Harry_Potter_04 = media.Movie("Harry Potter and the Goblet of Fire",
                              "A young wizard finds himself competing in a "
                              "hazardous tournament"
                              " between rival schools of magic, but he is"
                              " distracted by recurring nightmares.",
                              "https://tinyurl.com/y8cdfn44",
                              "https://www.youtube.com/watch?v=_i0EN_YHdYA")

Harry_Potter_05 = media.Movie("Harry Potter and the Order of the Phoenix",
                              "With their warning about Lord Voldemort's"
                              " return scoffed at, Harry and Dumbledore"
                              " are targeted by the Wizard authorities"
                              " as an authoritarian bureaucrat slowly seizes"
                              " power at Hogwarts.",
                              "https://tinyurl.com/y6wl9cjc",
                              "https://www.youtube.com/watch?v=Niave1bUkHw")

Harry_Potter_06 = media.Movie("Harry Potter and the Half-Blood Prince",
                              "As Harry Potter begins his sixth year at"
                              " Hogwarts, he discovers an old"
                              " book marked as the property of the"
                              " Half-Blood Prince"
                              " and begins to learn"
                              " more about Lord Voldemort's dark past.",
                              "https://tinyurl.com/y9fyem4e",
                              "https://www.youtube.com/watch?v=0gV8CdBxmjI")

Harry_Potter_07 = media.Movie("Harry Potter and the Deathly Hallows: Part 1",
                              "As Harry races against time and evil to "
                              "destroy the Horcruxes, he uncovers the"
                              " existence of three"
                              " most powerful objects in the"
                              " wizarding world: the Deathly Hallows.",
                              "https://tinyurl.com/ybjl9559",
                              "https://www.youtube.com/watch?v=l4syK6Nwdcw")

Harry_Potter_08 = media.Movie("Harry Potter and the Deathly Hallows: Part 2",
                              "Harry, Ron and Hermione search for Voldemort's"
                              " remaining Horcruxes"
                              " in their effort to destroy the Dark Lord"
                              " as the final battle rages on at Hogwarts.",
                              "https://tinyurl.com/ybn5z2rp",
                              "https://www.youtube.com/watch?v=jgpJoKDzoZ4")

movies = [Harry_Potter_01, Harry_Potter_02, Harry_Potter_03, Harry_Potter_04,
          Harry_Potter_05, Harry_Potter_06, Harry_Potter_07, Harry_Potter_08]

fresh_tomatoes.open_movies_page(movies)
