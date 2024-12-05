from openai import OpenAI

def matching_llm(client, list_data, new_data):
    
    completion = client.chat.completions.create(
        model='gpt-4o',
        seed=2024,
        messages=[
            {
                "role": "system", 
                "content": """
                    You have to match the new column name with the standardized column name

                    1. The new column name consists of ('column name', 'explanation').
                    2. The standardized column name list consists of ("standardized column name", "column description").
                    3. Look at the column name and description to identify the characteristics and match them to the standardized column name.
                    4. If it doesn't match the standardized column name properly, match it to the 'other' column name
                    5. Results in the tuple type of ("standardized column name", "new column name")
                """
            },
            {
                "role": "user", 
                "content": f"""
                새로운 데이터를 표준화된 컬럼명리스트중 하나에 매칭시키고, 부가 설명없이 결과만 얘기해줘 
                - 표준화된 컬럼명리스트 : '{list_data}'

                
                - 새로운 데이터: '{new_data}'
                """
            }
        ]
    )
    return completion.choices[0].message.content

def matching_standard(client, tuple_list):
    data_dict = {key: [] for key, _ in list_data}
    for i in range(len(tuple_list)):
        new_data = tuple_list[i]
        try:
            result_match = matching(client, list_data, new_data)
            result_match = ast.literal_eval(result_match)
            if result_match[0] in data_dict:
                return data_dict[result_match[0]].append(result_match[1])
        except:
            print("오류 : ", result_match) 