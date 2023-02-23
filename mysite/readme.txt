/* Name: Vincent Nguyen */

Below is all the info about this assignment and how to run the website locally:

For this assignment, I use the Django framework and Python for backend.
This is the second time that I'm using this framework. For frontend, 
I use Bootstrap 5 and Charts.js for graphs and charts.
I actually wanted to add more to the website (3D interactive graph, etc.), but
I didn't want to compromise the performance of the page. The assignment is kinda
open-ended so I'm not sure if this is considered "interactive" enough, but I can
totally make it even more sophisticated. 


Instructions to run the website locally:

PREREQUISITES: This program needs Python and Django already installed in your system.
If you don't have those already, you can download using command line. 

+ Open command line
+ cd to the outer "mysite" directory (where manage.py is located)

SET UP OUR DATABASE
+ Run 
	$ python manage.py makemigrations calls 
	(Explanation: to create migrations for any new model we create.
	If there's no changes in the models, it will say "No changes detected in app 'calls'")
	
	$ python manage.py migrate
	(Explanation: to apply those changes to the database
	If there's no changes, it will say "No migations to apply")
	
	$ python addExcelFile.py
	(if the data from the excel file is not in our database already)
	
(Optional) SET UP ADMIN PAGE
+ Run: $ python manage.py createsuperuser
	and then input username, email address, and password as prompted 

RUN THE USER PAGE
+ Run: $ python manage.py runserver
	then open this: http://127.0.0.1:8000/calls/ or http://localhost:8000/calls in your Web browser
	(I recommend Chrome for optimal result)
	
If you have any trouble with any of the above steps, please email me. 