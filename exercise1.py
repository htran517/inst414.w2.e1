import json

with open('imdb_movies_1985to2022.json', 'r') as f:
    arr = []
    for line in f:
        this_movie = json.loads(line)
        for i in range(len(this_movie['actors'])):
            if this_movie['actors'][i][1] == 'Hugh Jackman':
                arr.append(this_movie['rating']['avg'])
print(sum(arr)/len(arr))
        
