movies = [
    {"title": "Avengers", "genre": "Action", "language": "English"},
    {"title": "Inception", "genre": "Sci-Fi", "language": "English"},
    {"title": "Interstellar", "genre": "Sci-Fi", "language": "English"},
    {"title": "The Dark Knight", "genre": "Action", "language": "English"},
    {"title": "Joker", "genre": "Drama", "language": "English"},
    {"title": "Titanic", "genre": "Romance", "language": "English"},
    {"title": "Avatar", "genre": "Sci-Fi", "language": "English"},
    {"title": "John Wick", "genre": "Action", "language": "English"},
    {"title": "Forrest Gump", "genre": "Drama", "language": "English"},
    {"title": "The Notebook", "genre": "Romance", "language": "English"},

    {"title": "Vikram", "genre": "Action", "language": "Tamil"},
    {"title": "Kaithi", "genre": "Action", "language": "Tamil"},
    {"title": "Master", "genre": "Action", "language": "Tamil"},
    {"title": "96", "genre": "Romance", "language": "Tamil"},
    {"title": "Vinnaithaandi Varuvaayaa", "genre": "Romance", "language": "Tamil"},
    {"title": "Asuran", "genre": "Drama", "language": "Tamil"},
    {"title": "Soorarai Pottru", "genre": "Drama", "language": "Tamil"},
    {"title": "Doctor", "genre": "Comedy", "language": "Tamil"},

    {"title": "Bahubali", "genre": "Action", "language": "Telugu"},
    {"title": "RRR", "genre": "Action", "language": "Telugu"},
    {"title": "Pushpa", "genre": "Action", "language": "Telugu"},
    {"title": "Arjun Reddy", "genre": "Romance", "language": "Telugu"},
    {"title": "Jersey", "genre": "Drama", "language": "Telugu"},
    {"title": "Eega", "genre": "Fantasy", "language": "Telugu"},

    {"title": "Drishyam", "genre": "Thriller", "language": "Malayalam"},
    {"title": "Kumbalangi Nights", "genre": "Drama", "language": "Malayalam"},
    {"title": "Premam", "genre": "Romance", "language": "Malayalam"},
    {"title": "Bangalore Days", "genre": "Drama", "language": "Malayalam"},

    {"title": "KGF", "genre": "Action", "language": "Kannada"},
    {"title": "Kantara", "genre": "Drama", "language": "Kannada"},

    {"title": "Parasite", "genre": "Thriller", "language": "Korean"},
    {"title": "Train to Busan", "genre": "Action", "language": "Korean"},

    {"title": "Spirited Away", "genre": "Fantasy", "language": "Japanese"},
    {"title": "Your Name", "genre": "Romance", "language": "Japanese"}
]

def recommend_movies(movies, genre, language):
    perfect_match = []
    partial_match = []

    for movie in movies:
        if movie["genre"].lower() == genre.lower() and movie["language"].lower() == language.lower():
            perfect_match.append(movie["title"])
        elif movie["genre"].lower() == genre.lower() or movie["language"].lower() == language.lower():
            partial_match.append(movie["title"])

    return perfect_match + partial_match

print("MOVIE RECOMMENDATION SYSTEM")

print("\nAvailable Genres:")
print("Action, Sci-Fi, Drama, Romance, Thriller, Fantasy, Comedy")

print("\nAvailable Languages:")
print("English, Tamil, Telugu, Malayalam, Kannada, Korean, Japanese")

user_genre = input("\nEnter preferred genre: ")
user_language = input("Enter preferred language: ")

results = recommend_movies(movies, user_genre, user_language)

if results:
    print("\nRecommended Movies:")
    for movie in results:
        print("-", movie)
else:
    print("\nNo movies matched your preferences.")
