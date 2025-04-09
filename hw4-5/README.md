# Assignment 4-5: intro to git

## Exercise 1: setup

- Install Git on your local machine, if you haven't already.
- Configure your Git username and email using the following commands:
```
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

## Exercise 2: first commit

In this exercise you will work in a git repository.

- Create a new repository in your github
- Make sure to make it public, so that mentor could see it and check it.
- Navigate to the repository directory.
- Create a new text file named `file1.txt` in the directory.
- Stage `file1.txt` using `git add`.
- Commit the changes with a message "add: file1.txt" using `git commit`.
- Push the changes using `git push`

## Exercise 3: branches

- Create a new branch named `feature` and switch to it using `git switch`.
- Add a new file named `file2.txt` in the directory.
- Stage `file2.txt` and commit the changes with a message "add: file2.txt".
- Push the changes using `git push`

## Exercise 4: merge

- Switch back to the `main` branch using `git switch`.
- Merge the `feature` branch into the `main` branch using `git merge`.
- Push the changes using `git push`

## Exercise 5: bugfix

- Create a new branch named `bugfix` and switch to it.
- Modify `file1.txt` by adding a new line of text.
- Stage the changes and commit with a message "fix: bug in file1.txt".
- Switch back to the `main` branch and merge the `bugfix` branch.
- Check the Git log to see the commit history using `git log`.
- Push the changes using `git push`

## Exercise 6: gitignore

- Create a `.gitignore` file in the repository and add a rule to ignore all files with the `.log` extension.
- Stage the changes and commit with a message "add: gitignore".
- Push the changes using `git push`

⚠️ For this assignment you need to send a GitHub link to your repository.