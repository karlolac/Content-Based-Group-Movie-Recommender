import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



def clean_title(title):
    title = str(title).lower()
    title = re.sub(r'\s*\(\d{4}\)', '', title) # Miče godinu (2009)
    if ', the' in title: title = 'the ' + title.replace(', the', '')
    if ', a' in title: title = 'a ' + title.replace(', a', '')
    if ', an' in title: title = 'an ' + title.replace(', an', '')
    return title.strip()

def prepare_data():
    U Djangu će se ovo pozvati samo jednom pri pokretanju."""
    data_tags = pd.read_csv('ml-latest-small/tags.csv')
    data_movies = pd.read_csv('ml-latest-small/movies.csv')
    
    metadata = pd.merge(data_tags, data_movies, on="movieId")
    metadata = metadata.drop_duplicates(subset='title').reset_index(drop=True)
    
    metadata['genres'] = metadata['genres'].str.replace('|', ' ', regex=False).str.lower()
    metadata['tag'] = metadata['tag'].fillna('').str.lower()
    metadata['soup'] = metadata['tag'].astype(str) + ' ' + metadata['genres'].astype(str)
    metadata['clean_title'] = metadata['title'].apply(clean_title)
    
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(metadata['soup'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()
    
    return metadata, cosine_sim, indices



def get_recommendations_from_list(movie_list, metadata, cosine_sim, indices):
    valid_indices = []
    found_titles = []
    
    for movie_input in movie_list:
        clean_input = clean_title(movie_input)
        match = metadata[metadata['clean_title'] == clean_input]
       
        if not match.empty:
            actual_title = match.iloc[0]['title']
            idx = indices[actual_title]
            
            if not isinstance(idx, (int, np.integer)):
                idx = idx.iloc[0]
                
            valid_indices.append(idx)
            found_titles.append(actual_title)

    if not valid_indices:
        return None
    
    sim_scores_total = np.sum(cosine_sim[valid_indices], axis=0)
    sim_scores = list(enumerate(sim_scores_total))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    final_recommendation_indices = []
    for i in sim_scores:
        title_at_idx = metadata['title'].iloc[i[0]]
        # Preskoči ako je film već na listi unosa
        if title_at_idx not in found_titles:
            final_recommendation_indices.append(i[0])
        
        # PROMIJENJENO: Ovdje je granica podignuta s 10 na 15 filmova
        if len(final_recommendation_indices) == 15: 
            break

    return metadata[['title', 'genres']].iloc[final_recommendation_indices]

#test
if __name__ == "__main__":
    meta, sim, idxs = prepare_data()
    test_movies = ['Interstellar', 'Inception', 'Matrix, The ']
    results = get_recommendations_from_list(test_movies, meta, sim, idxs)
    if results is not None:
        print(results)
    else:
        print("Nema pronađenih filmova.")
