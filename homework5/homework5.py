#Git vs GitHub
"""
Git is the language used in the terminal to implement version control and track changes in code over 
time. It works locally on the terminal. Github is a website that is able to host online repositories
and is avaliable remotely on the internet. 
"""
#terminal vs commandline 
"""
The terminal is the interface on locally on the computer that interacts with the system via commands
and there's a window where you can see the output. The commandline is how the interaction happens 
or the method where commands like pwd, cd, or ls is written on inside the terminal.
"""
#Local vs Remote Repository 
"""
A repository simplified is a directory with version control abilities. A local repository is one 
stored in whatever interface you are using such as your laptop/computer. Git commands are used on 
the computer/laptop so its saved locally. A remote repository is one that is on the internet such 
as Github that hosts multiple online repositories. Changes can be uploaded from local to remote via
git push and updates can be downloaded using git pull.
"""

#Version Control 
"""
Version control is a system that tracks and manages changes to files over time so you can view, 
restore, and collaborate on different versions of a project.
"""

#Staging Area 
"""
The staging area is achieved by using the git add command and its the rough draft zone place to
make last minute changes. 
"""

#Git Add
"""
Git add saves all files (git add .) or a specific file (git add <specific file> ) 
and adds it to the staging area. 
"""

#Git Commit 
"""
Git commit fully commits the work to saving it in the local repository or the computer 
using the command git commit -m "message". 
"""

#Git Push
"""
Git push updates and pushes the work from the local repository (computer) to the remote repository
on github using the command git push -u origin main. 
"""

#Git Status
"""
Git status is a command to call to learn more about the issues the local repository is facing such 
as if there are more files to be saved or if there are changes in the remote repository. 
"""

#Git Pull
"""
Git pull updates the local repository by using the information in the remotre repository. 
The command is git pull origin main to pull into local repository. 
"""

#Pwd
"""
Pwd means print the current working directory and the file path is also printed ad well as the 
root directory such as /Users/. 
"""

#ls
"""
Ls means list the contents of the folder except the hidden ones. 
"""

#cd
"""
Cd is change directories and changes the folder you are currently in.
"""

#nano 
"""
nano is a way to edit your file on the command line. 
"""

#touch
"""
touch is a way to make a new file on the terminal
"""

#mkdir 
"""
make a new folder on the terminal (make directory)
"""

#mv
"""
mv can be used to rename a file or move a file from one directory to another 
"""

#rm
"""
rm permenantley deltes files and directories 
"""

#cat
"""
prints all the content of a file that you use the command on 
"""

#In Judy's directory system, the command pwd would tell you the current working directory. 

#I would use ls to list all the files in your current working directory. 

"""You would need to move cd ../brianna_repo, moving to python_decal then brianna_repo, and then
use git pull to download the latest changes from the remote repository.
"""
#I would use mv brianna_repo/homework.py judy_decal/homework/. 

#To move mysekf from brianna_repo to judy_decal using cd../judy_decal 

#To see the contents of homework.py in terminal i would use nano to see and edit on the terminal. 

"""
First I would use git status and see what needs to be added. I would then use git add . that adds 
and saves all to the staging area. After i would use git status to see that everything is moved 
to the staging area. Then, I would call git commit -m "done with homework.py" and commit to save
work on local repository. Then I would call git status see that there's nothing more to commit 
and then I would push to the remote repository using git push -u origin main. 
"""

"""
This error means that the remote repository has changes that the local repository doesn't have, so
she can't push. She would need to pull from the remote to the local using git pull origin main and
then push again using push origin main. Someone else probably made changes to the remote repository 
so her current version was behind
"""

#The absolute path would be cd /Recents. 

#4.1 Data Types

def checkDataType(input): 
    variable = type(input)
    return variable 


def evenOrOdd(number):
    if number % 2 == 0: 
        print("Even")
    else:
        print("Odd")


numbers =  [1,2,3,4,5]
def sumWithLoop(numbers):
    total = 0
    for number in numbers: 
        total+= number
    return total 


my_list = ["a","b","c"]
def duplicateList(my_list): 
    new_list = []
    for letter in my_list:
        new_list.append(letter)
        new_list.append(letter)
    return new_list


def square(num):
    return num * num 


#my favorite code 
def evenOrOdd(number):
    if number % 2 == 0: 
        print("Even")
    else:
        print("Odd")
    return number 
