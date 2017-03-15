#check if a user can only see one stash project at a given URL

import stashy

#URL and account variables

url = "put your URL here"
userName = "put your user here"
userPassword = "put your user password here"

#Connection string
stash = stashy.connect(url, userName, userPassword)

#Iterate over all projects (that you have access to)
projects = stash.projects.list()

#Retrieve all users if needed for check all users in the future
#users = stash.admin.users.list()

#String variable to append messages and print out
strOut = ""

if(len(projects) == 0):
 strOut +=("Warn: No projects are visible for user " + userName)    
elif (len(projects) == 1):
    strOut +=("Info: 1 project is visible for user " + userName + " in project " +  projects[0]["name"])
else:
    stringMessage = ("Error: more than one project is visible for user: " + userName)
    strOut +=stringMessage + "<br/>"
    for project in projects:
        strOut += project["name"] + "<br/>"
print(strOut)
