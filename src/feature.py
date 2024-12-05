def select_columns(data, column_name_field, description_field):
    """
    지정된 컬럼명과 설명 필드를 기반으로 데이터를 추출하는 함수

    Args:
        data (pd.DataFrame): 데이터프레임
        column_name_field (str): 컬럼명을 나타내는 필드 이름 (예: '컬럼명')
        description_field (str): 설명을 나타내는 필드 이름 (예: '설명')

    Returns:
        list: (컬럼명, 설명) 쌍으로 이루어진 리스트
    """

    feature_list = list(zip(data[column_name_field], data[description_field]))
    return feature_list
