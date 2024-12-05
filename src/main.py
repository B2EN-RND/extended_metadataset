from llm_clustering import llm_clustering
from load_data import load_data
from openai import OpenAI
from feature import select_columns
from Preprocessing import preprocessing, extract_standard_metalist
from meta_table import meta_table
from matching import matching_standard
from ml_clustering iport kmeans_clustering
from visualize import tsne, heat_map
import config


def main():
    """
    프로그램의 메인 실행 로직을 작성합니다.
    """
    print("=====프로그램이 시작됩니다.=====")
    
    file_name = "aihub_industry metadata.csv"
    data = load_data(file_name)
    client = OpenAI(api_key=config['api_key'])
    # select_columns :
    # 컬럼명을 나타내는 필드 이름 (예: '컬럼명'), 설명을 나타내는 필드 이름 (예: '설명')
    feature_list = select_columns(data, "컬럼명", "설명")
    clustering_text = extract_standard_metalist(llm_clustering(client, feature_list))
    standard_meta = preprocessing(clustering_text)
    process_metadata(standard_meta)
    data_dict = matching_standard(client, feature_list)
    ml_cluster_result = kmeans_clustering(feature_list)
    tsne(feature_list) # tsne 시각화
    heat_map(feature_list) # 코사인 유사도 히트맵 시각화
    


if __name__ == "__main__":
    main()
