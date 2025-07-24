git checkout main
git pull origin main

set /p branch=Please enter branch name to merge to "MAIN":
git merge feature-branch

# WARNING: Resolve any conflicts if necessary

git add .
set /p mergeMSG=Please enter merge commit message:
git commit -m %mergeMSG%
git push origin main