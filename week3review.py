###################################
# Name:         Brendan Obilo
# Reg No:       100952871
# Description:  Week 3 Class review
# Date:         23/05/2024
####################################

main_characters = [
 ("BoJack Horseman", "Will Arnett", "Horse"),
 ("Princess Carolyn", "Amy Sedaris", "Cat"),
 ("Diane Nguyen", "Alison Brie", "Human"),
 ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
 ("Todd Chavez", "Aaron Paul", "Human")
]


for title, author, pet in main_characters:
    print(f"{title} is a {pet.lower()} voiced by {author}")

details = ("John Smith", 11743, ("Computer Science", "Mathematics"))

full_name, year, subjects = details
computer, maths = subjects

print(full_name, year, computer, maths)

album_with_details = [
 ("The Dark Side of the Moon",
  "Pink Floyd",
  1973,
  ("Speak to Me",
   "Breathe",
   "On the Run",
   "Time",
   "The Great Gig in the Sky",
   "Money",
   "Us and Them",
   "Any Colour You Like",
   "Brain Damage",
   "Eclipse"
   )
  )
]

album_dictionary = {}

for title, artiste, year, tracks in album_with_details:
    album_dictionary["title"] = title
    album_dictionary["artiste"] = artiste
    album_dictionary["year"] = year
    album_dictionary["tracks"] = tracks

print(album_dictionary)

for key, value in album_dictionary.items():
    print(f"{key}: {value}")

del album_dictionary["year"]
del album_dictionary["tracks"]

album_dictionary["year released"] = 2012

for key, value in album_dictionary.items():
    print(f"{key}: {value}")

tv_show = {"title": "Breaking Bad", "seasons": 5, "initial_release":
           2008}


def print_show_info(television_show):
    print(f"{television_show["title"]} ({television_show["initial_release"]}) - {television_show["seasons"]} seasons")


print_show_info(tv_show)
