import openai
import numpy as np
import pandas as pd
from collections import Counter
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from collections import Counter
import json
import re
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

def get_column_description(column_name, unique_values):
    """ Queries OpenAI API to interpret the meaning of the protected column. """
    prompt = f"""
    I have a dataset with a protected attribute named '{column_name}' that has the following unique values: {unique_values}.
    What's the distribution of {unique_values} in the global population. DO NOT DEFAULT TO EQUAL DISTRIBUTION AMONG ALL GROUPS!
    Provide a dictionary where keys are attribute values and values are their expected proportions (sum should be ~1). Be concise - not more than 2 lines
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']

def get_fairness_thresholds(column_name, unique_values):
    """
    Uses OpenAI API to get a predefined fairness distribution and converts it to a dictionary.
    The distribution will be directly extracted from the response between '{' and '}'.
    """
    prompt = f"""
    I have a dataset with a protected attribute named '{column_name}' that has the following unique values: {unique_values}.
    What's the latest expected distribution of {unique_values} in the total global population based on relevant and reliable sources. DO NOT DEFAULT TO EQUAL DISTRIBUTION AMONG ALL GROUPS!
    Provide a dictionary where keys are {unique_values} and values are their expected proportions (sum should be ~1). Be concise - not more than 2 lines
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    response_content = response['choices'][0]['message']['content']

    print("Response Content: ", response_content)

    try:
        start = response_content.index('{')
        end = response_content.index('}') + 1  # Include closing brace
        dict_str = response_content[start:end]
        
        thresholds = eval(dict_str)  # Convert the dictionary string into an actual Python dictionary
    except Exception as e:
        print(f"Error in extracting or evaluating the dictionary: {e}")
        thresholds = {value: 1 / len(unique_values) for value in unique_values}  # Default to uniform distribution

    print(f'\nThresholds: {thresholds}\n')
    return thresholds


def get_fairness_strategy():
    prompt = """
    Given a clustering scenario where demographic fairness is required, what is the best distribution? DO NOT DEFAULT TO EQUAL ALLOCATION AMONG ALL GROUPS!
    Be concise - not more than 2 lines
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']

def initialize_centroids(X, k, random_state=123):
    """ Randomly selects k data points as initial centroids. """
    np.random.seed(random_state)
    indices = np.random.choice(len(X), k, replace=False)
    return X[indices]
    
def assign_clusters(X, centroids):
    """ Assigns each data point to the nearest centroid. """
    distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
    return np.argmin(distances, axis=1)

def update_centroids(X, labels, k):
    """ Updates centroids as the mean of assigned data points. """
    return np.array([X[labels == i].mean(axis=0) for i in range(k)])

def compute_cluster_fairness(df, protected_col, expected_distribution):
    """ Computes fairness scores for each cluster. """
    fairness_scores = {}
    overall_count = dict(Counter(df[protected_col]))  
    overall_ratio = {k: v / sum(overall_count.values()) for k, v in overall_count.items()}

    for cluster in sorted(df['Cluster'].unique()):
        cluster_count = dict(Counter(df[df['Cluster'] == cluster][protected_col]))
        cluster_ratio = {k: cluster_count.get(k, 0) / sum(cluster_count.values()) for k in overall_ratio.keys()}

        fairness_scores[cluster] = {
            k: round(abs(cluster_ratio.get(k, 0) - expected_distribution[k]), 4)
            for k in expected_distribution
        }

    return fairness_scores

from sklearn.metrics import silhouette_score

def advanced_fairness_adjustment(df, protected_col, expected_distribution, max_iterations=100, silhouette_threshold=0.05):
    """
    Adjust the clusters for fairness while ensuring silhouette score does not drop significantly.
    This version adjusts fairness across multiple clusters, not just the most and least fair ones.
    """
    
    feature_cols = [col for col in df.columns if col != protected_col and col != 'Cluster']
    X_scaled = df[feature_cols].values
    
    initial_silhouette = silhouette_score(X_scaled, df['Cluster'])
    print(f"Initial Silhouette Score: {initial_silhouette}")

    for _ in range(max_iterations):
        fairness_scores = compute_cluster_fairness(df, protected_col, expected_distribution)

        sorted_clusters = sorted(fairness_scores.items(), key=lambda item: sum(item[1].values()), reverse=True)
        
        for cluster, scores in sorted_clusters:
            overrepresented_group = max(scores, key=scores.get)
            underrepresented_group = min(scores, key=scores.get)
            
            candidates = df[(df['Cluster'] == cluster) & (df[protected_col] == overrepresented_group)].sample(1)
            
            if not candidates.empty:
                target_cluster = next((c for c, s in sorted_clusters if underrepresented_group in s and c != cluster), None)
                
                if target_cluster:
                    df.at[candidates.index[0], 'Cluster'] = target_cluster

        new_silhouette = silhouette_score(X_scaled, df['Cluster'])
        print(f"New Silhouette Score After Adjustment: {new_silhouette}")

        if initial_silhouette - new_silhouette > silhouette_threshold:
            print("Silhouette score dropped too much, stopping further adjustments.")
            break

    return df

from sklearn.metrics import silhouette_score

def fair_kmeans(data, n_clusters, protected_col, max_iterations=100, random_state=123):
    """
    Custom k-means clustering with AI-defined fairness constraints and an AI-suggested fairness strategy.
    """
    
    feature_cols = [col for col in data.columns if col != protected_col and col != 'Cluster']
    X = data[feature_cols].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    unique_values = data[protected_col].unique().tolist()

    print(f"Querying OpenAI API for fairness distribution of {unique_values}...")
    expected_distribution = get_fairness_thresholds(protected_col, unique_values)  # Assuming this function returns a dict of expected proportions
    print(f"AI-Recommended Fairness Distribution: {expected_distribution}")

    
    centroids = initialize_centroids(X_scaled, n_clusters, random_state)
    
    for _ in range(100):  
        labels = assign_clusters(X_scaled, centroids)
        new_centroids = update_centroids(X_scaled, labels, n_clusters)

        if np.all(centroids == new_centroids):
            break  # Stop if centroids don't change

        centroids = new_centroids

    data['Cluster'] = labels  # Assign final clusters

    initial_silhouette = silhouette_score(X_scaled, labels)
    print(f"Initial Silhouette Score: {initial_silhouette}")
    
    fairness_before = compute_cluster_fairness(data, protected_col, expected_distribution)

    data = advanced_fairness_adjustment(data, protected_col, expected_distribution, max_iterations, silhouette_threshold=0.05)

    fairness_after = compute_cluster_fairness(data, protected_col, expected_distribution)
    
    new_silhouette = silhouette_score(X_scaled, data['Cluster'])
    print(f"Silhouette Score After Adjustment: {new_silhouette}")

    return data, {'before': fairness_before, 'after': fairness_after, 'initial_silhouette': initial_silhouette, 'new_silhouette': new_silhouette}
