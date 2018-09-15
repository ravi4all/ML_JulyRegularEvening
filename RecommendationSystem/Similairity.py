dataset = [
    {'action' : ["terminator","batman","iron man","thor","hulk",
          "baahubali",'jumanji',"dabang","mi"],
     'comedy' : ['mask','fukrey'],
     'biopic' : ['sultan','dangal','ms dhoni','gold']
     }
]

user_1 = {"terminator","batman","iron man","thor","hulk",
          "baahubali","dangal","sultan","gold","dabang"}

user_2 = {"gold","batman","terminator","thor","mask","ms dhoni",
          "fukrey","jumanji","iron man","hulk"}

numer = len(user_1.intersection(user_2))
denom = len(user_1.union(user_2))

j = numer / denom

print("Similarity is",j*100)

action = 0
comedy = 0
biopic = 0

similarMovies = user_1.intersection(user_2)
print("Similar movies",similarMovies)

for movie in similarMovies:
    for data in dataset:
        if movie in data['action']:
            action += 1
        elif movie in data['comedy']:
            comedy += 1
        elif movie in data['biopic']:
            biopic += 1

print("Action : {}, Comedy : {}, Biopic : {}".format(action,comedy,biopic))

category = ""

if action > comedy and action > biopic:
    category = 'action'
elif comedy > action and comedy > biopic:
    category = 'comedy'
else:
    category = 'biopic'

for movie in dataset[0][category]:
    if movie not in similarMovies:
        print("Recommended", movie)