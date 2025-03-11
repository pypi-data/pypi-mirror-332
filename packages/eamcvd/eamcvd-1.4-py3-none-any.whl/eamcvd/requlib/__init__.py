import requests

ver = 1.0

BASE_URL = "https://axiom-mc.org/eamcvd/wp-json/wp/v2/posts"

def getByName(name):
    params = {
        "search": name,
        "per_page": 5
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        posts = response.json()
        if posts:
            return [{
                'title': post['title']['rendered'],
                'content': post['content']['rendered']
            } for post in posts]
        return "No blogs found with that name."
    return f"Error: {response.status_code}"

def getByID(id):
    params = {
        "search": 'eai-' + id,
        "per_page": 5
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        posts = response.json()
        if posts:
            return [{
                'title': post['title']['rendered'],
                'content': post['content']['rendered']
            } for post in posts]
        return "No blogs found with that ID."
    return f"Error: {response.status_code}"
    return f"Error: {response.status_code}"