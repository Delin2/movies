import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of toys that came to life",
                        "https://images-na.ssl-images-amazon.com/images/I/51K8r9COEQL.jpg",
                        "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

#print(toy_story.title)
#toy_story.show_trailer()

titanic = media.Movie("Titanic",
                      "Epic and action-packed romance set against the ill-fated maiden voyage of the R.M.S. Titanic",
                      "https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UY222_CR0,0,150,222_AL.jpg",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

#titanic.show_trailer()

kung_fu_hustle = media.Movie("Kung Fu Hustle",
                      "When the hapless Sing (Stephen Chow) and his dim-witted pal, Bone (Feng Xiaogang), try to scam the residents of Pig Sty Alley into thinking they're members of the dreaded Axe Gang, the real gangsters descend on this Shanghai slum to restore their fearsome reputation.",
                      "http://www.gstatic.com/tv/thumb/v22vodart/35470/p35470_v_v8_aa.jpg",
                      "https://www.youtube.com/watch?v=VSfJZ6B4P6Y")

avatar = media.Movie("Avatar",
                      "On the lush alien world of Pandora live the Navi, beings who appear primitive but are highly evolved. Because the planet's environment is poisonous, human/Na'vi hybrids, called Avatars, must link to human minds to allow for free movement on Pandora.",
                      "https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UY222_CR0,0,150,222_AL.jpg",
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")

kimi_no_na_wa = media.Movie("Kimi no Na wa",
                      "Kimi no Na wa. revolves around Mitsuha and Taki's actions, which begin to have a dramatic impact on each other's lives, weaving them into a fabric held together by fate and circumstance.",
                      "https://cdn.myanimelist.net/images/anime/5/87048.jpg",
                      "https://www.youtube.com/watch?v=3KR8_igDs1Y")

fullmetal_alchemist_brotherhood = media.Movie("Fullmetal Alchemist: Brotherhood",
                      "Alchemy is bound by this Law of Equivalent Exchange—something the young brothers Edward and Alphonse Elric only realize after attempting human transmutation: the one forbidden act of alchemy. Edward loses his left leg, Alphonse his physical body. It is only by the desperate sacrifice of Edward right arm that he is able to affix Alphonse soul to a suit of armor. Devastated and alone, it is the hope that they would both eventually return to their original bodies that gives Edward the inspiration to obtain metal limbs called automail and become a state alchemist, the Fullmetal Alchemist.",
                      "https://cdn.myanimelist.net/images/anime/1223/96541.jpg",
                      "https://www.youtube.com/watch?v=--IcmZkvL0Q")

movies = [toy_story, titanic, kung_fu_hustle, avatar, kimi_no_na_wa, fullmetal_alchemist_brotherhood]
fresh_tomatoes.open_movies_page(movies)
