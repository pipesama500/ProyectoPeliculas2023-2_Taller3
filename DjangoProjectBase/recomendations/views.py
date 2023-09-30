from django.shortcuts import render
from movie.models import Movie
from dotenv import load_dotenv, find_dotenv
import json
import os
import openai
from openai.embeddings_utils import get_embedding, cosine_similarity
import numpy as np
def recomendations_function(request):
    searchTerm = request.GET.get('searchMovie')
    result = []
    if searchTerm != None:
        print(searchTerm)
        _ = load_dotenv('openAI.env')
        openai.api_key  = os.environ['openAI_api_key']
        with open('movie_descriptions_embeddings.json', 'r') as file:
            file_content = file.read()
            movies = json.loads(file_content)
        req = searchTerm
        emb = get_embedding(req,engine='text-embedding-ada-002')
        sim = []
        for i in range(len(movies)):
            sim.append(cosine_similarity(emb,movies[i]['embedding']))
        sim = np.array(sim)
        ordered_sim = np.argsort(sim)[-3:][::-1]
        for idx in ordered_sim:
            result.append(movies[idx])
            print(movies[idx]['title'])
    return render(request, 'recomendations.html', {'searchTerm':searchTerm,'result':result, 'movies':Movie.objects.all()})