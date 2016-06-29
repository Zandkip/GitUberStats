import subprocess

def GetLog():
    print("Getting logs for Git archive")
    return subprocess.Popen(["git", "log", "--all"], stdout=subprocess.PIPE).communicate()[0]

def ParseLog(log):
    print("Parsing Git log")
    commits = GetCommitsFromLog(log)
    print("Found " + str(len(commits)) + " commits")

def GetCommitsFromLog(log):
    lines = log.splitlines()
    trimmedLines = filter(bool, lines)
    index = 0
    commits = []
    singleCommit = []
    for line in trimmedLines:
        stringLine = line.decode("utf-8")
        if stringLine.startswith("commit"):
            if singleCommit.count != 0:
                commits.append(singleCommit)
            singleCommit.clear()
        singleCommit.append(stringLine)
    return commits

if __name__ == '__main__':
    log = GetLog()
    statistics = ParseLog(log)
    print("Done!")