actor_info = {"act1": ["movieC", "movieA"], "act2": ["movieA", "movieB"],
              "act3": ["movieA", "movieB"], "act4": ["movieC", "movieD"],
              "act5": ["movieD", "movieB"], "act6": ["movieE"],
              "act7": ["movieG", "movieE"], "act8": ["movieD", "movieF"],
              "KevinBacon": ["movieF"], "act10": ["movieG"], "act11": ["movieG"]}

movie_info = {'movieB': ['act2', 'act3', 'act5'], 'movieC': ['act1', 'act4'],
              'movieA': ['act1', 'act2', 'act3'], 'movieF': ['KevinBacon', 'act8'],
              'movieG': ['act7', 'act10', 'act11'], 'movieD': ['act8', 'act4', 'act5'],
              'movieE': ['act6', 'act7']}


def shortest_distance(actA, actB, actor_info, movie_info):
    if actA not in actor_info:
        return -1  # "infinity"
    if actB not in actor_info:
        return -1  # "infinity"
    if actA == actB:
        return 0

    dist = 1
    movies = set(actor_info[actA])
    end_movies = set(actor_info[actB])
    if movies & end_movies:
        return dist

    seen = movies.copy()
    print("All movies with", actA, seen)
    while 1:
        dist += 1
        next_step = set()
        for movie in movies:
            for actor in movie_info[movie]:
                next_step.update(actor_info[actor])
        print("Movies with actors from those movies", next_step)
        movies = next_step - seen
        print("New movies with actors from those movies", movies)
        if not movies:
            return -1  # "Infinity"

        # Has actorB been in any of those movies?
        if movies & end_movies:
            return dist

        # Update the set of seen movies, so I don't visit them again
        seen.update(movies)


if __name__ == "__main__":
    print(shortest_distance("act1", "KevinBacon", actor_info, movie_info))
