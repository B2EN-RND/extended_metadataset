import pandas as pd

def process_metadata(data):
    """
    메타 데이터를 카테고리와 표준/확장 기준으로 분류하고 데이터프레임으로 반환하는 함수.

    Args:
        data (list of tuple): (메타항목, 메타정의) 형태의 리스트.

    Returns:
        pd.DataFrame: 분류 결과를 포함한 데이터프레임.
    """
    result = []
    
    for meta_item, meta_definition in data:
        # 카테고리와 표준/확장 기준 분류
        if "라벨" in meta_definition or "클래스" in meta_definition:
            category = "데이터 분석 지원"
            standard = "표준"
        elif "이미지" in meta_definition or "바운딩박스" in meta_definition or "위치" in meta_definition or "포인트" in meta_definition:
            category = "데이터 수집"
            standard = "표준"
        elif "센서" in meta_definition or "로봇" in meta_definition or "장비" in meta_definition:
            category = "데이터 연관 관계 강화"
            standard = "확장"
        elif "기타" in meta_definition or "일반" in meta_definition:
            category = "기타 정보"
            standard = "확장"
        else:
            category = "기타 정보"
            standard = "확장"
        
        # 메타항목 이름 수정 (예: 경로_정보 -> 경로 정보)
        updated_meta_item = meta_item.replace("_", " ")
        
        # 결과 추가
        result.append((category, updated_meta_item, standard, meta_definition))
    
    # 데이터프레임 생성 및 반환
        pd.DataFrame(result, columns=["카테고리", "메타항목", "표준/확장", "메타정의"]).to_csv("standard_metatable.csv")
