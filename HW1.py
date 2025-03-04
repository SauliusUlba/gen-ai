import requests

url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url)

if response.status_code == 200:
    todos = response.json()
    
    for todo in todos[:10]:
        print(f"ID: {todo['id']}")
        print(f"User ID: {todo['userId']}")
        print(f"Title: {todo['title']}")
        print(f"Completed: {todo['completed']}")
        print("-" * 40)
else:
    print("Failed to fetch data")