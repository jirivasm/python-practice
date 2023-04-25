import requests

response =requests.get("https://api.github.com/users/jirivasm/repos")
print(response)
my_projects = response.json()

for project in my_projects:
    print(f"Project name: {project['name']}")
    print(f"Project URL: {project['html_url']}\n")
    
    