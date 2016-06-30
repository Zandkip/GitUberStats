import subprocess
import copy
from GitUser import GitUser

def GetLog():
    print("Getting logs for Git archive")
    return subprocess.Popen(["git", "log", "--all"], stdout=subprocess.PIPE).communicate()[0]

def ParseLog(log):
    print("Parsing Git log")
    commits = GetCommitsFromLog(log)
    print("Found " + str(len(commits)) + " commits")
    users = ExtractUsersFromCommits(commits)
    print("Found " + str(len(users)) + " user(s)")

def GetCommitsFromLog(log):
    lines = log.splitlines()
    trimmedLines = filter(bool, lines)
    index = 0
    commits = []
    singleCommit = []
    for line in trimmedLines:
        stringLine = line.decode("utf-8")
        if stringLine.startswith("commit"):
            if singleCommit:
                newCommit = copy.deepcopy(singleCommit)
                commits.append(newCommit)
            singleCommit.clear()
        singleCommit.append(stringLine)
    return commits

def ExtractUsersFromCommits(commits):
    print("Extracting users from commits")
    users = []
    for commit in commits:
        if commit[1].startswith("Author: "):
            userName = commit[1][8:]
            if not UserExists(users, userName):
                user = GitUser(userName)
                users.append(user)
            GetUserByName(users, userName).AddCommit(commit)
    return users

def UserExists(users, userName):
    for i, j in enumerate(users):
        if j.name == userName:
            return True
    return False

def GetUserByName(users, userName):
    for i, j in enumerate(users):
        if j.name == userName:
            return j
    return 0

if __name__ == '__main__':
    log = GetLog()
    statistics = ParseLog(log)
    print("Done!")