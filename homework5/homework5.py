#homework 1+2 review 
# vocab review 
"""
1. Git vs. GitHub
    git is the tool that lets you commit etc, while github is the platform for the repository 
2. Terminal vs. Command Line
    terminal is the program in mac, and the command line is where you actually type the commands 
3. Local vs. Remote Repository
    local is on the computer and remote is like on the github website 
4. Version Control
    traching the changes of the code 
5. Staging Area
    the pre area where things are kind of in between, before you send them to the remote repository 
6. git add
    takes from the working directory to the staging area 
7. git commit
    moves from the staging area to the local repository 
8. git push
    from local repo to the remote repo 
9. git status
    tells you what is going on / where you are 
10. git pull
    takes things from the remote repo and pulls them into the working directory 
11. pwd
    present directory 
12. ls
    shows the contents of the directory you are in 
13. cd
    change directory 
14. nano
    create a new file 
15. touch
    create a new empty file 
16. mv
    move
17. rm
    remove 
18. cat
    cancatinate files 
"""
# 3.2 --- a directory tree ---
"""
1. pwd 
2. ls
3. git pull origin brianna_repo, git pull, 
4. git clone homework.py, cd homework, git add . , git commit -m "move files" , git push origin brianna_repo
5. cd homework
6. ls 
7. git push 
8. git pull origin main, git add ., git commit, git push origin main
9. ~/Recent/
"""
# --- draw directory tree ---

# homework 4 review 
# --- data types ---
def checkDataType(input): 
    return type(input)

# --- cnoditionals ---
def evenOrOdd(num):
    if num % 2 ==0: 
        return "Even"
    else:
        return "Odd"
    
# --- loops ---
def sumWithLoop(lst): 
    total = 0 
    for num in lst: 
        total += num 
    return total

# homework 6 review 
# --- lists ---
def duplicateList(lst): 
    repeated_list = []
    for num in lst: 
        repeated_list.append(num)
        repeated_list.append(num)
    return repeated_list

numssss = [1,2,3]
print(duplicateList(numssss))

# --- debugging --- 
def square(num): #the original code was missing a colon 
    return num * num 

