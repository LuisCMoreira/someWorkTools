git add .
set /p commitMSG=Please enter commit description:
git commit -m "%commitMSG%"
set /p repo=Please enter repository:
git push origin %repo%