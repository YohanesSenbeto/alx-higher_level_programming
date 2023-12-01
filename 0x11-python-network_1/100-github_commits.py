#!/usr/bin/python3
"""
This script is fetches the 10 most recent commits of the specified repository by the given user using the GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    # Get repository and owner names from command line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Build the URL for the GitHub API request
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    # Send GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the JSON response and extract the first 10 commits
        commits = response.json()[:10]
    else:
        commits = []

    # Print the SHA and author name of each commit
    for commit in commits:
        sha = commit.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print(f"{sha}: {author_name}")
