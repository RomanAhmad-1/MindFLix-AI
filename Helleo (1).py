import random

# ======================================================
#                    MINDFLIX AI
#                    AICT PROJECT
#
#       Designed By Abdul Moueed & Roman Ahmad
# ======================================================

# ======================================================
# MOVIE DATABASE
# ======================================================

movies = {

    "Action": [

        "John Wick",
        "John Wick: Chapter 2",
        "John Wick: Chapter 3 - Parabellum",
        "John Wick: Chapter 4",

        "Jumanji",
        "Jumanji: Welcome to the Jungle",
        "Jumanji: The Next Level",

        "Mission Impossible",
        "Mission Impossible: Fallout",
        "Mission Impossible: Dead Reckoning",

        "Mad Max: Fury Road",
        "Top Gun: Maverick",
        "Extraction",
        "The Raid",
        "Nobody",
        "Baby Driver",
        "Avatar",
        "Django Unchained"
    ],

    "Emotional": [

        "The Shawshank Redemption",
        "Forrest Gump",
        "A Silent Voice",
        "Your Name",
        "The Pursuit of Happyness",
        "The Green Mile",
        "La La Land",
        "Her",
        "Soul",
        "Aftersun",

        "The Perks of Being a Wallflower",
        "Manchester by the Sea",
        "Children of Heaven",
        "The Kite Runner",
        "Scent of a Woman",
        "Ikiru",
        "The Curious Case of Benjamin Button",
        "The Pianist",
        "Taste of Cherry"
    ],

    "Mind-Bending": [

        "Interstellar",
        "Inception",
        "The Matrix",
        "Fight Club",
        "Shutter Island",
        "Memento",
        "Arrival",
        "Predestination",
        "The Prestige",
        "Tenet",

        "Project Hail Mary",
        "The Martian",
        "Gravity",
        "2001: A Space Odyssey",
        "Blade Runner",
        "Blade Runner 2049",
        "The Man From Earth",
        "Voyage of Time",
        "Eternal Sunshine of the Spotless Mind",
        "The Tree of Life"
    ],

    "Comfort": [

        "Spirited Away",
        "Toy Story",
        "Ratatouille",
        "Paddington 2",
        "Spider-Man: Into the Spider-Verse",
        "Rush Hour",
        "Superbad",
        "Coco",
        "Howl's Moving Castle",
        "The Secret Life of Walter Mitty",

        "Back to the Future",
        "Colour of Wizard",
        "Mary Shelley",
        "Frankenstein"
    ],

    "Dark": [

        "Joker",
        "Se7en",
        "Prisoners",
        "Nightcrawler",
        "Gone Girl",
        "Black Swan",
        "Parasite",
        "Taxi Driver",
        "American Psycho",
        "The Batman",

        "The Silence of the Lambs",
        "Oldboy",
        "The Machinist",
        "There Will Be Blood",
        "No Country for Old Men",
        "Perfect Strangers",
        "No Other Choice",
        "Kill Bill",
        "The Godfather"
    ]
}

# ======================================================
# SCORES
# ======================================================

scores = {

    "Action": 0,
    "Emotional": 0,
    "Mind-Bending": 0,
    "Comfort": 0,
    "Dark": 0
}

# ======================================================
# INTRO
# ======================================================

print("=" * 70)
print("                       MINDFLIX AI")
print("                       AICT PROJECT")
print()
print("         Designed By Abdul Moueed & Roman Ahmad")
print("=" * 70)

# ======================================================
# QUESTION 1
# ======================================================

while True:

    print("\n1. What do you want tonight?\n")

    print("A. Action")
    print("B. Emotional")
    print("C. Mind-Blowing")
    print("D. Comfort Watch")
    print("E. Dark Story")

    choice = input("\nChoose (A/B/C/D/E): ").strip().upper()

    if choice == "A":

        scores["Action"] += 5
        break

    elif choice == "B":

        scores["Emotional"] += 5
        break

    elif choice == "C":

        scores["Mind-Bending"] += 5
        break

    elif choice == "D":

        scores["Comfort"] += 5
        break

    elif choice == "E":

        scores["Dark"] += 5
        break

    else:

        print("\n❌ Wrong Choice! Please choose again.")

# ======================================================
# QUESTION 2
# ======================================================

while True:

    print("\n2. What's your mood?\n")

    print("A. Excited")
    print("B. Sad")
    print("C. Curious")
    print("D. Tired")

    choice = input("\nChoose (A/B/C/D): ").strip().upper()

    if choice == "A":

        scores["Action"] += 3
        break

    elif choice == "B":

        scores["Emotional"] += 3
        scores["Comfort"] += 1
        break

    elif choice == "C":

        scores["Mind-Bending"] += 3
        break

    elif choice == "D":

        scores["Comfort"] += 3
        break

    else:

        print("\n❌ Wrong Choice! Please choose again.")

# ======================================================
# QUESTION 3
# ======================================================

while True:

    print("\n3. How should the movie end?\n")

    print("A. Happy")
    print("B. Emotional")
    print("C. Mind-Blowing Twist")
    print("D. Dark")

    choice = input("\nChoose (A/B/C/D): ").strip().upper()

    if choice == "A":

        scores["Comfort"] += 2
        scores["Emotional"] += 2
        break

    elif choice == "B":

        scores["Emotional"] += 3
        break

    elif choice == "C":

        scores["Mind-Bending"] += 3
        break

    elif choice == "D":

        scores["Dark"] += 3
        break

    else:

        print("\n❌ Wrong Choice! Please choose again.")

# ======================================================
# QUESTION 4
# ======================================================

while True:

    print("\n4. How deep should the movie be?\n")

    print("A. Simple & Fun")
    print("B. Balanced")
    print("C. Deep & Thought-Provoking")

    choice = input("\nChoose (A/B/C): ").strip().upper()

    if choice == "A":

        scores["Comfort"] += 2
        scores["Action"] += 2
        break

    elif choice == "B":

        scores["Emotional"] += 2
        break

    elif choice == "C":

        scores["Mind-Bending"] += 3
        scores["Dark"] += 2
        break

    else:

        print("\n❌ Wrong Choice! Please choose again.")

# ======================================================
# FIND BEST GENRE
# ======================================================

best_genre = max(scores, key=scores.get)

# ======================================================
# PICK 3 RANDOM MOVIES
# ======================================================

recommended_movies = random.sample(
    movies[best_genre],
    3
)

# ======================================================
# RESULTS
# ======================================================

print("\n" + "=" * 70)

print(f"\n🎬 Recommended Genre: {best_genre}")

print("\n🍿 Your Movie Picks:\n")

for index, movie in enumerate(recommended_movies, start=1):

    print(f"{index}. {movie}")

print("\nEnjoy Your Movie Night 🍿")

# ======================================================
# WEBSITE
# ======================================================

print("\n🌐 Visit Our Website:")
print("https://movie-mood-match--gamerxstorm88.replit.app")

print("\n" + "=" * 70)
x=input("are you satisfied?")