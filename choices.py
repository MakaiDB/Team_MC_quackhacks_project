#get input from users (what movies they want to watch)
# present all of the input options to users one by one and get their yes/no vote on each movie
# #all movies that are slected with everyone choosing yes' return a list of those movies
# if only one movie got everyones yes return that movie
#if multiple movies got voted yes by every user randomly select one of those movies
#returns the movie selected
import random
import doctest

movie_list = input("Enter the list of movies separated by commas: ").split(',')
num_users = int(input("Enter the number of users: "))
user_votes = []
def get_movie_choice(movie_list, num_users, user_votes=[]): 
    """ Get movie choice based on user votes. If multiple movies get all yes votes, randomly select one. 
    >>> get_movie_choice(['Cat in the Hat', 'Despicable Me', 'LEGO Movie'], 2, ['yes', 'yes', 'no', 'yes', 'yes', 'no'])
    ['Cat in the Hat']

    """
    for i in range(num_users):
        votes = [] 
        movie = []
        print(f"User {i+1}, please vote on the following movies:")
        for movie in movie_list:
            vote = input(f"Do you want to watch '{movie.strip()}'? (yes/no): ").strip().lower() #get user vote
            user_votes.append(vote) #add vote to user votes
            if all(user_votes) == 'yes': #if everyone voted yes for the movie 
                votes.append(movie) #add movie to votes list
            elif len(user_votes) > 1: #if more than one movie got all yes votes
                random.choice(votes) #randomly select one of those movies
                votes.append(movie) #add movie to user votes
        return votes
        
def main():
    selected_movies = get_movie_choice(movie_list, num_users, user_votes)
    print("Selected movie:", selected_movies)
    doctest.testmod(verbose=True)
if __name__ == "__main__":
    main()


