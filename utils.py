from pdf_parser import extract_text_from_chunk

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

def sort_chunks_by_tfidf(pdf_chunks, user_query):
    chunk_texts = []
    # Extract the text from each chunk
    for chunk in pdf_chunks:
        chunk_text = extract_text_from_chunk(chunk)
        chunk_texts.append(chunk_text)
        
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(chunk_texts)  # Includes user_query implicitly

    query_tfidf = vectorizer.transform([user_query])
    cosine_similarities = (query_tfidf * tfidf_matrix.T).toarray()  

    # Get chunk indices in ascending order of similarity
    sorted_indices = cosine_similarities.argsort()[0][::-1] 

    return [pdf_chunks[i] for i in sorted_indices]  