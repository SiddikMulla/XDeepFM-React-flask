import numpy as np
from scipy.sparse import load_npz
import json

# Load ratings_matrix and item_similarity for each category from disk
ratings_matrices = {}
item_similarities = {}
user_to_indexes = {}
item_to_indexes = {}

def load_matrices(category):
    ratings_matrix = load_npz(f'/home/anonymou/CapstoneProject/csr_matrix/{category}_ratings_matrix.npz')
    item_similarity = load_npz(f'/home/anonymou/CapstoneProject/csr_matrix/{category}_item_similarity.npz')

    with open(f'/home/anonymou/CapstoneProject/csr_matrix/{category}_user_to_index.json', 'r') as user_file:
        user_to_index = json.load(user_file)

    with open(f'/home/anonymou/CapstoneProject/csr_matrix/{category}_item_to_index.json', 'r') as item_file:
        item_to_index = json.load(item_file)

    return ratings_matrix, item_similarity, user_to_index, item_to_index

def initialize_matrices(categories):
    global ratings_matrices, item_similarities, user_to_indexes, item_to_indexes
    for category in categories:
        ratings_matrices[category], item_similarities[category], \
        user_to_indexes[category], item_to_indexes[category] = load_matrices(category)

categories = ['Cell_Phones_and_Accessories', 'All_Beauty', 'Amazon_Fashion', 'Appliances', 'Electronics','All']
initialize_matrices(categories)

def get_recommendations(category, target_user , n_recommendations):
    target_user_idx = user_to_indexes[category][target_user]
    user_ratings = ratings_matrices[category].getrow(target_user_idx).toarray().flatten()
    
    # Get the indices of items the user has already rated
    user_rated_item_indices = np.where(user_ratings > 0)[0]


    weighted_similarities = item_similarities[category].dot(user_ratings)
    sorted_similar_items = np.argsort(weighted_similarities)[::-1]

    # Exclude items the user has already rated
    #user_rated_items = set(df[df['user_id'] == target_user]['parent_asin'])
    
    top_recommended_items = [idx for idx in sorted_similar_items if idx not in user_rated_item_indices][:n_recommendations]

    recommended_items = []
    for item_idx in top_recommended_items:
        item_id = next(key for key, value in item_to_indexes[category].items() if value == item_idx)
        similarity_score = weighted_similarities[item_idx]
        similarity_percentage = (similarity_score - min(weighted_similarities)) / (max(weighted_similarities) - min(weighted_similarities)) * 100
        recommended_items.append({"item_id": item_id, "similarity_percentage": similarity_percentage})

    return recommended_items
