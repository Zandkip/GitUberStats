import copy

class GitCommit:
    hash = ""
    date = ""
    message = ""

    def __init__(self, commit):
        self.hash = commit[0].replace('commit', '')
        self.hash = self.hash.strip()
        self.date  = commit[1].replace('Date:', '')
        self.date = self.date.strip()
        self.message = commit[2]
        self.message = self.message.strip()