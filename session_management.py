"""
Create sessions with a host user and a unique code to allow users to join

def create_session(host_user)
    code = random str + digits must be 9 characters long
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
import random
import string

def unique_code(length=9):
    characters = string.ascii_letters + string.digits
    