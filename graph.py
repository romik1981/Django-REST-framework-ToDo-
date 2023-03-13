import requests

url = "http://127.0.0.1:8000/graphql/"

body = """
{
  allTodos{
    id
    text
    project {
      name
    }
    isActive
    creator {
      username
    }
  }
}
"""


response = requests.post(url, json={"query": body})

print(response.text)
