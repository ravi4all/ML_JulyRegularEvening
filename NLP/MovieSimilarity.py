movies = [
    {
        "action" : ['Baahubali','Avengers','Terminator',
                     'Jumanji','Baaghi','Dhoom','Tiger',
                    'Raees'],
        "comedy" : ['Dhamaal','Hera Pheri', 'Golmaal'],
        "Biopic" : ['Sultan','Dangal','MS Dhoni']
    }
]

user_1 = {'Baahubali','Avengers','Terminator',
          'Jumanji','Dhamaal','Dangal','Sultan',
          'Dhoom','IT','Conjuring'}

user_2 = {'Avengers','Terminator','Dangal','Dhoom','IT',
          'Tubelight','Tiger','Krrish','Baaghi','Raees'}

simMovies = user_1.intersection(user_2)
# print(simMovies)
allMovies = user_1.union(user_2)
j = len(simMovies) / len(allMovies)

# print("Similarity is",j)

m1 = user_1 - user_2
m2 = user_2 - user_1

print("Movies Recommended for user_1",m2)
print("Movies Recommedned for user_2",m1)