import ast
import re

def extract_standard_metalist(text):
    result = re.search(r'\(.*\)', text, re.DOTALL)

    if result:
        return extracted_text = result.group()
    else:
        return None
        
def preprocessing(text):
    text = text.replace("\n", "").replace(" ","")
    try:
        result = ast.literal_eval(text)
        return result
    except e:
        print(e, "추출된 문자열이 없습니다.")
        return None