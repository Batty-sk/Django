import requests
import json
data={}
def Api(query):
    for q in query:
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(q)
        api_key='RS7HAJlDyWVOHFROyklHGw==emYfKBZYVXNwuntW'
        response = requests.get(api_url, headers={'X-Api-Key': api_key})
        if response.status_code != requests.codes.ok:
            print("Error:", response.status_code, response.text)
        else:
            data[q]=json.loads(response.text)
    print(data);
    return data;