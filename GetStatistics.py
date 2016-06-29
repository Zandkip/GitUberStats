import subprocess

def GetLog():
    print("Getting logs for Git archive")
    return subprocess.Popen(["git", "log", "--all"], stdout=subprocess.PIPE).communicate()[0]

if __name__ == '__main__':
    log = GetLog()
    print("Done!")