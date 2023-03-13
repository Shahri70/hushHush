import threading
from github import Github
import urllib.request
import re
# define a function that will fetch data for a given user
def fetch_data(username):
    ACCESS_TOKEN ="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"
    g = Github(ACCESS_TOKEN)
    user=None
    if type(username)==list:
        for userlist in username:
            query = f"fullname:{userlist}"
            users = g.search_users(query=query)
            for userone in users:
                if userone.name.lower()==userlist.lower():
                    user = g.get_user(user.login)
                    break
    else:
        query = f"fullname:{username}"
        users = g.search_users(query=query)
        for userone in users:
            if userone.name.lower()==username.lower():
                user = g.get_user(userone.login)
                break
    # get the user object
    if user!=None:
        personal_info = {
            "name": user.name,
            "bio": user.bio,
            "location": user.location,
            "email": user.email,
            "company": user.company,
            "hireable": user.hireable,
            "created_at": user.created_at,
            "updated_at": user.updated_at,
            "html_url": user.html_url,
            "public_repos": user.public_repos,
            "public_gists": user.public_gists,
            "followers": user.followers,
            "following": user.following
        }
        
        # get the user's email
        hash_number=None
        repos = user.get_repos()
        emails=None
        for repo in repos:
            repos_info={
                "name": repo.name,
                "fork": repo.fork,
                "commits_url":repo.commits_url
            }
            if repos_info["fork"]==False:
                repo = user.get_repo(repos_info["name"])
                commits = repo.get_commits()
                try:
                    for commit in commits:
                        hash_number=commit.sha
                        if hash_number!=None:
                            break
                except:
                    None
            if hash_number!=None:
                break
        if hash_number!=None:
            repos_info["commits_url"]=repos_info["commits_url"].split("commits{/sha}")[0]
            repos_info["commits_url"]+="commit/"+hash_number
            repos_info["commits_url"]+=".patch"
            repos_info["commits_url"]=repos_info["commits_url"].split("https://api.")[1]
            repos_info["commits_url"]="https://"+repos_info["commits_url"]
            repos_info["commits_url"]=repos_info["commits_url"].split("/repos")[1]
            repos_info["commits_url"]="https://github.com"+repos_info["commits_url"]
            #print(repos_info["commits_url"])
            try:
                response = urllib.request.urlopen(repos_info["commits_url"])
                content = response.read().decode()
                email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
                emails = re.findall(email_pattern, content)
            except:
                None
            personal_info["email"]=emails
    try:
        return personal_info
    except:
        None
# create a list of threads
def check_availabality(usernames):
    threads = []
    results = []
    # create a new thread for each username and start it
    for username in usernames:
        thread = threading.Thread(target=lambda: results.append(fetch_data(username)))
        thread.start()
        threads.append(thread)

    # wait for all threads to finish
    for thread in threads:
        thread.join()
    results = list(filter(lambda x: x is not None, results))
    return results

