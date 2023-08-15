# Project Repo README

## Questions

1. Where do I put Agile in the technology overview section? with emphasis on how Agile methodology shaped the application over time 

We discovered (after a looooong process ) that if you have jenkins installed in windows and you run into an error saying that your 'SQLALCHEMY_DATABASE_URI' isn't set
you have to include the 'set DATABASE_URI=mysql+pymysql://etc' as the first command in the Jenkins build step

## Contents

1. Overview of technologies used: Readme file is very well detailed and structured. App adheres to agreed standards (app structure, technologies, etc.) -> At the top say how im going to use the techonologies and list them as an overview.

2. How I organised Sprints: utilisation of Sprints, There is time for two 2-day Sprints before the site is scheduled to "go live". take 10 minutes in each morning to plan out your day. you should be planning your actual work time in easy to manage chunks, database then html etc. just describe how you've broke it down. required to track your designs and workflow throughout the duration of the project, with emphasis on how Agile methodology shaped the application over time write down sprints where i plan what to do each time. prioritised the mvp so worked on those first, then scheduled time slots for extra features 

3. How I used my Kanban board: make 7 user stories for the entire project and add screenshots (key features only i.e. home page, log in button etc.). 
Put a task breakdown inside each of your user stories to keep it well-structured. 
Include some acceptance criteria screenshots (in description of user stories). 
Add in risk assessment screenshot from excel and summarise it [https://qa-community.co.uk/~/_/learning/agile/agile--risk-assessments] ("a record of any issues or risks encountered during project creation, Based on results, changes were made to the solution and discussed at a good level"). Also in this space, Showcased evolution of ideas from base design to final designs -> refactoring code because you wanted it to do something else so take screenshot before and after i encourntered soem errors where i was able to improve and refactor my code.
Finally, show some screenshots of entire Kanban board how it looked at the beginning vs. middle vs. end. 

4. How I used Feature-Branch Model: have 2 feature branches 1 for html and one for back end. screenshot the network graph on the github repo in the insights section.

5. ERD Diagram: screenshot and give 1 sentence to explain "this is the tables i have and how they relate to each other"

6. Jenkins section - included test reports as a sub-section and analyse them

the way that im using jenkins as a pipeline means i can automate the code.
jenkins also handled my test automation and some screenshots of tests passing and faileing and wha ti encountered with the test.

7. Future Steps: further analysis, what would i do next if i continued with this project id add this feature create new database relationship etc.

8. Licensing: i used vscode i used mysql for database

9. Contributors: w3schools, Qa community, bootstrap, Innocent website

10. Acknowledgements: to trainer, colleagues etc.

## 1. Project Overview

I have created an online storefront that fully conforms to a provided client specification. The website was made with ease of use and attractiveness in mind, and provides information about various products, product categories, pricing, and upcoming sales. 

I have used the following technologies in my project:

1. Kanban (via Jira) for project management and agile framework
2. Git as the version control system
3. GitHub for source code management 
4. HTML, CSS, JavaScript and Bootstrap for front-end development
5. Python as the back-end programming language
6. Flask as the API development platform
7. MySQL as the database management system

My overarching objective for this project was to create a fully functioning application with full documentation around utilisation of the supporting tools and technologies. 

## 2. How I used Agile Methodology

How I organised Sprints: utilisation of Sprints, There is time for two 2-day Sprints before the site is scheduled to "go live". take 10 minutes in each morning to plan out your day. you should be planning your actual work time in easy to manage chunks, database then html etc. just describe how you've broke it down. required to track your designs and workflow throughout the duration of the project, with emphasis on how Agile methodology shaped the application over time write down sprints where i plan what to do each time. prioritised the mvp so worked on those first, then scheduled time slots for extra features 