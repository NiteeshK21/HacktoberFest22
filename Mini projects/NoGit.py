import subprocess

class GithubAutomate:

    def run(self, cmd):
        completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        print(completed)
        print(completed.stdout.decode('utf-8'))
        return completed

    def git_init(self):
        self.run("git init")
    
    def cd(self,path):
        self.run("cd {}".format(path))


if __name__ == '__main__':

    obj = GithubAutomate()

    PATH = "<write your folder's path>"
    # e.g.: PATH = r"C:\Users\HELLO\OneDrive\Desktop\coding\Python\HackSquad"
    REPO_PATH = "write you Repo's path in https format"
    # e.g.: REPO_PATH = r"https://github.com/just-injoey/DemoRepo.git"

    initial_cmds = ['cd {PATH}',
    'git init',
    'git remote add origin {REPO_PATH}',
    'git add .',
    'git commit -s -m "Initial commit',
    'git push origin main'
    ]
    
    commands=['cd {PATH}',
    'git add .',
    'git commit -s -m "Commit message"',
    'git push origin main'
    ]

    # obj.run("{0};{1};{2};{3};{4};{5}".format(initial_cmds[0],initial_cmds[1],initial_cmds[2],initial_cmds[3],initial_cmds[4],initial_cmds[5]))

    obj.run("{0};{1};{2};{3};{4};{5}".format(initial_cmds[0],initial_cmds[1],initial_cmds[2],commands[0],commands[1],commands[2]))

