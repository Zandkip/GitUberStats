import copy
from GitCommit import GitCommit

class GitUser:
    name = ""
    commits = []

    def __init__(self, name):
        self.name = name

    def AddCommit(self, commit):
        del commit[1]
        newCommit = GitCommit(commit)
        self.commits.append(newCommit)

