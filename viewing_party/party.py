# ------------- WAVE 1 --------------------from HP

# def create_movie(title, genre, rating):
#     if title is None or genre is None or rating is None :
#         return None

#     new_movie = dict(title = title, genre = genre, rating = rating)

#     return new_movie

# def add_to_watched(user_data, movie):
#     watched_list = user_data["watched"]
#     watched_list.append(movie)

#     return user_data

# def add_to_watchlist(user_data, movie):
#     watchlist = user_data["watchlist"]
#     watchlist.append(movie)

#     return user_data

# def watch_movie(user_data, movie_title):
#     movie_title_to_move = None

#     for movie in user_data["watchlist"] :
#         if movie["title"] == movie_title :
#             movie_title_to_move = movie
#             break
#     if movie_title_to_move is not None:
#         user_data["watched"].append(movie_title_to_move)
#         user_data["watchlist"].remove(movie_title_to_move)

#     return user_data


# ------------- WAVE 1 --------------------from AT

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating
       }
    return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    movie_to_pop = -1
    for i in range(len(user_data["watchlist"])):
        movie = user_data["watchlist"][i]
        if movie["title"] == title:
            movie_to_pop = i
    if movie_to_pop > -1:
        user_data["watched"].append(user_data["watchlist"].pop(movie_to_pop))

    return user_data

# ------------- WAVE 2 --------------------from HP

def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]

    if not watched_list:
        return 0.0

    total_rating = 0

    for movie in watched_list:
        total_rating += movie["rating"]

    average_rating = total_rating/len(watched_list)
    return average_rating

def get_most_watched_genre(user_data):
    watched_list = user_data["watched"]

    if not watched_list:
        return None

    movie_genre_count = {}

    for movie in watched_list:
        genre = movie["genre"]

        if genre in movie_genre_count :
            movie_genre_count[genre] += 1
        else:
            movie_genre_count[genre] = 1

    popular_genre  = max(movie_genre_count, key=movie_genre_count.get)

    return popular_genre


# ------------- WAVE 3 --------------------from AT

def get_unique_watched(user_data):
    watched_movies = {}
    for movie in user_data["watched"]:
        watched_movies[movie["title"]] = movie

    for user in user_data["friends"]:
        for movie in user["watched"]:
            if movie["title"] in watched_movies:
                del watched_movies[movie["title"]]

    return list(watched_movies.values())

def get_friends_unique_watched(user_data):
    watched_movies = {}
    for user in user_data["friends"]:
        for movie in user["watched"]:
            watched_movies[movie["title"]] = movie

    for movie in user_data["watched"]:
        if movie["title"] in watched_movies:
            del watched_movies[movie["title"]]
    
    return list(watched_movies.values())

# ------------- WAVE 4 --------------------from AT

def get_available_recs(user_data):
    recommended_movies = []
    current_subscriptions = set(user_data["subscriptions"])

    friends_watched_movies = get_friends_unique_watched(user_data)

    for movie in friends_watched_movies:
        if movie["host"] in current_subscriptions:
            recommended_movies.append(movie)

    return recommended_movies


# ------------- WAVE 5 --------------------from AT

def get_new_rec_by_genre(user_data):
    recommended_movies = []
    genre_count = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_count:
            genre_count[movie["genre"]] = 0
        
        genre_count[movie["genre"]] += 1

    fav_genre = ""
    max_genre_count = -1

    for genre, count in genre_count.items():
        if max_genre_count < count:
            fav_genre = genre
            max_genre_count = count
    
    friend_movies = get_friends_unique_watched(user_data)

    for movie in friend_movies:
        if movie["genre"] == fav_genre:
            recommended_movies.append(movie)

    return recommended_movies

def get_rec_from_favorites(user_data):
    recommended_movies = []

    favorite_movies = {}

    for movie in user_data["favorites"]:
        favorite_movies[movie["title"]] = movie

    user_only_watched_movies = get_unique_watched(user_data)

    for movie in user_only_watched_movies:
        if movie["title"] in favorite_movies:
            recommended_movies.append(movie)
    
    return recommended_movies

