#!/usr/bin/env python3

from contributor_ci.utils import read_json, write_json
import os

here = os.path.abspath(os.path.dirname(__file__))
root = os.path.dirname(here)
outfile = os.path.join(root, "assets", "repos.json")

repos = read_json(os.path.join(root, "cci", "data", "latest", "cci-repos.json"))
topics = read_json(os.path.join(root, "cci", "data", "latest", "cci-topics.json"))

# Assemble data first as dict
data = {}

for reponame, repo in repos.items():
    repo_topics = topics.get(reponame) or []
    if repo_topics:
        names = [x["topic"]["name"] for x in repo_topics["repositoryTopics"]["nodes"]]
        names.sort()
        repo_topics = names

    data[reponame] = {
        "github_url": "https://github.com/" + repo["nameWithOwner"],
        "url": repo["homepageUrl"],
        "description": repo["description"],
        "issues-open": repo["issues_Open"]["totalCount"],
        "issues-closed": repo["issues_Closed"]["totalCount"],
        "stars": repo["stargazers"]["totalCount"],
        "forks": repo["forks"]["totalCount"],
        "language": repo["primaryLanguage"]["name"],
        "topics": repo_topics,
    }

write_json(list(data.values()), outfile)
