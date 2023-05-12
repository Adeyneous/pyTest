# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
products_df = pd.read_csv("products.csv")

# Create a TF-IDF vectorizer object
tfidf = TfidfVectorizer(stop_words='english')

# Replace NaN values with an empty string
products_df['description'] = products_df['description'].fillna('')

# Construct the TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(products_df['description'])

# Compute the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Define a function to get the top n similar products based on the cosine similarity score
def get_top_similar_products(product_id, n=5):
    # Get the index of the product from its id
    idx = products_df[products_df['id'] == product_id].index[0]

    # Get the pairwise similarity score of the product with all the products
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the products based on the similarity score in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top n similar products excluding the input product
    top_products_idx = [i[0] for i in sim_scores[1:n+1]]

    # Return the top similar products
    return products_df.iloc[top_products_idx]

# Example usage
get_top_similar_products(1, n=3)
