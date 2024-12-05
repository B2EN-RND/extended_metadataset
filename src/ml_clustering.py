from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import pandas as pd

def kmeans_clustering(tuple_list):
    # 1. 텍스트 전처리 (컬럼명 + 설명 결합)
    texts = [f"{col} {desc}" for col, desc in tuple_list]

    # 2. 텍스트 임베딩 (TF-IDF)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    # 3. 코사인 유사도 계산 (참고용)
    cos_sim_matrix = cosine_similarity(X)
    cos_sim_df = pd.DataFrame(cos_sim_matrix, columns=[col for col, _ in tuple_list], index=[col for col, _ in tuple_list])
    print("코사인 유사도 행렬:")
    print(cos_sim_df)

    # 4. K-Means Clustering
    num_clusters = 28  # 클러스터 개수
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X)

    # 5. 결과 정리
    clusters = kmeans.labels_
    result = pd.DataFrame({"컬럼명": [col for col, _ in tuple_list], "설명": [desc for _, desc in tuple_list], "클러스터": clusters})
    print("\n군집화 결과:")
    print(result)

    # 6. 클러스터별 데이터 그룹화
    grouped = result.groupby("클러스터")
    for cluster_id, group in grouped:
        print(f"\n클러스터 {cluster_id}:")
        print(group)
        
    return result
