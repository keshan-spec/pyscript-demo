from js import document, Element
import requests
import pyodide_http
pyodide_http.patch_all()

def get_public_repos():
    username = document.getElementById("username").value
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        repo_element = document.getElementById("manual-write")#

        html = ""
        for repo in repos:
            repo_name = repo["name"]
            repo_url = repo["html_url"]
            html += f"""<a href="{repo_url}">{repo_name}</a><br>"""

        repo_element.innerHTML = html
    else:
        return None