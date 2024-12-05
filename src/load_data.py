import pandas as pd

def load_data(file):
    #데이터를 불러오는 코드, df로 return.
    data = pd.read_csv(file)
    print(f"======{data.shape[0]}건의 {file}를 불러옵니다.======")
    
    return data