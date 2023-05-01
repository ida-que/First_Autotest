## GIT - homework 1 - GIT_init publishing with git init
This is a part of GIT homework 1. To see all the GIT homeworks, click [here](https://github.com/ida-que/GIT-homeworks).</br>
_Note: To work with GIT repos, I used some of these necessary tools:_
- _a GitHub account_
- _GitBash (for Windows) to write commands_
- _Git installed to operate Git repos_
- _folders for keeping local repos (I used `mkdir` Bash command to create those in terminal)_

## STEPS
#### 1. Create a local repository _GIT_init_.
To make a local repo, I just use `git init` command while being in the directory where I have one file - my first autotest.
```
$ git init
Initialized empty Git repository in D:/career/My courses/QA/GIT/First_Autotest/.git/
```
Now, we have add the file to make an initial (root) commit on _(master)_ branch. I didn't want to add readme yet, but I already have a file with autotest to upload:
```
$ git add .
```
Initial commit:
```
$ git commit -m "initial commit"
[master (root-commit) afcc9f0] initial commit
 1 file changed, 41 insertions(+)
 create mode 100644 Capitalcom_glossary_imgsrc.py
```
But what about branches? We have to create a `main` branch:
```
$ git branch -M main
```
And then we are automatically checked out at the `main` branch.
#### 2. Create a remote repository _First_Autotest_ at GitHub.
To make this step, I go to my GitHub account, then go to the _"Repositories"_ tab and click on _"New"_ button.</br>
After this, I needed an HTML link to this remote repo to connect it with my local repo in the very next step.
#### 3. Connect and synchronize these local and remote repositories.
To connect to the remote repo, I have a link to it. I can come back to terminal with a previously prepared initial commit.
```
$ git remote add origin https://github.com/ida-que/First_Autotest.git
```
The last thing is pushing that commit we created:
```
$ git push -u origin main

Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 761 bytes | 761.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/ida-que/First_Autotest.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.

```