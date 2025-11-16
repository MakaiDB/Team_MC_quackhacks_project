from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Session(models.Model):
    code = models.CharField(max_length=10, unique=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hosted_sessions")
    users = models.ManyToManyField(User, related_name="joined_sessions")

    def __str__(self):
        return f"Session {self.code} hosted by {self.host.name}"


class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=300)
    tmdb_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    session = models.OneToOneField(Session, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return f"Playlist for session {self.session.code}"


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    decision = models.BooleanField()  # True = Yes, False = No

    class Meta:
        unique_together = ("user", "movie", "session")  # Prevent duplicate votes

    def __str__(self):
        return f"{self.user.name} voted {'Yes' if self.decision else 'No'} on {self.movie.title}"