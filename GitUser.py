class GitUser:
    name = ""
    commits = []

    def __init__(self, name):
        self.name = name

    def AddCommit(self, commit):
        self.commits.append(commit)

