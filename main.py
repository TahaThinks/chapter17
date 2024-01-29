import requests

#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {"Accept":"application/vnd.github.v3+json"}
r = requests.get(url,headers=headers)
print(f"Status code: {r.status_code}")

#Store API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

#Explore information about the repositories
repo_dicts = response_dict['items']
print(f"repositories returned: {len(repo_dicts)}")

#Examine the first repository
repo_dict = repo_dicts[0]
print("\n Selected information about the first repository")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")