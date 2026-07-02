import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def main():
    print("====================================================")
    print("      DecodeLabs Tech Stack Recommender Initialized  ")
    print("====================================================\n")

    # Verify dataset exists
    csv_path = "raw_skills.csv"
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found. Please create your dataset first.")
        return

    # Load job roles dataset (Items)
    df = pd.read_csv(csv_path)
    
    # --- PIPELINE STEP 1: INGESTION ---
    # Accepting a minimum of 3 user inputs to ensure sufficient density
    print("Step 1: Ingesting user profile states...")
    user_skills = []
    for i in range(1, 4):
        skill = input(f"Enter your technical skill or career interest #{i}: ").strip()
        user_skills.append(skill)
    
    # Combine inputs into a single profile query text space
    user_query = " ".join(user_skills)
    print(f"\nCreated User Profile String: '{user_query}'\n")

    # --- PIPELINE STEP 2: SCORING (TF-IDF & Cosine Similarity) ---
    print("Step 2: Vectorizing text space and calculating similarity scores...")
    
    # Initialize TF-IDF Vectorizer to automatically handle frequency weighting
    # We fit on item metadata combined with our query to align the vocabulary
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the job role skills
    tfidf_matrix = vectorizer.fit_transform(df['Skills'])
    
    # Transform the user profile query into the exact same vector space dimension
    user_vector = vectorizer.transform([user_query])
    
    # Run the similarity math across all rows in the dataset matrix
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()

    # Add scores into our structural framework dataframe
    df['Similarity_Score'] = similarity_scores

    # --- PIPELINE STEP 3: SORTING ---
    print("Step 3: Organizing scored vectors in descending order...")
    sorted_df = df.sort_values(by='Similarity_Score', ascending=False)

    # --- PIPELINE STEP 4: FILTERING (TOP-N LIST) ---
    print("Step 4: Filtering out noise to avoid Choice Overload...\n")
    print("====================================================")
    print("         TOP 3 RECOMMENDED CAREER PATHS             ")
    print("====================================================")
    
    # Truncate to extract the Top 3 items
    top_n = sorted_df.head(3)
    
    for idx, row in top_n.iterrows():
        match_percentage = row['Similarity_Score'] * 100
        print(f"🏆 Rank Match: {row['Role']}")
        print(f"   📊 Alignment Score: {match_percentage:.2f}%")
        print(f"   🛠️ Expected Stack: {row['Skills']}\n")
    print("====================================================")

if __name__ == "__main__":
    main()