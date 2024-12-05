from openai import OpenAI

def llm_clustering(client, tuple_list):
    completion = client.chat.completions.create(
        model='gpt-4o',
        seed=2024,
        messages=[
            {
                "role": "system", 
                "content": """
                    You will group and classify column names with similar features in the entire column name. You should follow the rules below
                    
                    1. The data consists of [( 'column name', 'explanation',...]]
                    2. The number of standardized column names shall be between 20 and 30
                    3. Create other columns and include non-collected column names in others
                    4. Results in the list type of standardized column names [(Standardized column name 1', 'column description'), ('Standardized column name 2', 'column description'),...]
                    5. Make it a Korean column name
                """
            },
            {
                "role": "user", 
                "content": f"""
                주어진 데이터를 이용하여 표준화된 컬럼명으로 군집화하고, 부가 설명없이 결과만 얘기해줘 
                - 데이터: '{tuple_list}'
                """
            }
        ]
    )
    return completion.choices[0].message.content