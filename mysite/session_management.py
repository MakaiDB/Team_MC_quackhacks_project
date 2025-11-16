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
import sys
import django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from mysite.models import Session
import random


def unique_code(length=9):
    """Generate a unique session code with numbers only."""
    code = random.randint(10**(length-1), 10**length - 1)
    return str(code)

print(unique_code())

def create_session(host_user):
    code = unique_code()
    session = Session(host=host_user, code=code)
    session.users.add(host_user)
    session.save()
    return session

def join_session(user, code):
    session = Session.objects.filter(code=code).first()
    if session:
        session.users.add(user)
        session.save()
        return session
    else:
        return "Invalid session code"
    