import requests
import json

def movie_info():
    api_key = 'de87c4c6dc96c2e871432e62a2bdb7e2'
    language = 'ko'
    region = 'KR'
    
    movie_info_result = []
    for i in range(1, 21):
      page = i
      URL = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language={language}&page={page}&region={region}'

      response = requests.get(URL).json()['results']

      for movie in response:
        movie_info = { "model": "movies.movie", 
          "pk": movie['id'], 
          "fields": movie
          }
      
        movie_info_result.append(movie_info)

        
    file_path = './movies.json'
    with open(file_path, 'w', encoding='utf-8') as outfile:
        json.dump(movie_info_result, outfile, indent=4, ensure_ascii=False)

movie_info()