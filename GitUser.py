import copy

class GitUser:
    name = ""
    commits = []

    def __init__(self, name):
        self.name = name

    def AddCommit(self, commit):
        trimmedCommit = copy.copy(commit)
        del trimmedCommit[1]
        self.commits.append(trimmedCommit)

