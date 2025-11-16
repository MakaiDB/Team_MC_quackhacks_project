"""
Create sessions with a host user and a unique code to allow users to join

def create_session(host_user)
    code = random  digits must be 9 characters long
    session = Session(host=host_user, code=code)
    add host_user to session's user list
    return session

def join_session(user, code)
    session = find session where session.code == code
    if session exists
        add user to the session's user list
        return session
    else
        return None

def search_for_movie(query):
    url = TMDb search endpoint with query parameters
    parameters = {TMBD_API_KEY, query}
    response = send GET request to TMDb
    return response[results]

def add_movie_to_playlist(session, movie_data):
    check if movie already exsists in database
    movie = get movie from database
    playlist = session.playlist
    if movie not in playlist
        add movie to playlist
        return "Movie added to playlist"
    if movie in playlist
        return "Movie already in playlist"

"""
import os
from core.models import Session, Movie
import random 
import requests

def unique_code(length=9):
    """Generate a unique session code with numbers only."""
    code = random.randint(10**(length-1), 10**length - 1)
    return str(code)


def create_session(host_user):
    """Create and return a Session with a unique code and host as a member."""
    code = unique_code()
    session = Session.objects.create(host=host_user, session_id = code)
    session.users.add(host_user)
    return session

def join_session(user, code):
    """Add a user to an existing session by code and return the session or None."""
    session = Session.objects.filter(code=code).first()
    if session:
        session.users.add(user)
        session.save()
        return session
    else:
        print("Session not found")
        return None
    
def search_for_movie(query):
    """Return list of TMDb results for query (empty list on error)."""
    if not os.getenv("TMDB_API_KEY"):
        print("TMDB API key not set")
        return []
    url = "https://api.themoviedb.org/3/search/movie"
    parameters = {
        "api_key": os.getenv("TMDB_API_KEY"),
        "query": query
    }
    try:
        response = requests.get(url, params=parameters, timeout=5)
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.RequestException:
        print("Error fetching data from TMDb")
        return []
    
def add_movie_to_playlist(session, movie_data):
    """'''
    movie_data expected to include at least 'id' (TMDb id) and 'title'.
    Creates or finds Movie, adds to session.playlist if not already present.
    Returns tuple (movie, created, message).
    """
    tmdb_id = movie_data.get("id")
    title = movie_data.get("title") or movie_data.get("name") or "Untitled"

    if tmdb_id is None:
        return None, False, "Missing TMDb id"

    movie, created = Movie.objects.get_or_create(tmdb_id=str(tmdb_id), defaults={"title": title})

    if session.playlist.filter(pk=movie.pk).exists():
        return movie, False, "Movie already in playlist"

    session.playlist.add(movie)
    return movie, created, "Movie added to playlist"


def main():
    from django.contrib.auth.models import User
    host_user = User.objects.first()
    session = create_session(host_user)
    print(f"Created session with code: {session.code}")