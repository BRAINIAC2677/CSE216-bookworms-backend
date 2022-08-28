import requests 

list_endpoint = 'http://127.0.0.1:8000/api/book/list/'

list_query_data = {
    'bid': 1,
    'title': 'title',
    'gte_page_count': 0,
    'lte_page_count': 0,
    'genre_id': 0,
    'author_id': 0,
}

list_response = requests.get(list_endpoint, params=list_query_data)
print(list_response.json)
