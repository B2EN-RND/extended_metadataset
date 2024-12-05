import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
 import seaborn as sns
    
def tsne(tuple_list)
    texts = [f"{desc}" for col, desc in tuple_list]
    # 1. 텍스트 임베딩 (TF-IDF)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    tsne = TSNE(n_components=2, random_state=42, perplexity=5, n_iter=1000)
    X_2d = tsne.fit_transform(X.toarray())

    # 2. 시각화
    plt.figure(figsize=(12, 8))
    for cluster_id in range(num_clusters):
        cluster_points = X_2d[kmeans.labels_ == cluster_id]  # 클러스터에 속한 포인트
        plt.scatter(
            cluster_points[:, 0],
            cluster_points[:, 1],
            label=f"클러스터 {cluster_id}"
        )

    # 3. 데이터 포인트에 설명 텍스트 추가
    for i, (x, y) in enumerate(X_2d):
        plt.text(x, y, result["설명"][i], fontsize=9, alpha=0.75)

    # 4. 그래프 꾸미기
    plt.title("K-Means 군집화 결과 시각화 (t-SNE)", fontsize=14)
    plt.xlabel("축소된 차원 1", fontsize=12)
    plt.ylabel("축소된 차원 2", fontsize=12)
    plt.grid()
    plt.show()
    
def heat_map(tuple_list):
    # 1. 텍스트 전처리 (컬럼명 + 설명 결합)
    texts = [f"{col} {desc}" for col, desc in tuple_list]

    # 2. 텍스트 임베딩 (TF-IDF)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    # 3. 코사인 유사도 계산 (참고용)
    cos_sim_matrix = cosine_similarity(X)
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        cos_sim_df, 
        annot=True, 
        cmap="Blues", 
        xticklabels=cos_sim_df.columns, 
        yticklabels=cos_sim_df.index
    )
    plt.title("코사인 유사도 히트맵")
    plt.show()

